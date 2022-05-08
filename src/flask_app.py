from flask import Flask, render_template, url_for, flash, redirect, request
from solar_weather_fetcher import SolarWeatherFetcher
from solar_flare_fetcher import SolarFlareFetcherSWL
from solar_flare_fetcher import SolarFlareFetcherNOAA
from alerts_backend import Alerts
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import forms
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


@app.route("/")
def home():
    return render_template("index.html")


#@app.errorhandler(Exception)
#def error_handler(error):
#    return ("<h1> That page does not exist. </h1>")


@app.route("/wind")
def solar_wind():
    return render_template("graph.html")


@app.route("/wind/<data>")
def solar_wind_graphs(data):
    if(data == "all"):
        temperature = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "temperature")
        density = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "density")
        speed = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "speed")
        time = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "time_tag")
        return render_template("activities.html", temperature=temperature, density=density, speed=speed, time=time)
    else:
        data1 = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", data)
        time = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "time_tag")

        if data == 'temperature':
            axis = 'Temperature (K)'
        elif data == 'density':
            axis = 'Density (1/cm^3)'
        elif data == 'speed':
            axis = 'Speed (km/s)'

        return render_template("test.html", data1=data1, data2=time, data3=axis)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/community")
def community():
    return render_template("community.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/solarflare")
def solar_flare():
    swl_data = SolarFlareFetcherSWL.fetch_website_data()
    noaa_data = SolarFlareFetcherNOAA.fetch_website_data()
    return render_template("solar_flare.html", data1=swl_data[0], data2=swl_data[1], data3=swl_data[2], data4=noaa_data[0],
                           data5=swl_data[1], data6=noaa_data[2], data7=noaa_data[3])


@app.route("/feed/<selection>")
def feed(selection):
    al = Alerts()
    temperature = False
    speed = False
    density = False

    selection = int(selection)

    if selection & 1 == 1:
        temperature = True
    if (selection >> 1) & 1 == 1:
        speed = True
    if (selection >> 2) & 1 == 1:
        density = True

    al.customize_alerts(density, speed, temperature)
    response = al.get_custom_alert()

    return render_template("feed.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)

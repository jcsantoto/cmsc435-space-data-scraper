import argparse
from alerts_backend import Alerts
from data_fetcher import SolarWeatherFetcher
from SolarFlareFetcher import SolarFlareFetcherSWL
from SolarFlareFetcher import SolarFlareFetcherNOAA

parser = argparse.ArgumentParser(description="For each of the commands below type the command followed by the argument"
                                             "to specify the action you want to perform.")

parser.add_argument(
    '-show',
    type=str,
    help="Enter \"Categories\" to navigate a list of the available space data categories"
)

parser.add_argument(
    '-get',
    type=str,
    help="Enter \"SolarData\" to view information about solar weather activity"
)

parser.add_argument(
    '-download',
    type=str,
    help="Enter \"30daySolar\" to download file of 30 day data"
)

parser.add_argument(
    '-view',
    type=str,
    help="Enter \"DailySolarFlare\" to see daily solar flare activity data"
)

parser.add_argument(
    '-check',
    type=str,
    help="Enter \"Feed\" to be alerted of changes in the solar wind speed"
)

args = parser.parse_args()

show = args.show if args.show else ''
get = args.get if args.get else ''
download = args.download if args.download else ''
view = args.view if args.view else ''
check = args.check if args.check else ''

if show != '':
    if show == "Categories":
        print("Right now you can access Solar Wind Density, Solar Wind Temperature, Solar wind Speed, and Solar Flare "
              "activity.")
    else:
        print("error: unrecognized command \"-show {0}\". Try \"-show Categories\" instead".format(show))

if get != '':
    if get == "SolarData":
        print(SolarWeatherFetcher.format_website_data())
    else:
        print("error: unrecognized command \"-get {0}\". Try \"-get SolarData\" instead".format(get))

if download != '':
    if download == "30daySolar":
        """
       today = date.today()
        yesterday = today - timedelta(days=30)

        print(yesterday)
        """
    else:
        print("error: unrecognized command \"-download {0}\". Try \"-download 30daySolar\" instead".format(download))

if view != '':
    if view == 'DailySolarFlare':
        print(SolarFlareFetcherSWL.format_website_data())
        print("{0} \n\n".format(SolarFlareFetcherNOAA.format_website_data()))
    else:
        print("error: unrecognized command \"-view {0}\". Try \"-view DailySolarFlare\" instead".format(view))

if check != '':
    if check == 'Feed':
        print(Alerts.get_alert())
    else:
        print("error: unrecognized command \"-check {0}\". Try \"-check Feed\" instead".format(check))

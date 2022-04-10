FROM python:3
ADD data_fetcher.py /
RUN pip install requests
RUN pip install beautifulsoup4
CMD ["python", "./data_fetcher.py"]
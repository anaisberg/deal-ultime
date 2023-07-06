# get all the current Deals from le Guide Ultime

## Prerequisites

For the code to work, you will need:

- [python3](https://www.python.org/downloads/) installed.

- Create your python environment: `python3 -m venv dealutltimeenv` 
- Activate the virtual environment
source `dealutltimeenv/bin/activate` (If you want to deactivate your environment, just type `deactivate` in the terminal.)


<!-- - install Flask: `pip3 install flask`
- install Selenium: `pip install selenium` or `pip3 install selenium` -->
- [Chrome](https://www.google.com/chrome/) installed, try to have the latest version
- and the [driver for Chrome](https://sites.google.com/chromium.org/driver/downloads)

Make sure to match the browser and driver versions, Chrome 96, as of this writing.

Credits: I used [this article](https://dev.to/anderrv/intro-to-web-scraping-with-selenium-in-python-4011) to help me get started.


## Run the app
- Make sure that our virtual env is active: `source dealutltimeenv/bin/activate`
- Export our app.py file to tell the flask server where to look for the file: `export FLASK_APP=app.py`
- Run flask in the terminal: `flask run`
- Open `http://localhost:5000/` in your navigator.
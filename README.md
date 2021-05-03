# A simple Flask Application 

First off, this is all largely borrowed from [RealPython](https://realpython.com/flask-by-example-part-1-project-setup/) and various other sites, pages, and people - not really anything that I have contributed organicly.

This is a simple 'quick n simple' Python-Flask application tutorial written for general useage of Python/Flask, forms processing (GUI), and local deployment/dubugging. This will help a new (but probably not noob) Pythonista learn how to set up a basic web server application in Python with Flask running on a local server, and assumes that the the developer is using Visual Studio Code as their IDE of choice.

Flask is a Model-View-Controller (MVC) framework (see [this page](https://www.guru99.com/mvc-vs-mvvm.html) for some insight to what MVC is and isnt, and also Real Python's [MVC Explained](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/) page for more details.

This readme will walk through the steps to make a basic user-interactive web-application using Flask and Python (and a few other simple additions that are easy to install).  If you just want to look at the final product, look at the [app.py](app.py) file where it is all completed and comments, docstrings, and more are added to help explain things.

## Getting started

Create the Python virtual environment - this only needs doing ONCE

    python3 -m venv venv

Activate (e.g. use) the virtual enviroment - do this EVERY time

    source venv/bin/activate

For Windows command line:

    venv\Scripts\activate

Create a 'requirements.txt' file that lists all of the libraries that we will use. For now, just add the following line:

    Flask==1.1.2

Install the requirements file like so (update this file everytime you permanently add a library that you need to use and then rerun this command):

    pip install -r requirements.txt

## Hello world! - a static beginning

Create a file named `app.py` that is parallel to the `requirements.txt` file and the virtual environment (`venv`) folder with the following content:

    from flask import Flask

    app = Flask(__name__)
export 
    @app.route("/")
    def index():
        return "Hello World!"

Run this minimalist web application with the following commands:

    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run

For Windows command line:

    set FLASK_ENV=development
    set FLASK_APP=app.py
    flask run

Exporting the `FLASK_ENV` as `development` enables some nice features that we will explore later on (see Visual Studio's [Run the App Debugger](https://code.visualstudio.com/docs/python/tutorial-flask#_run-the-app-in-the-debugger) page fore more info on how to setup/use it from within VS), and disables some anoying reminders to NOT use this in 'production' without a proper WSGI (or similar interface).

Exporting the `FLASK_APP` is not strictly necessary, since we are using the default name for our application python file, but it is a good idea to be fimiliar with the variable and it's usage.

Now that the applicatrion is running, browse the local system on port `5000` (typically http://localhost:5000/).  When you do, you should see the friendly message "Hello World!" in your browser and the following in the terminal where the application is running:

    ❯ flask run
    * Serving Flask app "app.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 290-425-530
    127.0.0.1 - - [25/Apr/2021 12:04:00] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [25/Apr/2021 12:04:01] "GET /favicon.ico HTTP/1.1" 404 -

## Forms - interacting with users

...TBD/In progress ;)
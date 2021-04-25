#!/usr/bin/env python3

# We need Flask for all the webby things to follow
from flask import Flask

# Datetime is needed for telling time
from datetime import datetime

# RE is a common regular-expression library that is great for parsing strings 
# and data - and is a 'built-in' library for Python3 installations.
import re


###
# Initialize our FLASK application object from the Flask class like so:
app = Flask(__name__)

@app.route("/")
def index():
    """
    Our first (topmost) route (aka 'view').  Routes are like URLs, 
    which we can access from a browser. The line immediately below is known as a 
    'decorator' and implements some boilerplate code for us without much work on 
    our end.  Basically it creates a 'view' to our app and data to show the user.
    This one merely shows a static message.  Easy-peasy.
    """
    return "Hello World!"

@app.route("/hello/<name>")
def hello_there(name):
    """
    This route shows a bit more of what we can do, including some 'REST'full user 
    interaction.  If a user specifies a name in the url like so: http://localhost/hello/supercoder
    the response will include the value 'supercoder' in the `name` variable, and 
    can then be validated with the RE `match_object` output.  If an invalid value is specified
    for `name` the validator code will simply assign 'friend' value to the `clean_name`
    instead.  If no value is specified, it will error out and present a 404 error to the browser.
    """
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    # Output the semi-static text with the time and supplied name (if any)
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
# In this code ,
# We will take inputs and try to call the APIs and then return the result.

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

# Now we will write
# a function which will take all 3 data from the form , execute an API and return the
# result .

@app.route('/weatherapp',methods=['POST',"GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form.get("city"), #city is the id here and this way we take input from form .
        'appid':request.form.get("appid"),
        'units':request.form.get("units")
    }
    response = requests.get(url,params=param) 
    # requests is used to get data from a url whereas request is used to get data from a form.
    data = response.json()
    return f"data : {data}" # here 'f' means formatted string.


if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5002)

# Now this is working in our local system .
# Next step is to deploy these things in the cloud through GitHub.
# We have to make this application global .

# requirements.txt is used to keep all the dependencies.
'''
Cloud gives us a blank system , so when we think of deploying an app over there,
we need to install the libraries(that are required) over there.

keeping all modules that need to be installed for a particular project in one single file
so that we can install all the modules in bulk at one go by using the command below.
pip install -r requirements.txt

The Flask == some number
gunicorn == some number , these numbers are version numbers of the modules.

Take the latest versions always.

We are going to push this app from local system(pwskills lab here) to git to cloud.



'''



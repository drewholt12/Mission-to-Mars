from flask import Flask, render_template, redirect, url_for  # use flask to render a template, redirect to another url, and create a url
from flask_pymongo import PyMongo # use pymongo to interact with our mongo db
#import scraping # use scraping code, we will convert our file from jupyter notebook to python

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"  # tells python our app will connect to mongo using URI (uniform resource identifier, like a URL)
mongo = PyMongo(app) 

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()  # uses pymongo to find the mars collection in our db and assign as mars
   return render_template("index.html", mars=mars) # tells flask to return the html tmeplate using an index.html file, and use mars collection

# set up scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars  # access db using variable
   mars_data = scraping.scrape_all()  #new variable to hold the scraped data
   mars.update({}, mars_data, upsert=True)  # updates the db  {} is an empty json object, use the mars data we stored, upsert creates a new document
   return redirect('/', code=302) # redirects to see the updated/new content

# tell flask to run 
if __name__ == "__main__":
   app.run()
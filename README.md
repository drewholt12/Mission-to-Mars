# Mission-to-Mars
## Purpose
Use BeautifulSoup, Splinter, and Pandas to scrape web sites for text and images.  Then use MongoDB, Flask, and bootstrap to customize the HTML display of the collected data.  
## Dependencies
-	Splinter
-	BeautifulSoup
-	Pandas
-	ChromeDriverManager
-	MongoDB
-	Flask

## Overview
Mars exploration information is scattered across the web.  We are attempting to scrape data and images from various websites into a Mongo Data Base.  Then use that data to create a one stop website for all things Mars exploration related.  We began by using a jupyter notebook to create an ipynb file, testing our code along the way.  The file began with creation of a variable that would call the url of our selected websites.  We added a delay to compensate for server and ISP speeds.  We converted the html from the website that was visited to a soup object which could them be sorted and analyzed for the data we desire.  The sites utilized are redpalanetscience.com for mars news, spaceimages-mars.com for the featured image, , galaxyfacts-mars.com to compare facts with earth facts, and marshemipheres.com for high resolution jpg images of the mars hemispheres.  
Once the code worked in jupyter, it was transferred to a python file title scraping.  This file defined functions for accessing the websites, transfer to soup objects, scraping the desired data, and saving to a mongo data base.  A scrape all function starts the process of executing code to visit the websites and creates a dictionary to store the desired results.  A function for each data type is nested within this function where each website is visited and scraped.  Another python file was created called app.  This file holds the flask code to utilize mongo database with flask.  
Finally, an HTML file was created to display our data.  A “get new data” button is front and center at the top of the page so that users can get the most up to date mars data.  The HTML file works for various screen sizes and adjusts automatically. 

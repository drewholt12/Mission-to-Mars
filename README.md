# Mission-to-Mars
## Purpose
Use BeautifulSoup, Splinter, and Pandas to scrape web sites for text and full resolution images.  Then use MongoDB to store the data, Flask, and bootstrap to customize the HTML display of the collected data.  
## Dependencies
-	Splinter
-	BeautifulSoup
-	Pandas
-	ChromeDriverManager
-	MongoDB
-	Flask

## Overview
Mars exploration information is scattered across the web.  We are scrapeing data and images from various websites into a Mongo Data Base.  Then use that data to create a one stop website for all things Mars exploration related.  We began by using a jupyter notebook to create an ipynb file, testing our code along the way.  The file began with creation of a variable that would call the url of our selected websites.  We added a delay to compensate for server and ISP speeds.  We converted the html from the website that was visited to a soup object which could them be sorted and analyzed for the data we desire. The sites utilized are redpalanetscience.com for mars news, spaceimages-mars.com for the featured image, galaxyfacts-mars.com to compare facts with earth facts, and marshemipheres.com for high resolution jpg images of the mars hemispheres.

### redplanetscience.com

![redplanet](https://user-images.githubusercontent.com/79231355/130620516-ea196081-8df5-4656-a29a-9fc4c9e1ff06.png)

### spaceimages-mars.com - low res images

![image_scrape](https://user-images.githubusercontent.com/79231355/130620681-b0d65486-f2af-440e-86ba-a41e89788ecb.png)

### galaxyfacts-mars.com

![mars_facts](https://user-images.githubusercontent.com/79231355/130620715-da16f86a-7ccc-45d3-b46a-c54129ea4e3e.png)

### marshemispheres.com  high-res images loop

![image_loop](https://user-images.githubusercontent.com/79231355/130621102-2e649438-35e6-4ca8-b80e-c34a88c20d42.png)

 
Once the code worked in jupyter, it was transferred to a python file title scraping.  This file defined functions for accessing the websites, transfer to soup objects, scraping the desired data, and saving to a mongo data base.  

### Scraping

![scrape](https://user-images.githubusercontent.com/79231355/130620918-7e32d1ce-de5b-4fb3-90a2-dbd69d6c2b8d.png)

### Flask

![flask](https://user-images.githubusercontent.com/79231355/130621172-a8ad45b1-7c4c-4f15-88f1-aa00c0d7d55c.png)

### Web Page Screenshots

![Screenshot 1](https://user-images.githubusercontent.com/79231355/130629013-6989bc32-48db-4fda-97b1-dadcd02f5029.png)
![Screenshot 2](https://user-images.githubusercontent.com/79231355/130629018-e9a16b5d-7011-4210-9f05-7cca5ce9fa8f.png)



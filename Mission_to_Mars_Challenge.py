#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = bs(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

# In[13]:


# web page is html table formatt.  using pandas to read the html and scrape for what we need. 
df = pd.read_html('https://galaxyfacts-mars.com')[0]  # create dataframe from html table, index of 0 pulls 1st table it encounters and returns a df
df.head()


# In[14]:


df.columns=['description', 'Mars', 'Earth']  # assign columns to new df
df.set_index('description', inplace=True) # set index to description column, inplace=true means the updated index will remain in place without reassigning to new variable. 
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars??? Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[18]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
# scrape page into soup
html = browser.html
soup = bs(html, "html.parser")


# In[19]:


# Find hemisphere image link and title
mars_hemispheres = soup.find_all('div', class_='description')
mars_hemispheres


# In[20]:


# loop through and select HTML link under href and grab the jpeg
for img in mars_hemispheres:
    # find link with references
    link_ad = soup.find('div', class_ = 'item')
    img_url = img.a['href']
    # set up link full url
    img_link = 'https://marshemispheres.com/' + img_url
    # Visit each link
    browser.visit(img_link)
    
    # dictionary to hold the urls/titles
    hemisphere_dict = {}
    
    # reparse html
    html = browser.html
    soup = bs(html, "html.parser")
    
    # get jpg image
    img_click = soup.find('img', class_='wide-image')
    img_jpg = img_click['src']
    img_jpg_url = f'https://marshemispheres.com/{img_jpg}'
    
    # get title
    hemi_title = soup.find('h2', class_='title').get_text()
    
    # append title/img to dict
    hemisphere_dict['title'] = hemi_title
    hemisphere_dict['img_url'] = img_jpg_url
    
    # append dict to list
    hemisphere_image_urls.append(hemisphere_dict)  
    
    #send browser back to main url page to restart search
    browser.back()
print(hemisphere_image_urls)


# In[21]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[22]:


# 5. Quit the browser
browser.quit()  #closes the auto browser


# In[ ]:





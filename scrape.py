# Import libraries
import requests
from bs4 import BeautifulSoup as bs
import csv
import re

# Obtain data from website to scrape
response = requests.get('https://webscraper.io/test-sites/e-commerce/scroll')

# Prepare the data with Beautiful Soup
soup = bs(response.content, 'html.parser')

# Scrape the elements

# Get all titles
titles = soup.find_all(['a'], attrs={'class':'title'})

# Get all descriptions
descriptions = soup.select('.description')

# Get all prices
prices = soup.select('.price')

# Get all reviews
reviews = soup.select('.ratings > .pull-right')

# Create list to store values
finaldata = []

# Add file headers
finaldata.append(["Title","Description","Price","Reviews"])

# Start loop to store the data inside a list
for i in range(len(titles)):

    # Get the title
    title = titles[i]['title']

    # Get description
    desc = descriptions[i].get_text()

    # Get the price
    price = prices[i].get_text()

    # Get the number of reviews
    review = reviews[i].get_text()

    # Append data into the list
    finaldata.append([title, desc, price, review])

# Open csv file
with open('results.csv', 'w', newline='') as results:
    
    # Create instance of csv writer
    writer = csv.writer(results)
    
    # Start loop to write data into csv file
    for row in finaldata:
        
        # Write row of data
        writer.writerow(row)

# Close file and finish
results.close()
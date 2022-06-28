from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

#endpoints to /read :{national, business, sports, world, politics, technology, startup , entertainment, miscellaneous, hatke, science, automobile}
website = "https://inshorts.com/en/read/technology"

# local path to the chromedriver
path = "/home/hashmap/chromedriver"

# headless mode
options = Options()
options.headless = True



# Drivers init
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

#find elements

# init main element
containers = driver.find_elements(by="xpath", value='/html/body/div[@class="container"]/div[@class="row"]/div[@class="card-stack"]/div/div[@class="news-card z-depth-1"]/div[@class="news-card-title news-right-box"]')



# delcare objects to hold the elements

title=[]
author=[]
timestamp=[]
date=[]

# loop via sub elements
for container in containers:
    Title = container.find_element(by="xpath", value='./a/span[@itemprop="headline"]').text
    Author = container.find_element(by="xpath", value='./div[@class="news-card-author-time news-card-author-time-in-title"]/span[@class="author"]').text
    Timestamp = container.find_element(by="xpath", value='./div[@class="news-card-author-time news-card-author-time-in-title"]/span[@class="time"]').text
    Date = container.find_element(by="xpath", value='./div[@class="news-card-author-time news-card-author-time-in-title"]/span[@clas="date"]').text

    # append objects to iterations
    title.append(Title)
    author.append(Author)
    timestamp.append(Timestamp)
    date.append(Date)


# define a dicitory for feilds to extract and save
my_dictionary = {'Title':title, 'Timestamp':timestamp,'Author': author, 'Date':date}


# export data to csv using pandas - data frame
df_headlines = pd.DataFrame(my_dictionary)
df_headlines.to_csv('shorts-headless.csv')

#close driver (browser instance)
driver.quit()


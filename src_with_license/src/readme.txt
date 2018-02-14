
Quick Start:

steps:

#step 1 : import Spider class from spider module
from scrapy_module.spider import Spider

url='http://example.com/#'  #start URL
allowed_domain='http://example.com/' #assign the domain which it should crawling in


#step 2: create  spider object and pass varibales(Url and allowed_domain)
spider=Spider(url,allowed_domain)


#step 3:assign project name (this will be output file name)
spider.ProjectName=ProjectName


#step 4: run spider function to start crawling
#it gets output_data and links as return value from spider function
#output_data is dict it has url and data as key/value pairs
#links get list of all urls grabbed

output_data,links=spider.spider()

________________________________________
Example :
from scrapy_module.spider import Spider

url='http://njpc.goonj.org/#'
allowed_domain='http://njpc.goonj.org/'

spider=Spider(url,allowed_domain)
spider.ProjectName=ProjectName

output_data,links=spider.spider()
________________________________________

--------------------------------------------------------------------------------------------------------------


OUTPUT FILES:
we can get output either in .TXT file or  .JSON format


To get TEXT file as output :
# set objectInstance.txt_output= True

Example:
spider.txt_output=True




To get JSON file as output :
# set objectInstance.json_output=True= True

Example:
spider.json_output=True=True

_______________________________________________
EXAMPLE:

from scrapy_module.spider import Spider

url='http://njpc.goonj.org/#'
allowed_domain='http://njpc.goonj.org/'

spider=Spider(url,allowed_domain)
spider.ProjectName=ProjectName

spider.json_output=True
spider.txt_output=True

output_data,links=spider.spider()
________________________________________________


--------------------------------------------------------------------------------------------------------------

#Scrape given only  URL :


#it scrapes only given url  and doesn't crawl other urls in page
spider.is_recursive=False


____________________________________________________________

example:

from scrapy_module.spider import Spider

url='http://njpc.goonj.org/#'
allowed_domain='http://njpc.goonj.org/'

spider=Spider(url,allowed_domain)
spider.ProjectName=ProjectName

spider.is_recursive=False

output_data,links=spider.spider()
____________________________________________________________


------------------------------------------------------------------------------------------------------------------


ADD NEW TAGS AND TO REMOVE TAGS FROM SCRAPER:

STEPS TO ADD TAGS:

#step 1: get list of tags which needs to be added
add=['code','label']

# step 2:call add_tags function and pass list of tags to be added to function
spider.add_tags(add)



STEPS TO REMOVE TAGS:

#step 1: get list of tags which needs to be removed
remove=['code','label']

# step 2:call remove_tags function and pass list of tags to be removed from list
 spider.remove_tags(remove)


---------------------------------------------------------------------------------------------------------------------

GETS TAG LIST OF SCRAPER:

STEPS TO GET TAGS :

#step: call get_tags_list function

tags=spider.get_tags_list()

----------------------------------------------------------------------------------------------------------------------

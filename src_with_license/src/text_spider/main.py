#!/usr/bin/python

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))



from text_spider.spider import Spider


# url='http://njpc.goonj.org/#'
# allowed_domain='http://njpc.goonj.org/'
# # ProjectName='njpc'


url='http://davschoolbangalore.in'
allowed_domain='http://davschoolbangalore.in'
ProjectName='DAV'

# remove_tags=['div','li','br\\']
add=['div','code','label']

spider=Spider(url,allowed_domain)
# spider.ProjectName=ProjectName
spider.json_output=False
spider.txt_output=True
spider.is_recursive=True
spider.add_tags(add)

# spider.remove_tags(remove_tags)
# tags=spider.get_tags_list()
# print(tags)

output_data,links=spider.spider()
print('--------------------------------------------------')
# print(output_data[links[0]])
print('--------------------------------------------------')
print(links)




def func(url,allowed_domain,ProjectName):
    import sys
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from scrapy_module.spider import Spider

    spider=Spider(url,allowed_domain)
    spider.ProjectName=ProjectName

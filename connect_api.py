import requests
import json

# variables for querying the API
number=''
enumeration_type=''
taxonomy_description=''
name_purpose=''
first_name='jo*'
use_first_name_alias=''
last_name=''
organization_name=''
address_purpose=''
city=''
state=''
postal_code=''
country_code=''
limit=''
skip=''
pretty=''
version=2.1


# get first result
url = "https://npiregistry.cms.hhs.gov/api/?number={}&enumeration_type={}&taxonomy_description={}&name_purpose={}&first_name={}&use_first_name_alias={}&last_name={}&organization_name={}&address_purpose={}&city={}&state={}&postal_code={}&country_code={}&limit={}&skip={}&pretty={}&version=2.1"
url = url.format(number,enumeration_type,taxonomy_description,name_purpose,first_name,use_first_name_alias,last_name,organization_name,address_purpose,city,state,postal_code,country_code,limit,skip,pretty)
r = requests.get(url)
results_json = r.json()
print(results_json['results'][0])

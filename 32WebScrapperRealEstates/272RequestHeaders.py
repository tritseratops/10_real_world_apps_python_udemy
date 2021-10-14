import requests, pandas
from bs4 import BeautifulSoup

"""
get link on beautiful soup and retrieves all estates from it 
"""
def get_estates(bs):
    all_estates_tags = bs.findAll("div", {"class": "propertyRow"})
    print(len(all_estates_tags))
    estates = []
    for estate in all_estates_tags:
        features = {}
        price = estate.find_all("h4", {"class":"propPrice"})[0].text.strip()
        features['price']=price
        address1 = estate.find_all("span", {"class":"propAddressCollapse"})[0].text.strip()
        features['address1'] = address1
        address2 = estate.find_all("span", {"class": "propAddressCollapse"})[1].text.strip()
        features['address2'] = address2
        beds_tags= estate.find_all("span", {"class": "infoBed"})
        beds = 0
        if (beds_tags != []):
            beds = beds_tags[0].find("b").text.strip()
            features['beds'] = beds
        baths_tags = estate.find_all("span", {"class": "infoValueFullBath"})
        baths = 0
        if (baths_tags != []):
            baths = baths_tags[0].find("b").text.strip()
            features['baths'] = baths

        additional_attributes = estate.find_all("div", {"class":"columnGroup"})

        for attribute in additional_attributes:
            spans = attribute.find_all("span")
            if(len(spans)!=0):

                # print(attribute)
                feature_group = attribute.find_all("span", {"class": "featureGroup"})[0]
                feature_key = feature_group.text.split(sep=":")[0]
                features[feature_key] = []
                for feature_item in attribute.find_all("span", {"class": "featureName"}):
                    # print(feature_item)
                    features[feature_key].append(feature_item.text)
        estates.append(features)
    return estates



search_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"


r = requests.get(search_url,
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
bs = BeautifulSoup(r.content, "html.parser")
#find number of page (#PageNumbers)
pages_container = bs.findAll("span", {"id": "PageNumbers"})[0]
pages_links = pages_container.findAll("a")
max_page = len(pages_links)
# print("Max Page:"+str(max_page))

all_estates = []
first_estates = get_estates(bs)
all_estates.extend(first_estates)

for page_id in range(1, max_page+1):
    page_url = search_url + "t=0&s="
    current_page=page_url+str(page_id)+"0.html"
    r = requests.get(current_page,
                     headers={
                         'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    bs = BeautifulSoup(r.content, "html.parser")
    estates_on_current_page =  get_estates(bs)
    all_estates.extend(estates_on_current_page)
    print(page_id)


# print("Estates num:"+str(len(estates)))
# for estate in estates:
#     for feature_name, feature_values in estate.items():
#         print(str(feature_name) +":"+str(feature_values))


# http://pythonhow/real-estate/rock-springs-wy/LVWYROCKSPRINGS/
# http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
df = pandas.DataFrame(all_estates)
print(df)
df.to_csv("output.csv")

#TODO find why there are 37 entries instead of 17 , hints - 25 per page
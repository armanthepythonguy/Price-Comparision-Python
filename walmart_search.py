import requests

def walmartSearch(keyword):
    url = "https://axesso-walmart-data-service.p.rapidapi.com/wlm/walmart-search-by-keyword"
    querystring = {"keyword":keyword,"page":"1","sortBy":"best_match"}
    headers = {
        'x-rapidapi-host': "axesso-walmart-data-service.p.rapidapi.com",
        'x-rapidapi-key': "2bd459e39emsh0af302602dde003p180f97jsn8385827d271d"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    walmart_Data = []
    walmart_Avg = 0
    for i in range(5):
        item = response['item']['props']['pageProps']['initialData']['searchResult']['itemStacks'][0]['items'][i]
        if item['price'] == 0:
            walmart_Price = item['priceInfo']['minPrice']
        else:
            walmart_Price = item['price']
        walmart_Avg += walmart_Price
        walmart_Data.append({"title":item['name'],"price":"$"+str(walmart_Price),"image":item['image'],"link":"walmart.com"+item['canonicalUrl']})
    walmart_Avg /= 5
    return {"walmart_Avg":walmart_Avg,"walmart_Data":walmart_Data}
import requests
def ebaySearch(keyword):
    url = "https://ebay-product-search-scraper.p.rapidapi.com/index.php"
    querystring = {"query":keyword}
    headers = {
        'x-rapidapi-host': "ebay-product-search-scraper.p.rapidapi.com",
        'x-rapidapi-key': "2bd459e39emsh0af302602dde003p180f97jsn8385827d271d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    ebay_Data = []
    ebay_Avg = 0
    for i in response['products'][0:5]:
        if "to" in i['price']:
            ebay_Price = i['price'].split(" to ")[1]
        else:
            ebay_Price = i['price']
        ebay_Data.append({"title":i['name'],"price":ebay_Price,"image":i['image'],"link":i['link']})
        ebay_Avg += float((ebay_Price.split("$"))[1])
    ebay_Avg /= 5
    return {"ebay_Avg":ebay_Avg,"ebay_Data":ebay_Data}
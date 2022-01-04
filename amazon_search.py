import requests
def amazonSearch(keyword):
    url = "https://amazon-price1.p.rapidapi.com/search"
    querystring = {"keywords":keyword,"marketplace":"US"}
    headers = {
        'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
        'x-rapidapi-key': "2bd459e39emsh0af302602dde003p180f97jsn8385827d271d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    amazon_Data = []
    amazon_Avg = 0
    for i in range(5):
        amazon_Avg += float((response[i]['price'].split("$"))[1])
        amazon_Data.append({"title":response[i]['title'],"price":response[i]['price'],"image":response[i]['imageUrl'],"link":response[i]['detailPageURL']})
    amazon_Avg /= 5
    return {"amazon_Avg":amazon_Avg,"amazon_Data":amazon_Data}
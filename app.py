from flask import Flask, jsonify
from amazon_search import amazonSearch
from ebay_search import ebaySearch
from walmart_search import walmartSearch
app = Flask(__name__)

@app.route('/search/<string:keyword>', methods=['GET'])
def search(keyword):
    amazonData = amazonSearch(keyword=keyword)
    ebayData = ebaySearch(keyword=keyword)
    walmartData = walmartSearch(keyword=keyword)
    return jsonify({"amazon":amazonData, "ebay":ebayData, "walmart":walmartData})



if __name__ == "__main__":
    app.run()
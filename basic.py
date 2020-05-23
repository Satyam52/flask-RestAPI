from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{"name": "MyStore", "items": [{"name": "item1", "price": "price1"}]}]


@app.route("/")
def home():
    return render_template("index.html")


# Post  /store date = {name:}
@app.route("/store", methods=["POST"])
def createStore():
    requestData = request.get_json()
    newStore = {"name": requestData["name"], "items": []}
    stores.append(newStore)
    return jsonify(newStore)


# Get   /store/<string name>
@app.route("/store/<string:name>")
def getStore(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "Not Found"})


# Get   /store
@app.route("/store")
def getAllStore():
    return jsonify({"stores": stores})


# Post  /store/<string name>/item date ={name:,price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def addItem(name):
    requestData = request.get_json()
    for store in stores:
        if store["name"] == name:
            newItem = {"name": requestData["name"], "price": requestData["price"]}
            store["items"].append(newItem)
            return jsonify(newItem)
        return jsonify({"message": "Store not found"})


# Get   /store/<string name>/item
@app.route("/store/<string:name>/item")
def getAllItems(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "Not Found"})


app.run(port=5000)

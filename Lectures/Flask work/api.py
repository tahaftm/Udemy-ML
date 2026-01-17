from flask import Flask,jsonify,request

app = Flask(__name__)

items = [{"name" : "Item 1", "description" : "This is Item 1", "id" : 1},{"name" : "Item 2", "description" : "This is Item 2", "id" : 2}]

@app.route("/")
def welcome():
    return "This is a simple TO DO list app"

@app.route("/items",methods = ["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>")
def get_item_by_id(item_id):
    for i in items:
        if i['id'] == item_id:
            return jsonify(i)
    return "Invalid ID"

## Creating a new task by using post
@app.route("/items", methods = ["POST"])
def new_item():
    data = request.get_json()
    if len(items) != 0:
        new_id = items[-1]['id'] + 1
    else:
        new_id = 1
    new_item = {
        "name" : data['name'],
        "description" : data["description"],
        "id" : new_id 
    }
    items.append(new_item)
    return jsonify(items)

##  PUT AND DELETE METHODS:
@app.route("items/<int:item_id>", methods = ['PUT'])
def updating_item(item_id):
    data = request.get_json()
    if not data:
        return {"error": "Invalid JSON"}, 404
    for i in items:
        if item_id == i['id']:
            i['id'] = data['id']
            i['name'] = data['name']
            i['description'] = data['description']
            return get_item_by_id(item_id)
    return {"error": "Item not found"}, 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
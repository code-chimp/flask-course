from flask import Flask, request

app = Flask(__name__)

# A list of stores, each store is represented as a dictionary with a name and a list of items.
stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    """
    GET /store
    Returns a list of all stores.

    Returns:
        dict: A dictionary containing a list of all stores.
    """
    return {"stores": stores}


@app.get("/store/<string:name>")
def get_store(name):
    """
    GET /store/<name>
    Returns a specific store by name.

    Args:
        name (str): The name of the store to retrieve.

    Returns:
        dict: The store with the specified name, or a 404 error message if not found.
    """
    for store in stores:
        if store["name"] == name:
            return store

    return {"message": "Store not found"}, 404


@app.post("/store")
def create_store():
    """
    POST /store
    Creates a new store with the provided name.

    Request Body:
        JSON: A JSON object containing the name of the new store.

    Returns:
        dict: The newly created store.
        int: HTTP status code 201 (Created).
    """
    data = request.get_json()

    new_store = {"name": data["name"], "items": []}
    stores.append(new_store)

    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    """
    POST /store/<name>/item
    Creates a new item in the specified store.

    Args:
        name (str): The name of the store to add the item to.

    Request Body:
        JSON: A JSON object containing the name and price of the new item.

    Returns:
        dict: The store with the newly added item.
        int: HTTP status code 201 (Created).
        dict: A 404 error message if the store is not found.
    """
    data = request.get_json()

    for store in stores:
        if store["name"] == name:
            new_item = {"name": data["name"], "price": data["price"]}
            store["items"].append(new_item)
            return store, 201

    return {"message": "Store not found"}, 404

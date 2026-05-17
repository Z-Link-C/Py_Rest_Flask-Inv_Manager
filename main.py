from flask import Flask, jsonify, request
from flask_cors import CORS
from app.services.inventory_service import (
    add_product, get_all, get_one, update_product, delete_product
)
app = Flask(__name__)
CORS(app)

@app.route("/inventory",methods=["GET"])
def view_all():
    return jsonify(get_all())

@app.route("/inventory/<id>",methods=["GET"])
def view_one(id):
    prod=get_one(id)
    if not prod:
        return jsonify({"error":"Product not found"}),404
    return jsonify(prod)

@app.route("/inventory",methods=["POST"])
def add():
    d=request.get_json
    if not d or "barcode" not in d:
        return jsonify({"error":"barcode is required"}), 400
    prod,err=add_product(d["barcode"],d.get("price"),d.get("stock"))
    if err:
        return jsonify({"error":err}),404
    return jsonify(prod),201

@app.route("/inventory/<id>",methods=["PATCH"])
def update(id):
    d=request.get_json()
    if not d:
        return jsonify({"error":"no data provided"}),400
    prod,err=update_product(id,d.get("price"),d.get("stock"))
    if err:
        return jsonify({"error":err}),404
    return jsonify(prod)

@app.route("/inventory/<id>",methods=["DELETE"])
def delete(id):
    _,err=delete_product(id)
    if err:
        return jsonify({"error":err}),404
    return jsonify({"message":f"Product {id} deleted"}),200
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route('/')
def home():
    return "Simple API is running"


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    name = data['name']
    quantity = data['quantity']
    price = data['price']

    total = quantity * price
    tax = total * 0.15
    final_total = total + tax

    product = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total,
        "tax": tax,
        "final_total": final_total
    }

    products.append(product)

    return jsonify({"message": "Product added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
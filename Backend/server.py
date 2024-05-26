# This Flask will act a Server 


from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection


app = Flask(__name__)

connection = get_sql_connection()

@app.route('/GetProducts', methods = ['GET'])

def get_products():
    products = products_dao.get_all_products(connection)

    # in Flask We have to jasonify the Response
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/deleteproduct', methods = ['POST'])

def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])

    # in Flask We have to jasonify the Response
    response = jsonify({'product_id':return_id})

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('Starting Python Flask Server For Grocery Store Application')
    app.run(port=5000)


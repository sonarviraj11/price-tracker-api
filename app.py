from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Visit /prices to see competitor data."

@app.route('/prices', methods=['GET'])
def get_prices():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"name": r[0], "price": r[1]} for r in rows])

if __name__ == '__main__':
    app.run(debug=True)

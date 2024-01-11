from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def welcome():
    return render_template('indexpr.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

if __name__ == '__main__':
    app.run(debug=True)

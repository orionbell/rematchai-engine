from flask import Flask, request

app = Flask(__name__)


@app.route('/engine/health', methods=['GET'])
def healthcheck():
    return "Healthy"


@app.route('/engine/sell', methods=['POST'])
def sell():
    return request.json


@app.route('/engine/buy', methods=['POST'])
def buy():
    return request.json


if __name__ == '__main__':
    app.run(port=8080, debug=False)

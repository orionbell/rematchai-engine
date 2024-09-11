from flask import Flask, request

app = Flask(__name__)


@app.route('/engine/health')
def healthcheck():
    return "Healthy"


if __name__ == '__main__':
    app.run(port=8080, debug=False)

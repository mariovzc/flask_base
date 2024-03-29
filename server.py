from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return jsonify({'api': 'ok'}), 200

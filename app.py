from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST request!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    return jsonify({'msg': 'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
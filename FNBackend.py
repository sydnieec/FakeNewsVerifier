from flask import Flask, request
app = Flask(__name__)
@app.route('/fakenewsapi', methods=['POST'])
def result():
    link = request.form['link']
    return link

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def data():
    return 'Working well client'


@app.route('/POST')
def post_data():
    r = requests.post('http://192.168.2.126:8443/query-example', params={'language': 'Any param. 1',
                                                                         'framework': 'Any param. 2'})
    return r.content


@app.route('/GET')
def get_data():
    r = requests.get('http://192.168.2.126:8443/')
    return r.content


if __name__ == '__main__':
    app.run(host='192.168.2.126', port=8444)

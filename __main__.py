from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def start():
    return 'Working well server'


@app.route('/query-example', methods=['GET', 'POST'])
def query_example():
    if request.method == 'POST':
        language = request.args.get('language')
        framework = request.args.get('framework')
        return '<h1>The language value is: {0}</h1><h2>The framework value is: {1}</h2>'.format(language, framework)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == '__main__':
    app.run(host='192.168.2.126', port=8443)

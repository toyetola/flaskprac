from flask import Flask
from flask import jsonify
from flask.templating import render_template

app = Flask(__name__)

""" @app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is "+ str(number+1)  

@app.route('/<string:name>/')
def hello(name):
    return "Hello," + name  

@app.route('/person/')
def person():
    return jsonify({'name':'Houdu', 'address':'Singapore'})    

@app.before_request
def before():
    print("This is executed before request")

@app.route('/home/')
def homePage():
    return "Home Page" """

@app.route('/')    
def index():
    return render_template('index.html', title='home')

@app.route('/about/')
def about():
    return render_template('about.html', title='about page')

@app.route('/contact/')
def contactPage():
    return render_template('contact.html', title='Contact page')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, use_reloader=True)

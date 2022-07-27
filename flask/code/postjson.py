from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

@app.route('/') #decorator drfines the   
def home():  
    return "hello, this website is for adding number";

@app.route('/processjson', methods=['GET', 'POST'])
def process():
    data = request.get_json()
    name = data['name']
    location = data['location']
    return jsonify({'name' : name , 'location' : location , 'result' : 'posted'})

if __name__ =='__main__':  
    app.run()
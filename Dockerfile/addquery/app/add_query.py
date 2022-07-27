from email.policy import default
from flask import Flask, request

app = Flask(__name__)

@app.route('/') #decorator drfines the   
def home():  
    return "hello, this website is for adding number";

@app.route('/add', methods=['GET'])
def add():
    args = request.args
    n1 = args.get("b" , default=0 , type = int)
    n2 = args.get("a" , default=0 , type = int)
    sum = n1 + n2
    return(str(sum))

if __name__ =='__main__':  
    app.run(host='0.0.0.0', port=5000)
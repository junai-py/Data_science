from flask import Flask
from flask import request,render_template,jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/math",methods=['POST'])
def math_ops():
    if request.method=="POST" :
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if ops =='add':
            result="The sum of {} and {} is {}".format(num1,num2,num1+num2)
        if ops =='subtract':
            result="The subtract of {} and {} is {}".format(num1,num2,num1-num2)
        if ops =='multiply':
            result="The multiply of {} and {} is {}".format(num1,num2,num1*num2)
        if ops =='divide':
            result="The divide of {} and {} is {}".format(num1,num2,num1/num2)
        return render_template("results.html",result=result)



@app.route("/postman_action",methods=['POST'])
def math_ops1():
    if request.method=="POST" :
        ops=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if ops =='add':
            result="The sum of {} and {} is {}".format(num1,num2,num1+num2)
        if ops =='subtract':
            result="The subtract of {} and {} is {}".format(num1,num2,num1-num2)
        if ops =='multiply':
            result="The multiply of {} and {} is {}".format(num1,num2,num1*num2)
        if ops =='divide':
            result="The divide of {} and {} is {}".format(num1,num2,num1/num2)
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
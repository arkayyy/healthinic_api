from flask import Flask, render_template,request, jsonify

app=Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/evaluate.html')
def evaluate():
    return render_template('evaluate.html')

@app.route('/evaluate.html',methods=["POST"])
def getInput():
    category1=request.form["knk"]
    return category1
    



@app.route('/test.html')
def disp():
    return render_template('test.html')

@app.route('/test.html',methods=['POST'])
def inputt():
    name=request.form["knk"]
    return name

if __name__=='__main__':
    app.run(debug=True)
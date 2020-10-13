from flask import Flask, render_template,request, jsonify, url_for

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
    inputs=request.form
    for key,value in inputs.items():
        if key=='category1':
            return value 
    



@app.route('/test.html')
def disp():
    return render_template('test1.html')

@app.route('/test.html',methods=['GET','POST'])
def inputt():
    s1=""
    s2=""
    if request.method=="POST":
        name=request.form
        n1=request.form
        #for key,value in name.items():
            #if key=='category':
                #s1=value
            #if key=="category1":
                #s2=value
    return n1
        #return name
    #else:
        #return render_template("test.html")

if __name__=='__main__':
    app.run(debug=True)
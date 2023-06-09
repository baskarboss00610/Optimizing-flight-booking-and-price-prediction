from flask import Flask,render_template, request
import numpy as np
import pickle

model=pickle.load(open(r"model1.pkl",'rb'))

app = Flask(__name__,template_folder="../templates")

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
@app.route("/predict")
def predict1():
    return render_template("predict.html")


@app.route("/pred",methods=['POST','GET'])
def predict():
    if request.method=='POST':
        x=[[x for x in request.form.values()]]
        print(x)
        
        x=np.array(x)
        print(x.shape)

        print(x)
        pred= model.rfr(x)
        return pred
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)


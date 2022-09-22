import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)

model = pickle.load(open("air.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index1.html")

@flask_app.route("/predict", methods = ["GET","POST"])
def predict():
    b = request.form.get('b')
    c = request.form.get('c')
    d = request.form.get('d')
    e = request.form.get('e')
    f = request.form.get('f')
    g = request.form.get('g')
    h = request.form.get('h')
    i = request.form.get('i')
    j = request.form.get('j')
    k = request.form.get('k')
    l = request.form.get('l')
    m = request.form.get('m')
    n = request.form.get('n')


    if b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i=='' or j=='' or k=='' or l=='' or m=='' or n=='':
            return "You can\'t leave any field empty!!!"

    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    g = float(g)
    h = float(h)
    i = float(i)
    j = float(j)
    k = float(k)
    l = float(l)
    m = float(m)
    n = float(n)

    arr=np.array([[b,c,d,e,f,g,h,i,j,k,l,m,n]])
    print(arr)
    prediction = model.predict(arr)
    return render_template("after1.html", data=prediction)

if __name__ == "__main__":
    flask_app.run(debug=True)
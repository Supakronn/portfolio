from flask import Flask,render_template,request,url_for
app=Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/sum',methods = ['get'])
def sum():
    S=0
    C1 = request.args.get('Cappuccino')
    C2 = request.args.get('Latte')
    C3 = request.args.get('Mocha')
    C4 = request.args.get('Americano')
    C5 = request.args.get('Espresso')
    P=[]
    L=[]
    User = request.args.get('name')
    if(C1!=None):
        L.append([C1,50])
        S+=50
    if(C2!=None):
        L.append([C2,100])
        S+=100
    if(C3!=None):
        L.append([C3,150])
        S+=150
    if(C4!=None):
        L.append([C4,200])
        S+=200
    if(C5!=None):
        L.append([C5,250])
        S+=250
    return render_template('summarize.html',order=L,name=User,sumP=S)

app.run(debug=True)
    
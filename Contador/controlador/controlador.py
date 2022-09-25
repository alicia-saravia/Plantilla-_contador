from Contador import app
from flask import Flask,render_template, request, redirect, session

import Contador

app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def raiz():
    if session.get("visitas") == None:
        session['visitas']=0
    if session.get('contador') == None:
        session['contador'] = 0
    valor = int(session['visitas'])+1
    session['visitas']= valor
    valor = int(session['contador'])+1
    session['contador'] = valor
    return render_template("index.html",visitas=session['visitas'], contador = session['contador'])

@app.route('/inicio' ,methods=['POST','GET'])
def inicio():
    session.pop('contador')
    return redirect("/")

@app.route('/suma2',methods=['POST'])
def  suma_2():
    if session.get("contador") == None:
            session['contador']=0
    valor = int(session['contador'])+2
    session['contador']=valor
    valor = int(session['visitas'])+1
    session['visitas']= valor
    return render_template("index.html", contador = session['contador'], visitas = session['visitas'])	 

@app.route('/sumar' , methods=['POST'])
def sumar():
    if session.get("visitas") == None:
            session['visitas']=0
    valor = int(session['contador']) + int(request.form['numero'])
    session['contador']=valor
    valor = int(session['visitas'])+1
    session['visitas']= valor
    return render_template("index.html",visitas = session['visitas'], contador = session['contador'])	 

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404
from . import app
from flask import render_template, flash, request
from CryptoSoft.templates.forms import Form
from CryptoSoft.models import *

url_BBDDates = app.config.get("BASE_DE_DATOS")
manager = BBDDoperations(url_BBDDates)
@app.route("/")
def movements():
    consult = "SELECT * FROM Movimientos ORDER BY fecha"
    movements_list = manager.consultation(consult)
    return render_template("movements.html", items = movements_list)

@app.route("/purchase", methods=['GET', 'POST'])
def exchanges():
    form = Form()
    calculator_pushed = False
    if request.method == 'GET':
        return render_template("exchanges.html", formulary=form)
    else:
        if form.validate():
            if form.calculadora.data:
                fcoin = request.form.get('coinsfrom')
                tcoin = request.form.get('coinsto')
                qf = request.form.get('quantityfrom')
                form.pu = 1 / ConectApi.conecta(fcoin, tcoin)
                form.quantityto = float(qf) / form.pu
                return render_template("exchanges.html", formulary=form)

            if form.submit.data:
                print("Boton aceptar")
            else:
                flash("Debe hacer el cálculo antes de enviar el formulario")
                pass
        else:
            return render_template("exchanges.html", formulary=form)

@app.route("/status")
def investment():
    return render_template("status.html")

@app.route("/saldo")
def saldo():
    consult = "SELECT * FROM saldo"
    saldo_list = manager.consultation(consult)
    return render_template('saldo.html', items=saldo_list)
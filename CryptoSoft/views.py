from werkzeug.utils import bind_arguments
from . import app
from CryptoSoft.forms import Form
from flask import render_template, flash, request, url_for, redirect
from CryptoSoft.models import *
from datetime import datetime

url_BBDDates = app.config.get("BASE_DE_DATOS")
manager = BBDDoperations(url_BBDDates)
api_key = app.config.get("API_KEY")

@app.route("/")
def movements():
    consult = "SELECT * FROM Movimientos ORDER BY fecha"
    try:
        movements_list = manager.consultation(consult)
        if len(movements_list) == 0:
            flash("No existen movimientos")
    except:
        flash("Error de conexión a la base de datos")
        return render_template("movements.html")
    return render_template("movements.html", items = movements_list)

@app.route("/purchase", methods=['GET', 'POST'])
def exchanges():
    lista=[("EUR", "EUR")]
    form = Form()
    if request.method == 'GET':
        form = Form()
        return render_template("exchanges.html", formulary=form)
    else:
        if form.validate():
            if form.calculadora.data:
                form.quantityfromH.data = form.quantityfrom.data
                if form.coinsfrom.data != 'EUR' and form.coinsfrom.data != "--Seleccione Criptomoneda--":
                    cantcoin = manager.consultation("SELECT {} FROM saldo".format(form.coinsfrom.data))
                    maxsale = cantcoin[0][form.coinsfrom.data]
                    if float(form.quantityfromH.data) > maxsale:
                        flash("No puede invertir una cantidad superior al saldo disponible")
                        return render_template("exchanges.html", formulary=form)
                if form.coinsfrom.data == "--Seleccione Criptomoneda--":
                    flash("Debe seleccionar una criptomoneda origen")
                    return render_template("exchanges.html", formulary=form)

                if form.coinsto.data == "0":
                    flash("Debe seleccionar un Criptomoneda destino")
                    return render_template("exchanges.html", formulary=form)
                if form.coinsfrom.data == form.coinsto.data:
                    flash("Las monedas de origen y destino no deben coincidir")
                    return render_template("exchanges.html", formulary=form)
                if form.quantityfrom.data <= 0:
                    flash("La cantidad debe ser un numero positivo mayor que 0")
                    return render_template("exchanges.html", formulary=form)
                try:
                    form.pu.data = 1 / ConectApi.conecta(form.coinsfrom.data, form.coinsto.data, api_key)
                except:
                    flash("Error de conexión con la API")
                    return render_template("exchanges.html", formulary=form)
                form.puH.data = form.pu.data
                form.quantityto.data = float(form.quantityfromH.data) / form.pu.data
                form.quantitytoH.data = form.quantityto.data
                return render_template("exchanges.html", formulary=form)

            if form.submit.data and form.puH.data != "":
                now = datetime.now()
                fecha = fecha = "{}/{}/{}".format(now.day, now.month, now.year)
                hora = "{}:{}".format(now.hour, now.minute)

                consult = "INSERT INTO movimientos (fecha, hora, coinsfrom, qf, coinsto, qt, pu) VALUES (?, ?, ?, ?, ?, ?, ?)"
                lista = [fecha, hora, form.coinsfrom.data, form.quantityfromH.data, form.coinsto.data, form.quantitytoH.data, form.puH.data]
                manager.recordMovements(consult, lista)
                if form.coinsfrom.data == 'EUR':
                    consult = "UPDATE saldo SET inversión = inversión + ?"
                    manager.recordMovements(consult, [form.quantityfromH.data])
                    consult = "UPDATE saldo SET {} = {} + ?".format(form.coinsto.data, form.coinsto.data)
                    manager.recordMovements(consult, [form.quantitytoH.data])
                elif form.coinsto.data == 'EUR':
                    consult = "UPDATE saldo SET inversión = inversión - ?"
                    manager.recordMovements(consult, [form.quantitytoH.data])
                    consult = "UPDATE saldo SET {} = {} - ?".format(form.coinsfrom.data, form.coinsfrom.data)
                    manager.recordMovements(consult, [form.quantityfromH.data])
                else:
                    consult = "UPDATE saldo SET {} = {} - ?".format(form.coinsfrom.data, form.coinsfrom.data)
                    manager.recordMovements(consult, [form.quantityfromH.data])
                    consult = "UPDATE saldo SET {} = {} + ?".format(form.coinsto.data, form.coinsto.data)
                    manager.recordMovements(consult, [form.quantitytoH.data])

                return redirect(url_for("movements"))
            else:
                flash("¡Debe de hacer el calculo antes de guardar el movimiento!")
                return render_template("exchanges.html", formulary=form)
        else:
            if form.quantityfrom.data == None:
                    flash("La cantidad origen debe ser de tipo numérico")
            elif form.quantityfrom.data <= 0:
                    flash("La cantidad debe ser un numero positivo mayor que 0")
            return render_template("exchanges.html", formulary=form) 

@app.route("/status")
def investment():
    consult = "SELECT * FROM saldo"
    try:
        dates = manager.consultation(consult)
    except:
        flash("Error de conexion a la base de datos")
        return render_template("status.html")
    cont = 0
    eur = "EUR"
    for i in range(len(dates)):
        for key in dates[i].keys():
            if key != "inversión" and dates[i][key] > 0:
                try:
                    cant = ConectApi.conecta(key, eur, api_key)
                    cont += (cant * dates[i][key])
                except:
                    flash("Error de conexión con la API")
                    return render_template("status.html")

    status = cont - dates[0]["inversión"]
    if status < 0:
        status *= -1
        BP = "Perdidas"
    elif status == 0:
        BP = ""
    else:
        BP = "Ganancias"            
    return render_template("status.html", inv = dates[0]["inversión"], result = status, B_P = BP)

@app.route("/saldo")
def saldo():
    consult = "SELECT * FROM saldo"
    saldo_list = manager.consultation(consult)
    return render_template('saldo.html', items=saldo_list)
    
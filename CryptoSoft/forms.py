from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import FloatField
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms import SelectField
from CryptoSoft.models import BBDDoperations
from . import app

class Form(FlaskForm):
                url_BBDates = app.config.get("BASE_DE_DATOS")
                manager = BBDDoperations(url_BBDates)
                coins = manager.consultation("SELECT * FROM saldo")
                lista = ["--Seleccione Criptomoneda--", "EUR"]
                for i in range(len(coins)):
                    for key in coins[i].keys():
                        if coins[i][key] > 0:
                            lista.append(key)
                coinsfrom = SelectField(u'Seleccione criptomoneda', choices = lista)
                coinsto = SelectField(u'Seleccione criptomoneda', choices=[('0', '--Seleccione criptomoneda--'), ('EUR', 'EUR'), ('ETH', 'ETH'), ('LTC', 'LTC'), ('BNB', 'BNB'), ('EOS', 'EOS'), ('XLM', 'XLM'), ('TRX', 'TRX'), ('BTC', 'BTC'), ('XRP', 'XRP'), ('BCH', 'BCH'), ('USDT', 'USDT'), ('BSV', 'BSV'), ('ADA', 'ADA')])
                quantityfrom = FloatField("Q: ", validators=[DataRequired(message="debe informar una cantidad"), NumberRange(message="debe informar una cantidad positiva", min=0.01)])
                quantityfromH = HiddenField()
                pu = FloatField("P.U.: ")
                puH = HiddenField()
                quantityto = FloatField("Q :")
                quantitytoH = HiddenField()
                submit = SubmitField('Aceptar')
                calculadora = SubmitField('Calculator')

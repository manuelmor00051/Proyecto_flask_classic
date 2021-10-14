from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import FloatField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms import SelectField



class Form(FlaskForm):
        coinsfrom = SelectField(u'Seleccione criptomoneda', choices=[('0', '--Seleccione criptomoneda--'), ('EUR', 'EUR'), ('ETH', 'ETH'), ('LTC', 'LTC'), ('BNB', 'BNB'), ('EOS', 'EOS'), ('XLM', 'XLM'), ('TRX', 'TRX'), ('BTC', 'BTC'), ('XRP', 'XRP'), ('BCH', 'BCH'), ('USDT', 'USDT'), ('BSV', 'BSV'), ('ADA', 'ADA')])
        coinsto = SelectField(u'Seleccione criptomoneda', choices=[('0', '--Seleccione criptomoneda--'), ('EUR', 'EUR'), ('ETH', 'ETH'), ('LTC', 'LTC'), ('BNB', 'BNB'), ('EOS', 'EOS'), ('XLM', 'XLM'), ('TRX', 'TRX'), ('BTC', 'BTC'), ('XRP', 'XRP'), ('BCH', 'BCH'), ('USDT', 'USDT'), ('BSV', 'BSV'), ('ADA', 'ADA')])
        quantityfrom = FloatField("Q: ", validators=[DataRequired(message="debe informar una cantidad"), NumberRange(message="debe informar una cantidad positiva", min=0.01)])
        pu = ""
        quantityto = ""
        submit = SubmitField('Aceptar')
        calculadora = SubmitField('Calculator')
        
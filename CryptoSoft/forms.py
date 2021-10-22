from flask_wtf import FlaskForm
from wtforms.fields.core import FloatField
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms import SelectField

class Form(FlaskForm):
    coinsfrom = SelectField(u'Seleccione criptomoneda', choices = [])
    coinsto = SelectField(u'Seleccione criptomoneda', choices=[('0', '--Seleccione criptomoneda--'), ('EUR', 'EUR'), ('ETH', 'ETH'), ('LTC', 'LTC'), ('BNB', 'BNB'), ('EOS', 'EOS'), ('XLM', 'XLM'), ('TRX', 'TRX'), ('BTC', 'BTC'), ('XRP', 'XRP'), ('BCH', 'BCH'), ('USDT', 'USDT'), ('BSV', 'BSV'), ('ADA', 'ADA')])
    quantityfrom = FloatField("Q: ", validators=[DataRequired(message="debe informar una cantidad"), NumberRange(message="debe informar una cantidad positiva", min=0.01)])
    quantityfromH = HiddenField()
    pu = FloatField("P.U.: ")
    puH = HiddenField()
    quantityto = FloatField("Q :")
    quantitytoH = HiddenField()
    submit = SubmitField('Aceptar')
    calculadora = SubmitField('Calcular')
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from riskLevel import RiskLevel
from trend import Trend
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_per_unit = db.Column(db.Integer)
    currency = db.Column(db.String)
    risk_level = db.Column(db.Enum(RiskLevel))
    trend = db.Column(db.Enum(Trend))
    duration = db.Column(db.Integer)
    emitent = db.Column(db.String)
    owner = db.Column(db.String)

    def __init__(self,
                 pricePerUnit=0, currency="$",
                 riskLevel=RiskLevel.LOW,
                 trend=Trend.UP, duration=0,
                 emitent="NoEmitent", owner="NoOwner"
                 ):
        self.price_per_unit = pricePerUnit
        self.currency = currency
        self.risk_level = riskLevel
        self.trend = trend
        self.duration = duration
        self.emitent = emitent
        self.owner = owner


class SecuritySchema(ma.Schema):
    class Meta:
        fields = ('price_per_unit', 'currency', 'risk_level', 'trend', 'duration', 'emitent', 'owner')


security_schema = SecuritySchema()
securities_schema = SecuritySchema(many=True)


@app.route("/security", methods=["POST"])
def add_security():
    price_per_unit = request.json['price_per_unit']
    currency = request.json['currency']
    risk_level = request.json['risk_level']
    trend = request.json['trend']
    duration = request.json['duration']
    emitent = request.json['emitent']
    owner = request.json['owner']

    new_security = Security(price_per_unit, currency, risk_level, trend, duration, emitent, owner)

    db.session.add(new_security)
    db.session.commit()

    return security_schema.jsonify(new_security)


@app.route("/security", methods=["GET"])
def get_all_securities():
    all_securities = Security.query.all()
    return securities_schema.jsonify(all_securities)


@app.route("/security/<id>", methods=["GET"])
def get_security(id):
    security = Security.query.get(id)
    return security_schema.jsonify(security)


@app.route("/security/<id>", methods=["PUT"])
def update_security(id):
    security = Security.query.get(id)

    price_per_unit = request.json['price_per_unit']
    currency = request.json['currency']
    risk_level = request.json['risk_level']
    trend = request.json['trend']
    duration = request.json['duration']
    emitent = request.json['emitent']
    owner = request.json['owner']

    security.price_per_unit = price_per_unit
    security.currency = currency
    security.risk_level = risk_level
    security.trend = trend
    security.duration = duration
    security.emitent = emitent
    security.owner = owner

    db.session.commit()
    return security_schema.jsonify(security)


@app.route("/security/<id>", methods=["DELETE"])
def delete_security(id):
    security = Security.query.get(id)
    db.session.delete(security)
    db.session.commit()

    return security_schema.jsonify(security)


if __name__ == '__main__':
    app.run(debug=True)
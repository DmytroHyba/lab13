from riskLevel import RiskLevel
from trend import Trend


class Security:

    def __init__(self,
                 pricePerUnit=0, currency="$",
                 riskLevel=RiskLevel.LOW,
                 trend=Trend.UP, duration=0,
                 emitent="NoEmitent", owner="NoOwner"
                 ):
        self.pricePerUnit = pricePerUnit
        self.currency = currency
        self.riskLevel = riskLevel
        self.trend = trend
        self.duration = duration
        self.emitent = emitent
        self.owner = owner

    def __str__(self):
        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))
from riskLevel import RiskLevel
from security import Security
from trend import Trend

class Equity(Security):
    def __init__(self,
                 pricePerUnit=0, currency="$",
                 riskLevel=RiskLevel.LOW,
                 trend=Trend.UP, duration=0,
                 emitent="NoEmitent", owner="NoOwner",
                 company="NoCompany", percentOfCompany=0
                 ):
        super(Equity, self).__init__(
            pricePerUnit, currency, riskLevel,
            trend, duration, emitent, owner
        )
        self.company = company
        self.percentOfCompany = percentOfCompany
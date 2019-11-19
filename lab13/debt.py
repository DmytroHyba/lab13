from riskLevel import RiskLevel
from security import Security
from trend import Trend


class Debt(Security):

    def __init__(self,
                 pricePerUnit=0, currency="$",
                 riskLevel=RiskLevel.LOW,
                 trend=Trend.UP, duration=0,
                 emitent="NoEmitent", owner="NoOwner",
                 asset="NoAsset", security=Security()
                 ):
        super(Debt, self).__init__(
            pricePerUnit, currency, riskLevel,
            trend, duration, emitent, owner
        )
        self.asset = asset
        self.security = Security
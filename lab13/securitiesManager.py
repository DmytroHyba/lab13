import sys
sys.path.insert(0, '../models')
from debt import Debt
from derivative import Derivative
from equity import Equity
from security import Security
from riskLevel import RiskLevel
from trend import Trend


class SecuritiesManager:
    def __init__(self, *args):
        self.securities = args

    @staticmethod
    def sortByPrice(securities, descending=False):
        return sorted(securities, key=lambda security: security.pricePerUnit, reverse=descending)

    @classmethod
    def sortByPriceAscending(cls,securities):
        return cls.sortByPrice(securities)

    @classmethod
    def sortByPriceDescending(cls,securities):
        return cls.sortByPrice(securities, True)

    @staticmethod
    def sortByDuration(securities, descending=False):
        return sorted(securities, key=lambda security: security.duration, reverse=descending)

    @classmethod
    def sortByDurationAscending(cls,securities):
        return cls.sortByDuration(securities)

    @classmethod
    def sortByDurationDescending(cls,securities):
        return cls.sortByDuration(securities, True)

    # return [security for security in self.securities if security.pricePerUnit == price]

    def filterByPrice(self, price):
        return list(filter(lambda security: security.pricePerUnit == price, self.securities))

    def filterByRiskLevel(self, riskLevel):
        return list(filter(lambda security: security.riskLevel == riskLevel, self.securities))

    def filterByTrend(self, trend):
        return list(filter(lambda security: security.trend == trend, self.securities))


def main():
    securities = [
        Security(30, "$", RiskLevel.LOW, Trend.UP, 0, "Ukraine", "I"),
        Equity(20, "$", RiskLevel.MEDIUM, Trend.DOWN, 0, "Russia", "I", "Roshen", 0.5),
        Debt(10, "$", RiskLevel.HIGH, Trend.UP, 0, "Belarus", "I"),
        Derivative(0, "$", RiskLevel.DANGER, Trend.UP, 0, "Moldova", "I", "house"),
        Security(0, "$", RiskLevel.LOW, Trend.DOWN, 10, "Ukraine", "I")
    ]
    manager = SecuritiesManager(*securities)

    filteredList = manager.filterByPrice(0)
    for s in filteredList:
        print(s)
    print()

    sortedList = SecuritiesManager.sortByPriceAscending(securities)
    for s in sortedList:
        print(s)
    print()

    sortedFilteredList = SecuritiesManager.sortByDurationDescending(filteredList)
    for s in sortedFilteredList:
        print(s)


if __name__ == '__main__':
    main()
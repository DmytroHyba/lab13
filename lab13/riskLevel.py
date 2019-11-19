from enum import Enum


class RiskLevel(str, Enum):
    LOW : str = 'LOW'
    MEDIUM : str = 'MEDIUM'
    HIGH : str = 'HIGH'
    DANGER : str = 'DANGER'
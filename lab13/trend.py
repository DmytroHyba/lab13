from enum import Enum


class Trend(str, Enum):
    DOWN : str = "DOWN"
    UP : str = "UP"
from enum import Enum

class StoneType(Enum):
    """
    定義符石的類型，使用枚舉類別來管理所有可能的符石類型。
    """
    CAR = "car"           # 汽車符石
    BUS = "bus"           # 公車符石
    BIKE = "bike"         # 自行車符石
    SCOOTER = "scooter"   # 機車符石
    TRAIN = "train"       # 火車符石


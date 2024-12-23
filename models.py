class Runestone:
    """
    定義遊戲中的符石物件，每個符石有其類型和狀態。
    """
    def __init__(self, _type, _status=""):
        """
        初始化符石的屬性。
        :param _type: 符石的類型（例如汽車、自行車等）
        :param _status: 符石的狀態（預設為空字串）
        """
        self.type = _type  # 符石的類型，使用 StoneType 枚舉
        self.status = _status  # 符石的狀態，例如是否被選中或拖曳

    def __repr__(self):
        """
        定義符石在調試模式下的字串表示。
        :return: 格式化後的符石資訊
        """
        return f"{self.type.value}({self.status})"


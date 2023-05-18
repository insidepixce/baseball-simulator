import json
class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return obj.__dict__  # Player 객체의 속성을 딕셔너리로 반환
        return super().default(obj)
    def convert_to_dict(obj):
        if isinstance(obj, Player):
            return obj.__dict__
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")






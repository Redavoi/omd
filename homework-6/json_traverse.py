from keyword import iskeyword


class JSONTraverse:
    def __init__(self, data):
        for key, value in data.items():
            if key == "price" and value < 0:
                raise ValueError("price must be >= 0")
            if isinstance(value, dict):
                value = JSONTraverse(value)
            if iskeyword(key):
                key += "_"
            setattr(self, key, value)

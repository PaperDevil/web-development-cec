from datetime import datetime

class TodoItem:
    id = 0
    text = ""
    datetime = ""
    is_complete = False
    is_delte = False
    # owner = User()

    def __init__(self, text, index, is_complete):
        self.id = index
        self.text = text
        self.datetime = datetime.now()
        self.is_complete = is_complete

    def serialize(self):
        return {
            "text": self.text,
            "datetime": self.datetime,
            "is_complete": self.is_complete
        }
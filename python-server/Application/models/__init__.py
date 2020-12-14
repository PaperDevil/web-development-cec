from datetime import datetime

class TodoItem:
    id = 0
    text = ""
    datetime = ""
    # owner = User()

    def __init__(self, text, index):
        self.id = index
        self.text = text
        self.datetime = datetime.now()

    def serialize(self):
        return {
            "text": self.text,
            "datetime": self.datetime
        }
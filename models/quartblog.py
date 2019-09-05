import datetime 

from app.database import DB  

class Post(object):

    def __init__(self, title, text):
        self.title = title 
        self.text = text 
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        if not DB.find_one("posts", {"title": self.title, "text":self.text}):
            DB.insert(collection='posts', data=self.json())

    def json(self):
        return { 
            'title': self.title,
            'text': self.text,
            'created_at': self.created_at
        }

    

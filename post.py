import uuid
import datetime

from database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.id = uuid.uuid4().hex if id is None else id
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection = 'posts', data = self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'title':self.title,
            'content':self.content,
            'author':self.author,
            'created_date':self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        posts = Database.find_one(collection='posts', query={'id': id})

        return cls(blog_id=posts['blog_id'],
                   title=posts['title'],
                   content=posts['content'],
                   author=posts['author'],
                   date=posts['created_date'])


    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]


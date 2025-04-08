from src.fields import IntegerField, StringField
from src.query import Query
class BaseModel:
    def save(self):
        pass

    def delete(self):
        pass

    @classmethod
    def query(cls):
        return Query(cls)

class User(BaseModel):
    id = IntegerField()
    username = StringField(max_length=50)
    email = StringField(max_length=100)

class Post(BaseModel):
    id = IntegerField()
    title = StringField(max_length=200)
    content = StringField(max_length=500)
    author_id = IntegerField()  # Foreign key to User model

    @classmethod
    def get_author(cls):
        return User.query().filter(User.id == cls.author_id)
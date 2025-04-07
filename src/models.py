class BaseModel:
    def save(self):
        pass

    def delete(self):
        pass

    @classmethod
    def query(cls):
        return Query(cls)

class User(BaseModel):
    id = IntegerField(primary_key=True)
    username = StringField()
    email = StringField()

class Post(BaseModel):
    id = IntegerField(primary_key=True)
    title = StringField()
    content = StringField()
    author_id = IntegerField()  # Foreign key to User model

    @classmethod
    def get_author(cls):
        return User.query().filter(User.id == cls.author_id)
from src.fields import IntegerField, StringField
from src.query import Query
from src.utils import connect_to_database
class BaseModel:
    
    def __init__(self, **kwargs):
        """
        Initialize the model instance with field values.
        """
        for field_name, field in self.__class__.__dict__.items():
            if isinstance(field, (IntegerField, StringField)):
                setattr(self, field_name, kwargs.get(field_name, None))
    _connection = connect_to_database("database.db") 
    @classmethod
    def create_table(cls):
        """
        Create a table for the model in the database.
        """
        fields = []
        for field_name, field in cls.__dict__.items():
            if isinstance(field, (IntegerField, StringField)):
                column = f"{field_name} {field.field_type}"
                if field.primary_key:
                    column += " PRIMARY KEY"
                fields.append(column)
        fields_sql = ", ".join(fields)
        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} ({fields_sql});"
        with cls._connection:
            cls._connection.execute(query)
    def save(self):
        fields = []
        values = []
        for field_name, field in self.__class__.__dict__.items():
            if isinstance(field, (IntegerField, StringField)):
                fields.append(field_name)
                values.append(getattr(self, field_name, None))
        fields_sql = ", ".join(fields)
        placeholders = ", ".join(["?"] * len(values))
        query = f"INSERT INTO {self.__class__.__name__.lower()} ({fields_sql}) VALUES ({placeholders});"
        try:
            with self._connection:
                self._connection.execute(query, values)
        except Exception as e:
            raise ValueError(f"Failed to save {self.__class__.__name__} instance: {e}")

    def delete(self):
        pass

    @classmethod
    def query(cls):
        return Query(cls)

class User(BaseModel):
    id = IntegerField(primary_key=True)
    username = StringField(max_length=50)
    email = StringField(max_length=100)

class Post(BaseModel):
    id = IntegerField(primary_key=True)
    title = StringField(max_length=200)
    content = StringField(max_length=500)
    author_id = IntegerField()  # Foreign key to User model

    def get_author(self):
        return User.query().filter(id=self.author_id).first()
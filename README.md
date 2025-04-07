# Custom ORM Framework

This project is a lightweight Object-Relational Mapping (ORM) framework designed to provide an easy-to-use interface for interacting with databases. It is built to help you understand metaprogramming and design patterns in Python.

## Features

- **Base Model**: A base class for all ORM models that provides methods for saving, deleting, and querying instances.
- **Field Types**: Various field types such as `StringField`, `IntegerField`, and `DateField` with built-in validation.
- **Querying**: A flexible query interface to filter and retrieve data from the database.
- **Utility Functions**: Helper functions for connection management, data serialization, and logging.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. **Define Models**: Create your models by inheriting from `BaseModel` and defining fields using the provided field types.

   ```python
   from src.models import BaseModel, StringField, IntegerField

   class User(BaseModel):
       username = StringField()
       age = IntegerField()
   ```

2. **Create and Save Instances**: Create instances of your models and save them to the database.

   ```python
   user = User(username='john_doe', age=30)
   user.save()
   ```

3. **Querying**: Use the query interface to retrieve data.

   ```python
   users = User.query.filter(User.age > 25).all()
   ```

## Running Tests

To run the tests, use the following command:

```
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
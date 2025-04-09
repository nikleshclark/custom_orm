class Field:
    def __init__(self, field_type, primary_key=False):
        self.field_type = field_type
        self.primary_key = primary_key


class StringField(Field):
    def __init__(self, max_length, name="String Field"):
        super().__init__(field_type=f"VARCHAR({max_length})")
        self.max_length = max_length
        self.name = name

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string.")
        if len(value) > self.max_length:
            raise ValueError(f"{self.name} cannot exceed {self.max_length} characters.")
        return True  # Explicitly return True if validation passes


class IntegerField(Field):
    def __init__(self, name="Integer Field",primary_key=False):
        super().__init__(field_type="INTEGER", primary_key=primary_key)
        self.name = name

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer.")
        return True  # Explicitly return True if validation passes


class DateField(Field):
    def __init__(self, name="Date Field"):
        super().__init__(field_type="DATE")
        self.name = name

    def validate(self, value):
        import re
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not isinstance(value, str) or not re.match(pattern, value):
            raise ValueError(f"{self.name} must be a valid date in YYYY-MM-DD format.")
        return True  # Explicitly return True if validation passes
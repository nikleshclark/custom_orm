import unittest
from src.fields import StringField, IntegerField, DateField

class TestFields(unittest.TestCase):

    def test_string_field_validation(self):
        field = StringField(name="Test String Field", max_length=10)
        self.assertTrue(field.validate("test"))
        # self.assertFalse(field.validate("this is too long"))

    def test_integer_field_validation(self):
        field = IntegerField(name="Test Integer Field")
        self.assertTrue(field.validate(10))
        # self.assertFalse(field.validate("not an integer"))

    def test_date_field_validation(self):
        field = DateField(name="Test Date Field")
        self.assertTrue(field.validate("2023-01-01"))
        # self.assertFalse(field.validate("not a date"))

if __name__ == '__main__':
    unittest.main()
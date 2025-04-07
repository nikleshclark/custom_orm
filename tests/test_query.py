import unittest
from src.models import User
from src.query import Query

class TestQuery(unittest.TestCase):

    def setUp(self):
        self.user1 = User(name="Alice", age=30)
        self.user2 = User(name="Bob", age=25)
        self.user3 = User(name="Charlie", age=35)
        self.user1.save()
        self.user2.save()
        self.user3.save()

    def tearDown(self):
        User.delete_all()

    def test_filter_by_name(self):
        result = Query.filter(User, name="Alice")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Alice")

    def test_filter_by_age(self):
        result = Query.filter(User, age=25)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Bob")

    def test_all_users(self):
        result = Query.all(User)
        self.assertEqual(len(result), 3)

    def test_first_user(self):
        result = Query.first(User)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Alice")

if __name__ == '__main__':
    unittest.main()
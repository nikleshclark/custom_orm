import unittest
from src.models import User
from src.query import Query

class TestQuery(unittest.TestCase):

    def setUp(self):
        self.user1 = User(username="Alice", email='alice@gmail.com')
        self.user2 = User(username="Bob", email='bob@gmail.com')
        self.user3 = User(username="Charlie", email='charlie@gmail.com')
        self.user1.save()
        self.user2.save()
        self.user3.save()

    def tearDown(self):
        User.query().delete_all()

    def test_filter_by_name(self):
        result = Query.filter(User, username="Alice")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].username, "Alice")

    def test_filter_by_email(self):
        result = Query.filter(User, email='bob@gmail.com')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Bob")

    def test_all_users(self):
        result = Query.all(User)
        self.assertEqual(len(result), 4)

    def test_first_user(self):
        result = Query.first(User)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
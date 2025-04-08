import unittest
from src.fields import StringField, IntegerField
from src.models import User, Post


class TestModels(unittest.TestCase):

    def test_user_model_fields(self):
        # Check if the User model has the correct fields
        self.assertIsInstance(User.id, IntegerField)
        self.assertIsInstance(User.username, StringField)
        self.assertIsInstance(User.email, StringField)

    def test_post_model_fields(self):
        # Check if the Post model has the correct fields
        self.assertIsInstance(Post.id, IntegerField)
        self.assertIsInstance(Post.title, StringField)
        self.assertIsInstance(Post.content, StringField)
        self.assertIsInstance(Post.author_id, IntegerField)

    # def test_user_save(self):
    #     # Simulate saving a User instance
    #     user = User(id=1, username="john_doe", email="john@example.com")
    #     try:
    #         user.save()
    #     except Exception as e:
    #         self.fail(f"User.save() raised an exception: {e}")

    # def test_post_save(self):
    #     # Simulate saving a Post instance
    #     post = Post(id=1, title="Test Post", content="This is a test post.", author_id=1)
    #     try:
    #         post.save()
    #     except Exception as e:
    #         self.fail(f"Post.save() raised an exception: {e}")

    # def test_post_get_author(self):
    #     # Simulate getting the author of a Post
    #     post = Post(id=1, title="Test Post", content="This is a test post.", author_id=1)
    #     try:
    #         author = post.get_author()
    #         # Assuming get_author() returns a User instance or None
    #         self.assertIsNotNone(author)
    #     except Exception as e:
    #         self.fail(f"Post.get_author() raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
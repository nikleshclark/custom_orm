from src.models import User, Post

def test_user_creation():
    user = User(username='testuser', email='test@example.com')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'

def test_post_creation():
    user = User(username='testuser', email='test@example.com')
    post = Post(title='Test Post', content='This is a test post.', author=user)
    assert post.title == 'Test Post'
    assert post.content == 'This is a test post.'
    assert post.author == user

def test_user_save():
    user = User(username='testuser', email='test@example.com')
    user.save()
    assert user.id is not None  # Assuming save assigns an ID

def test_post_save():
    user = User(username='testuser', email='test@example.com')
    user.save()
    post = Post(title='Test Post', content='This is a test post.', author=user)
    post.save()
    assert post.id is not None  # Assuming save assigns an ID

def test_user_query():
    user = User(username='testuser', email='test@example.com')
    user.save()
    queried_user = User.query().filter(username='testuser').first()
    assert queried_user is not None
    assert queried_user.username == 'testuser'

def test_post_query():
    user = User(username='testuser', email='test@example.com')
    user.save()
    post = Post(title='Test Post', content='This is a test post.', author=user)
    post.save()
    queried_post = Post.query().filter(title='Test Post').first()
    assert queried_post is not None
    assert queried_post.title == 'Test Post'
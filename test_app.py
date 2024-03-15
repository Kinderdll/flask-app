import unittest
from main import app, db
from models import User

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()


    def test_create_user_route(self):
        tester = app.test_client(self)
        response = tester.post('/create_user', data=dict(username="test4", email="test4@gmail.com"))
        self.assertEqual(response.status_code, 302)

    def test_users_route(self):
        tester = app.test_client(self)
        response = tester.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List of Users', response.data)

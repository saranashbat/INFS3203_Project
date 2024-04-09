import unittest
from app import app, users, save_users, User
from flask_login import login_user, logout_user
from flask import session

class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  

    def test_login_page_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_SignUp_page_route(self):  
        response = self.app.get('/SignUp')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'QCareers', response.data)

    def test_infotechjobs_route(self):
        response = self.app.get('/infotechjobs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Information Technology', response.data)

    def test_infotechjob1_route(self):
        response = self.app.get('/infotechjob1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cybersecurity', response.data)

    def test_login_functionality(self):
        with self.app as client:
            response = client.post('/login', data=dict(username='user1', password='hello123'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'QCareers', response.data)  

            response = client.post('/login', data=dict(username='user1', password='wrongpassword'), follow_redirects=True)
            self.assertIn(b'Invalid username or password', response.data)

    def test_logout_functionality(self):
        with app.test_request_context('/'):
            with self.app as client:
                login_user(users['user1'])
                response = client.get('/logout', follow_redirects=True)
                self.assertNotIn(b'user1', response.data)


    def test_signup_functionality(self):
        with self.app as client:
            response = client.post('/SignUp', data=dict(username='newuser', password='password', email='newuser@example.com', fullname='New User'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'QCareers', response.data) 

            response = client.post('/SignUp', data=dict(username='user1', password='hello123', email='test@example.com', fullname='Test User'), follow_redirects=True)
            self.assertIn(b'Username already exists', response.data)

    def test_session_management(self):
        with self.app as client:
            response = client.get('/infotechjobs', follow_redirects=False)
            self.assertEqual(response.status_code, 302)  

            user = users['user1']
            login_user(user)
            with client.session_transaction() as sess:
                sess['_user_id'] = user.get_id()
            response = client.get('/infotechjobs', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

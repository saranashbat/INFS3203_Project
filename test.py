import unittest
from app import app
from flask_login import login_user

class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_login_page_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login - Security Solutions LLC', response.data)

    def test_SignUp_page_route(self):  
        response = self.app.get('/SignUp')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up - Security Solutions LLC', response.data)

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

    def test_profile_route_authenticated(self):
        # Simulate a logged-in user session
        with self.app as c:
            with c.session_transaction() as sess:
                sess['_user_id'] = 'example_user'  # Simulate the user ID in the session
        # Access the profile route
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Profile', response.data)

if __name__ == '__main__':
    unittest.main()

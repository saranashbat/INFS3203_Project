import unittest
from app import app


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
        self.assertIn(b'Information', response.data)

    def test_infotechjob1_route(self):
        response = self.app.get('/infotechjob1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cybersecurity', response.data)


if __name__ == '__main__':
    unittest.main()

import unittest
import json
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test if the home page loads the HTML
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask API Test', response.data)

    def test_api_status(self):
        # Test the JSON API endpoint
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('Python Flask backend is running', data['message'])

if __name__ == '__main__':
    unittest.main()

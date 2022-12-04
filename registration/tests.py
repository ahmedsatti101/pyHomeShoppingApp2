from django.test import TestCase

from django.test import SimpleTestCase

class poll_page_Tests(SimpleTestCase):
    
    def test_registration_page_response_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertEqual(response.status_code, 200)
        
    def test_registration_page_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Registartion form')
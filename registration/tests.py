from django.test import TestCase

from django.test import SimpleTestCase

class poll_page_Tests(SimpleTestCase):
    
    def test_registration_page_response_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertEqual(response.status_code, 200)
        
    def test_registration_page_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Registartion form')
        
    def test_first_name_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'First name')
        
    def test_last_name_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Last name')
        
    def test_email_address_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Email address')
        
    def test_confirm_email_address_text(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Confirm email address')
        
    def test_phone_number_exists(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Phone number')
        
    def test_create_password_exists(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Create password')
        
    def test_retype_password_exists(self):
        response = self.client.get('http://127.0.0.1:8000/registration/')
        self.assertContains(response, 'Retype password')
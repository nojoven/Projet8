from django.test import TestCase


class SimpleTest(TestCase):

    URI_r_BASE = "http://localhost:8000/roles/"
    provided_mail = "ezzou@gmail.com"
    provided_password = "ezzou"
    signin_request = f"{URI_r_BASE}signin/"
    favourites_request = f"{URI_r_BASE}favourites/"
    account_request = f"{URI_r_BASE}account/"

    def test_views_signin(self):
        response = self.client.get(self.signin_request)
        assert response.status_code == 200

    def test_views_favourites(self):
        response =  self.client.get(self.favourites_request)
        assert response.status_code == 200

    def test_views_account(self):
        response = self.client.get(self.account_request)
        assert response.status_code == 200

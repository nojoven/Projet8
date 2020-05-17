from django.test import TestCase


class SimpleTest(TestCase):
    URI_f_BASE = "http://localhost:8000/foodfacts/"
    home_request = URI_f_BASE
    aliment_request = f"{URI_f_BASE}aliment/1/"
    notice_request = f"{URI_f_BASE}notice/"
    resultats_gazpacho = f"{URI_f_BASE}resultats/Gazpacho/"
    resultats_empty = f"{URI_f_BASE}resultats/empty/"
    favourites_request = f"{URI_f_BASE}favourites/"
    account_request = f"{URI_f_BASE}account/"


    def test_views_home(self):
        response = self.client.get(self.home_request)
        self.assertEqual(response.status_code, 200)

    def test_views_aliment(self):
        response = self.client.get(self.aliment_request)
        self.assertEqual(response.status_code, 200)

    def test_views_resultats_gazpacho(self):
        response = self.client.get(self.resultats_gazpacho)
        self.assertEqual(response.status_code, 200)

    def test_views_resultats_empty(self):
        response = self.client.get(self.resultats_empty)
        self.assertEqual(response.status_code, 200)

    def test_views_notice(self):
        response = self.client.get(self.notice_request)
        self.assertEqual(response.status_code, 200)


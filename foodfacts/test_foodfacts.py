"""This file contains the unitary tests of foodfacts"""
from django.test import TestCase
from PurBeurre.constants import PRODUCT_EXAMPLE
from foodfacts.models import Products
from foodfacts.modules.database_service import DatabaseService


class SimpleTest(TestCase):
    """
    Here we define attributes and functions to test
    the views responses and functions.
    """
    URI_f_BASE = "https://beurrepur.herokuapp.com/foodfacts/"
    home_request = URI_f_BASE
    aliment_request = f"{URI_f_BASE}aliment/1/"
    notice_request = f"{URI_f_BASE}notice/"
    resultats_gazpacho = f"{URI_f_BASE}resultats/Gazpacho/"
    resultats_empty = f"{URI_f_BASE}resultats/empty/"
    account_request = f"{URI_f_BASE}account/"

    def test_views_home(self):
        """Tests the HTTP response"""
        response = self.client.get(self.home_request)
        self.assertEqual(response.status_code, 200)

    def test_views_aliment(self):
        """Tests the HTTP response"""
        response = self.client.get(self.aliment_request)
        self.assertEqual(response.status_code, 200)

    def test_views_resultats_gazpacho(self):
        """Tests the HTTP response"""
        response = self.client.get(self.resultats_gazpacho)
        self.assertEqual(response.status_code, 200)

        self.client.post("/foodfacts/research", {'nav_search': 'Gazpacho'})
        self.assertEqual(response.status_code, 200)


    def test_views_resultats_empty(self):
        """Tests the HTTP response"""
        response = self.client.get(self.resultats_empty)
        self.assertEqual(response.status_code, 200)

    def test_views_notice(self):
        """Tests the HTTP response"""
        response = self.client.get(self.notice_request)
        self.assertEqual(response.status_code, 200)

    def test_select_better_products(self):
        """Tests the the database request for better products"""
        selection = DatabaseService.select_better_products("soup", -4)
        assert selection is not None

    def test_search_product(self):
        """Tests the retrieving of the wanted product"""
        product = PRODUCT_EXAMPLE
        query = Products(**product)
        query.save()
        searched = DatabaseService.select_product("Gazpacho")
        assert searched is not None

    def test_show_details(self):
        """Tests the requesting of a specific product"""
        product = {
            "category": "soup",
            "stores": "Auchan",
            "brands": "Reflets",
            "productname": "Gazpacho",
            "nutrigrade": "a",
            "quantity": "1L",
            "front_img": "img.jpg",
            "nutrition_img": "img.png",
            "ingredients_img": "img.svg",
            "fat_100g": 0.20,
            "sugars_100g": 3.20,
            "saturated_fat_100g": 0.20,
            "energy_kcal_100g": 250.16,
            "nutrition_Score_100g": -4,
            "fiber_100g": 24.14,
            "salt_100g": 1.03,
            "proteins_100g": 5.63,
            "carbs_100g": 3.20,
            "sodium_100g": 1.03,
            "url": "www.url.com",
        }
        query = Products(**product)
        query.save()
        article = DatabaseService.select_product("Gazpacho")
        selected = DatabaseService.show_details(article.idproduct)
        assert selected is not None


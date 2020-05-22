from django.test import TestCase

from foodfacts.models import Products
from foodfacts.modules.database_service import DatabaseService


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

    def test_select_better_products(self):
        selection = DatabaseService.select_better_products("soup", -4)
        assert selection is not None

    def test_search_product(self):
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
        searched = DatabaseService.select_product("Gazpacho")
        assert searched is not None

    def test_show_details(self):
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

import pytest
from django.contrib.auth import authenticate
from django.test import TestCase
from foodfacts.models import Favorites, Products
from foodfacts.modules.database_service import DatabaseService


class SimpleTest(TestCase):

    URI_r_BASE = "http://localhost:8000/roles/"
    provided_mail = "dubosc@gmail.com"
    provided_password = "Franck"
    signin_request = f"{URI_r_BASE}signin/"
    favourites_request = f"{URI_r_BASE}favourites/"
    account_request = f"{URI_r_BASE}account/"
    register_request = f"{URI_r_BASE}register/"

    def test_views_signin(self):
        response = self.client.get(self.signin_request)
        assert response.status_code == 200

    def test_views_favourites(self):
        response = self.client.get(self.favourites_request)
        assert response.status_code == 200

    def test_views_account(self):
        response = self.client.get(self.account_request)
        assert response.status_code == 200

    def test_views_register(self):
        response = self.client.get(self.register_request)
        assert response.status_code == 200


@pytest.mark.django_db
class TestRoles:
    """Pytest will be used to verify the behaviour of the following functions"""
    provided_mail = "dubosc@gmail.com"
    provided_password = "Franck"

    def test_create_product(self):
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
            "url": "www.url.com"
        }
        query = Products(**product)
        query.save()
        article = DatabaseService.select_product("Gazpacho")
        assert article.productname == "Gazpacho"

    def test_create_update_user_data(self,
                                     provided_username="username1",
                                     provided_mail="user@gmail.com",
                                     provided_password="test1234",
                                     update_email="update@test.com",
                                     update_first_name="Pierre",
                                     update_last_name="Dupuis"):

        DatabaseService.create_user(provided_username, provided_password, provided_mail, "User", "TESTNAME")

        user = authenticate(username=provided_mail, password=provided_password)
        assert user is not None

        email_before = user.email
        assert email_before is not None

        first_name_before = user.first_name
        assert first_name_before is not None

        last_name_before = user.last_name
        assert last_name_before is not None

        try:
            if update_email != "" and update_email != email_before:
                user.email = update_email
                assert user.email != email_before
            if update_first_name != "" and update_first_name != first_name_before:
                user.first_name = update_first_name
                assert user.first_name != first_name_before
            if update_last_name != "" and update_last_name != last_name_before:
                user.last_name = update_last_name
                assert user.last_name != last_name_before
            user.save()

            user = authenticate(username=update_email, password=provided_password)
            assert user is not None
            assert user.email != email_before
            assert user.first_name != first_name_before
            assert user.last_name != last_name_before

            user.email = email_before
            user.first_name = first_name_before
            user.last_name = last_name_before
            user.save()
            assert user.email == email_before
            assert user.first_name == first_name_before
            assert user.last_name == last_name_before

        except KeyError:
            return KeyError("CANNOT UPDATE A USER WHO DOES NOT EXISTS")

    def test_find_user_category_favourites(self):
        favourites = DatabaseService.sort_favourites(4, "soup")
        assert favourites is not None

    def test_find_favorite_in_products(self):
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
            "url": "www.url.com"
        }
        query = Products(**product)
        query.save()
        product = DatabaseService.select_product("Gazpacho")
        product_id = product.idproduct

        like_data = dict()
        like_data["productid"] = product_id
        like_data["name"] = product.productname
        like_data["nutrigrade"] = product.nutrigrade
        like_data["stores"] = product.stores
        like_data["brands"] = product.brands
        like_data["category"] = product.category
        like_data["quantity"] = product.quantity
        like_data["replacedid"] = product_id
        like_data["replacedarticle"] = product.productname
        like_data["replacednutrigrade"] = product.nutrigrade
        like_data["userid"] = 4
        like_data["front_img"] = "https://static.openfoodfacts.org/images/products/301/136/002/3995/front_fr.39.400.jpg"

        if not Favorites.objects.filter(productid=like_data["productid"]).exists():
            query = Favorites(**like_data)
            query.save()

        article = DatabaseService.select_liked_in_products(product_id)
        assert article is not None

    def test_get_all_user_favs(self):
        like_data = dict()
        like_data["productid"] = 22
        like_data["name"] = "Gazpacho Vert"
        like_data["nutrigrade"] = "a"
        like_data["stores"] = "'auchan', 'magasins-u'"
        like_data["brands"] = "Innocent"
        like_data["category"] = "soup"
        like_data["quantity"] = "84 g"
        like_data["replacedid"] = 1
        like_data["replacedarticle"] = "Gazpacho"
        like_data["replacednutrigrade"] = "a"
        like_data["userid"] = 4
        like_data["front_img"] = "https://static.openfoodfacts.org/images/products/301/136/002/3995/front_fr.39.400.jpg"

        if not Favorites.objects.filter(productid=like_data["productid"]).exists():
            query = Favorites(**like_data)
            query.save()
        user_favs = DatabaseService.select_user_favs(4)
        assert user_favs is not None
        assert len(user_favs) > 0

    def test_create_remove_fav(self):

        like_data = dict()
        like_data["productid"] = 44
        like_data["name"] = "Gazpacho Vert"
        like_data["nutrigrade"] = "a"
        like_data["stores"] = "'auchan', 'magasins-u'"
        like_data["brands"] = "Innocent"
        like_data["category"] = "soup"
        like_data["quantity"] = "84 g"
        like_data["replacedid"] = 1
        like_data["replacedarticle"] = "Gazpacho"
        like_data["replacednutrigrade"] = "a"
        like_data["userid"] = 4
        like_data["front_img"] = "https://static.openfoodfacts.org/images/products/301/136/002/3995/front_fr.39.400.jpg"

        if not Favorites.objects.filter(productid=44).exists():
            query = Favorites(**like_data)
            query.save()
            user_favs = DatabaseService.select_user_favs(4)
            assert user_favs is not None

        item = Favorites.objects.filter(productid=44, userid=4)

        item.delete()
        assert len(Favorites.objects.filter(productid=44, userid=4)) == 0

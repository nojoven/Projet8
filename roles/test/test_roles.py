"""
This is the file used to test the functions
that are specific to a user account
"""
import pytest
import logging
from django.test import TestCase, Client
# from PurBeurre.constants import PRODUCT_EXAMPLE
# from foodfacts.models import Favorites, Products
# from roles import views as rviews


@pytest.mark.django_db
class TestRoles(TestCase):
    """Pytest will be used to verify the behaviour of
     the following functions"""
    URI_r_BASE = "http://localhost:8000/roles/"
    logout_request = f"{URI_r_BASE}logout/"
    favourites_request = f"{URI_r_BASE}favourites/"
    account_request = f"{URI_r_BASE}account/"
    register_request = f"{URI_r_BASE}register/"
    signin_request = f"{URI_r_BASE}signin/"

    c = Client()
    LOGGER = logging.getLogger(__name__)

    def test_views_register(self):
        """Reach the register page"""
        response = self.client.get(self.register_request)
        assert response.status_code == 200

    def test_create_login_update_user_data(
            self,
            username="username1",
            email="user@gmail.com",
            password1="test1234$",
            password2="test1234$",
            first_name="Pierre",
            last_name="Dupuis",
    ):

        """Reach the register page"""
        response = self.client.get(self.register_request)
        assert response.status_code == 200

        response = \
            self.client.post("/roles/create",
                             {
                                 username: username,
                                 email: email,
                                 password1: password1,
                                 password2: password2,
                                 first_name: first_name,
                                 last_name: last_name
                             })
        assert response.status_code == 200

        """ logout page"""
        response = self.client.get(self.logout_request)
        assert response.status_code == 302

        """Reach the favourites page"""
        response = self.client.get(self.favourites_request)
        assert response.status_code == 200

        """Reach the account page"""
        # response = self.client.get(self.account_request)
        # assert response.status_code == 200
        """
        new_email = "charlie@choco.org"
        new_first_name = "Marcel"
        new_last_name = "Dupuis"
        response = self.client.post(
            "/roles/profileupdate",
            {
                'first_name': new_first_name,
                "last_name": new_last_name,
                "email": new_email
            }
        )
        assert response.status_code == 200
    """


"""

    def test_find_user_category_favourites(self):
       Tests if a user has a product in a category
        favourites = rviews.sort_favourites(4, "soup")
        assert favourites is not None

        def test_find_favorite_in_products(self):

            '''Tests if a liked product is found in the products table.'''

            product = PRODUCT_EXAMPLE
            query = Products(**product)
            query.save()
            product = rviews.select_product("Gazpacho")
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
            like_data["userid"] = 1
            like_data[
                "front_img"
            ] = IMG_URL

            if not Favorites.objects.filter(
                    productid=like_data["productid"]).exists():
                query = Favorites(**like_data)
                query.save()

            article = rviews.select_liked_in_products(product_id)
            assert article is not None

            
        def test_get_all_user_favs(self):
        '''    Tests the SELECT on all user's favourites'''
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
            like_data[
                "front_img"
            ] = IMG_URL

            if not Favorites.objects.filter(
                    productid=like_data["productid"]).exists():
                query = Favorites(**like_data)
                query.save()
            user_favs = rviews.select_user_favs(4)
            assert user_favs is not None
            assert len(user_favs) > 0
    """

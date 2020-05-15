"""This file is used to test the functions of the two apps. It is called via the pytest command in the terminal"""
from django.contrib.auth import authenticate
import pytest
import requests as re


@pytest.mark.django_db
class TestPurBeurre:
    """Pytest will be used to verify the behaviour of the following functions"""
    URI_f_BASE = "http://localhost:8000/foodfacts/"
    URI_r_BASE = "http://localhost:8000/roles/"
    provided_mail = "ezzou@gmail.com"
    provided_password = "ezzou"

    home_request = URI_f_BASE
    aliment_request = f"{URI_f_BASE}aliment/1/"
    favourites_request = f"{URI_f_BASE}favourites/"
    account_request = f"{URI_f_BASE}account/"
    signin_request = f"{URI_r_BASE}signin/"
    notice_request = f"{URI_f_BASE}notice/"
    resultats_gazpacho = f"{URI_f_BASE}resultats/Gazpacho/"
    resultats_empty = f"{URI_f_BASE}resultats/empty/"
    resultats_register = f"{URI_f_BASE}resultats/register/"

    def test_views_home(self):
        response = re.get(self.home_request)
        assert response.status_code == 200

    def test_views_aliment(self):
        response = re.get(self.aliment_request)
        assert response.status_code == 200

    def test_views_resultats_gazpacho(self):
        response = re.get(self.resultats_gazpacho)
        assert response.status_code == 200

    def test_views_resultats_empty(self):
        response = re.get(self.resultats_empty)
        assert response.status_code == 200

    def test_views_favourites(self):
        response = re.get(self.resultats_gazpacho)
        assert response.status_code == 200

    def test_views_account(self):
        response = re.get(self.account_request)
        assert response.status_code == 200

    def test_views_signin(self):
        response = re.get(self.signin_request)
        assert response.status_code == 200

    def test_views_register(self):
        response = re.get(self.resultats_register)
        assert response.status_code == 200

    def test_views_notice(self):
        response = re.get(self.notice_request)
        assert response.status_code == 200

    def test_update_user_data(self,
                              provided_mail="ezzou@gmail.com",
                              provided_password="ezzou",
                              update_email="test@test.com",
                              update_first_name="Jerôme",
                              update_last_name=""):

        user = authenticate(username="ezzou06060cimper", password=provided_password)
        assert user is not None
        user_before = user

        user_email = user.email
        assert user_email is not None

        first_name = user.first_name
        assert first_name is not None

        last_name = user.last_name
        assert last_name is not None

        new_data = {}

        if user is not None:

            if update_email != "" and update_email != user_email:
                user.email = update_email
                assert user.email != user_email
                new_data["mail"] = user.email
            if update_first_name != "" and update_first_name != first_name:
                user.first_name = update_first_name
                assert user.first_name != first_name
                new_data["first_name"] = user.first_name
            if update_last_name != "" and update_last_name != last_name:
                user.last_name = update_last_name
                assert user.last_name != last_name
                new_data["last_name"] = user.last_name
            user.save()

            user_after = authenticate(username=update_email, password=provided_password)
            assert user_after is not None
            assert user_after != user_before
            assert user_after["first_name"] != user_before.first_name
            assert user_after["last_name"] == user_before.last_name

            user_after.email = user_before.email
            user_after.first_name = user_before.first_name
            user_after.save()
            assert user_after == user_before

        else:
            return KeyError("CANNOT UPDATE A USER WHO DOES NOT EXISTS")

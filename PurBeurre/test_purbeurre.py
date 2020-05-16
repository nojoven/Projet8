"""This file is used to test the functions of the two apps. It is called via the pytest command in the terminal"""
from django.contrib.auth import authenticate
import pytest
import requests as re
from foodfacts.modules.database_service import DatabaseService


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

"""This file is used to test the functions """
import os
from django.http import HttpResponseRedirect
from foodfacts.views import *


class TestPurBeurre:
    """Pytest will be used to verify the behaviour of the following functions"""

    conf = os.environ

    def test_views_home(self):
        assert HttpResponseRedirect.status_code == 200


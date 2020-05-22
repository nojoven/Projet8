import pytest
from django.test import TestCase
from model_bakery import baker
from foodfacts.models import Categories, Favorites, Products


class TestModels(TestCase):
    @pytest.mark.django_db
    def test_category_model(self):
        name__category = baker.make(Categories, name="soup")
        assert name__category is not None
        self.assertEqual(str(name__category), "soup")

    @pytest.mark.django_db
    def test_favourites_model(self):
        name_fav = baker.make(Favorites, name="Gazpacho")
        assert name_fav is not None
        self.assertEqual(str(name_fav), "Gazpacho")

    @pytest.mark.django_db
    def test_products_model(self):
        name_product = baker.make(Products, productname="Gazpacho")
        assert name_product is not None
        self.assertEqual(str(name_product), "Gazpacho")

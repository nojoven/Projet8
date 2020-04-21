"""
API call

This code allows to fetch the data from the OpenFoodFact API.
It uses the built-in modules JSON and requests
"""
import requests as reqs
from json import JSONDecodeError


class Collector:
    """

    The collect of the data is done by a Collector object.

    This class is used to rerieve the products data by calling the OpenFoodFacts API.
    """
    def __init__(self):
        """

        Request components

        When instantiated a Collector object receives two attributes that are necessary to send an HTTP request:
        - the query params
        - the url
        """
        # We limit the fetch to 1000 products
        self.params = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': 'category', 'sort_by': 'unique_scans_n', 'page_size': 1000, 'json': 1}
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def get_products_by_category(self, category):
        """

        Five API requests for my five categories.

        I send a GET request for 1000 product of a category, then 1000 from another one, etc.
        """
        # I create lists to use them later
        results = []
        products = []
        try:
            self.params["tag_0"] = category
            req = reqs.get(self.url, self.params)
            data = req.json()
            # data is a huge json document but we only keep the products information
            products = data["products"]

        except JSONDecodeError:
            pass
        for product in products:
            try:
                # I ignore the products that have missing informations
                if not product["stores_tags"] or not product["quantity"] or not product["product_name"]:
                    continue
                product_data = {
                    "Stores": str(product["stores_tags"])[1:-1],
                    "Brands": product["brands"],
                    "ProductName": product["product_name"],
                    "Nutrigrade": product["nutrition_grade_fr"],
                    "Category": category,
                    "Quantity_String": product["quantity"]
                }
                quantity_string = product_data["Quantity_String"]
                for i, c in enumerate(quantity_string):
                    if not c.isdigit() and c != " ":
                        quantity_number = int(quantity_string[:i])
                        quantity_unit = quantity_string[i:]
                        product_data["Quantity_Number"] = quantity_number
                        product_data["Quantity_Unit"] = quantity_unit.upper()
                        break

            except KeyError:
                continue
            results.append(product_data)
        return results

"""
Data management code

This file is used to interact with the database in order to display and manipulate the data
depending on the user actions in the terminal.
It uses the orm objects Product, Categories and Favorites
"""
from django.db import transaction
from foodfacts.models import Categories, Favorites, Products, Users


class DatabaseService:
    """
    DatabaseServices

    Class created to provide statics methods that allows my terminal app do deal with the mysql data.
    Being static makes the call of DatabaseService's functions easier.
    """

    # I created this list here to be accessible inside the methods
    articles_ids = []

    # Insert multiple data at a time in multiple rows in (table Product)
    @staticmethod
    def fill_products_table(plist):
        list_product = []
        for product in plist:
            list_product.append(Products(productname=product["productname"],
            stores=product["stores"],
            brands=product["brands"],
            nutrigrade=product["nutrigrade"],
            quantity=product["quantity"],
            category=product["category"],
            front_img=product["front_img"],
            nutrition_img=product["nutrition_img"],
            ingredients_img=product["ingredients_img"],
            fat_100g=product["fat_100g"],
            sugars_100g=product["sugars_100g"],
            saturated_fat_100g=product["saturated_fat_100g"],
            energy_kcal_100g=product["energy_kcal_100g"],
            nutrition_Score_100g=product["nutrition_Score_100g"],
            fiber_100g=product["fiber_100g"],
            salt_100g=product["salt_100g"],
            proteins_100g=product["proteins_100g"],
            carbs_100g=product["carbs_100g"],
            sodium_100g=product["sodium_100g"]))


        Products.objects.bulk_create(list_product)

    # Insert multiple data at a time in multiple rows in (table Categories)
    @staticmethod
    def fill_categories_table(category):
        if not Categories.objects.filter(name=category["name"]).exists():
            query = Categories(**category)
            query.save()

    # Returns the content of the table Categories
    @staticmethod
    def show_entire_categories_table():
        categories_table = Categories.objects.all().dicts()
        return categories_table

    # Prints the products that correspond to the category selected by the user
    @staticmethod
    def show_all_category_products(category_selected):
        """

        To show the wanted products

        I look for the name of the category selected in the column of the category.
        """
        entire_category = Products.objects.filter(category=category_selected).dicts()
        for article in entire_category:
            DatabaseService.articles_ids.append(article['idProduct'])
            print(f"{article['idProduct']} : {article['ProductName']}")

    # Prints in the category selected
    # the products that have a better nutrigrade than the substituted product




    @staticmethod
    def show_better_products(product_id, category_selected, user_id):
        """
        Substitution process

        This method starts with the display of the better products.
        Then the user is asked to select a preferred product.
        Finally the preferred product is saved in the table 'Favorite'.
        """
        product_data = Products.objects.get(idProduct=product_id)
        product_nutrigrade = product_data.Nutrigrade
        print(f"Nutrigrade is {product_nutrigrade}. ")
        better_products = Products.objects.filter(category=category_selected, nutrigrade__lt=product_nutrigrade)

        if len(better_products) != 0:
            better_ids = []
            for better in better_products:
                print(f"{better.idProduct}---{better.ProductName}:{better.Nutrigrade}")
                better_ids.append(better.idProduct)

            better_choice = None
            while better_choice not in better_ids:
                try:
                    print("Choose a product to replace the bad product.")
                    better_choice = int(input("Enter the ID of a better product: "))
                except ValueError:
                    continue

            if better_choice in better_ids:
                good_product = Products.objects.get(idProduct=better_choice)
                good_id = better_choice
                good_category = good_product.Category
                good_brands = good_product.Brands
                good_stores = good_product.Stores
                good_quantity = good_product.Quantity
                print(f"You don't like \n{product_data.idProduct}--{product_data.ProductName} "
                      f"\n--Nutrigrade = {product_data.Nutrigrade}. \n"
                      f"You prefer {better_choice}---{good_product.ProductName}. \n"
                      f"Nutrigrade = {good_product.Nutrigrade} "
                      f" \n Favorites table edition...")
                DatabaseService.save_preference(good_id, good_category, good_product.ProductName,
                                                good_product.Nutrigrade, good_stores, good_brands, good_quantity,
                                                product_data.idProduct, product_data.ProductName,
                                                product_data.Nutrigrade, user_id)
        else:
            print("The nutriscore is already 'A'. There is no better product.")

    # Saves the preferred product with some data about the replaced one in the table 'Favorites'
    @staticmethod
    def save_preference(preferred_id, preferred_category, preferred_name, preferred_grade,
                        preferred_stores, preferred_brands, preferred_quantity,
                        replaced_id, replaced_name, replaced_grade, user_id):
        """

        Saving the preferred products.

        I save it by providing the data for each column of the entry row including the user id.
        You cannot save a substitution that is already recorded.
        """
        already_saved = Favorites.objects.filter(productID=preferred_id, replacedID=replaced_id, userID=user_id).dicts()

        if len(already_saved) == 0:
            query = Favorites.objects.bulk_create(ProductID=preferred_id, Name=preferred_name, Nutrigrade=preferred_grade,
                                     Category=preferred_category, Stores=preferred_stores,
                                     Brands=preferred_brands, Quantity=preferred_quantity,
                                     ReplacedID=replaced_id, ReplacedArticle=replaced_name,
                                     ReplacedNutrigrade=replaced_grade, UserID=user_id)
            query.save()
            print("Favorites updated. ")
        else:
            print("This favorite already exists. ")

    @staticmethod
    def select_better_products(product_id, category_selected, user_id):
        """
        Substitution process

        This method starts with the display of the better products.
        Then the user is asked to select a preferred product.
        Finally the preferred product is saved in the table 'Favorite'.
        """
        product_data = Products.objects.get(idProduct=product_id)
        product_nutrigrade = product_data.Nutrigrade

    # Displays the content of the table Favorites that correspond to the current user.
    @staticmethod
    def show_favorites(user_id):
        """

        Displaying the user's preferences.

        To fetch the user's favorites I only look for the enties that have the user ID of the current user.
        """
        favorites_table = Favorites.objects.get(userID=user_id).dicts()
        if len(favorites_table) != 0:
            for fav in favorites_table:
                print(f"{fav} \n")
        else:
            print("You have no favorite. ")

    # Save the user to create it in mysql
    @staticmethod
    def save_user(username, userpass):
        """

        Adding a user to the database.

        In the table 'Users' there are three columns:
        - one for the ID
        - one for the password
        - one for the username
        The ID which is the primary key is auto-incremented.
        So we only provide the username and the password of the current user to the database engine.
        """
        query = Users.objects.bulk_create(Username=username, password=userpass)
        query.save()
        print("User created. ")

    # Login user
    @staticmethod
    def authentify_user(username, userpass):
        """

        Login

        I check the validity of the username input and the password input by verifying if there is a user who
        possesses these username and password
        """
        query = Users.objects.filter(username=username, password=userpass)
        return query

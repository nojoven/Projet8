# README DU PROJET 8

## Présentation

L'objectif de ce projet est de récupérer des données mises à disposition par l'API OpenFoodFacts afin de développer une solution web fullstack avec le framework backend Django.

Le client est PurBeurre comme au projet 5.
D'après le cahier des charges qu'il nous a fourni il souhaite:
- l'utilisation de sa charte graphique
- l'intégration d'un template téléchargeable
- des couleurs chaudes 
- cette icône de carotte pour le menu. 
- une photo qu'il a choisie en fond de la page d’accueil.

Le projet est suivi sur Trello et le produit final est accessible à l’adresse 
(https://beurrepur.herokuapp.com/) 

## Lien GitHub: 
(https://github.com/nojoven/Projet8) 

## Exécution

    • L’environnement virtuel a été généré avec pipenv. 
    • En local il faudra donc utiliser pipenv shell  avant de pouvoir démarrer le serveur (localhost:8000).
    • Projet Django créé avec manage.py 
    • Ajout du chemin vers les variables d’environnement: $env:DJANGO_SETTINGS_MODULE='PurBeurre.settings'
    • Lancement local avec python manage.py runserver
    • Remplissage local de la basse de données: manage.py fill_db
    • Remplissage Heroku de la basse de données: 
      heroku run manage.py fill_db
      (nécessite heroku run python manage.py migrate )
    • Liste des requirements accessible avec pip freeze
    • Le fichier pytest.ini, à la racine, permet de lancer en un appel de pytest tous les tests du projet
    • Exécution des tests d’intégration: python manage.py test
    • Tests de couverture: coverage run suivi de coverage report (voir documentation de la stratégie de tests)
    • Lecture des logs heroku: heroku logs --tail



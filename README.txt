README DU PROJET 8

Pr�sentation

L'objectif de ce projet est de r�cup�rer des donn�es mises �disposition par l'API OpenFoodFacts afin de d�velopper une solution web fullstack avec le framework backend Django.

Le client est PurBeurre comme au projet 5.
D'apr�s le cahier des charges qu'il nous a fourni il souhaite:
- l'utilisation de sa charte graphique
- l'int�gration d'un template t�l�chargeable
- des couleurs chaudes 
- cette ic�ne de carotte pour le menu. 
- une photo qu'il a choisie en fond de la page d�accueil.

Le projet est suivi sur Trello et le produit final est accessible � l�adresse 
https://beurrepur.herokuapp.com/ 

Lien Github�: https://github.com/nojoven/Projet8 

Ex�cution

    � L�environnement virtuel a �t� g�n�r� avec pipenv. 
    � En local il faudra donc utiliser pipenv shell  avant de pouvoir d�marrer le serveur (localhost:8000).
    � Projet Django cr�� avec manage.py 
    � Ajout du chemin vers les variables d�environnement�: $env:DJANGO_SETTINGS_MODULE='PurBeurre.settings'
    � Lancement local avec python manage.py runserver
    � Remplissage local de la basse de donn�es�: manage.py fill_db
    � Remplissage Heroku de la basse de donn�es�: 
      heroku run manage.py fill_db
      (n�cessite heroku run python manage.py migrate )
    � Liste des requirements accessible avec pip freeze
    � Le fichier pytest.ini, � la racine, permet de lancer en un appel de pytest tous les tests du projet
    � Ex�cution des tests�d�int�gration�: python manage.py test
    � Tests de couverture�: coverage run suivi de coverage report (voir documentation de la strat�gie de tests)
    � Lecture des logs heroku�: heroku logs --tail



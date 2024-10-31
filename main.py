from flask import Flask, render_template
# On donne accès au fichier pendu.py
from pendu import Pendu
#Pour les données sécurisées
import os

# On crée l'application
app = Flask("MonPendu")
# Cookie de session pour l'utilisateur
app.secret_key = os.urandom(24)


# Route de la page d'accueil
@app.route("/")
def index():
  return render_template('index.html')

  
# On lance l'application
app.run("0.0.0.0","3904", debug=True)
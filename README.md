#  Scoria – Prédiction de Cotisations d'Assurance Habitation

**Scoria** est un projet de modélisation prédictive visant à estimer la **cotisation annuelle** d’un contrat d’assurance habitation à partir de caractéristiques client et logement.

---

##  Objectif du projet

Ce projet vise à prédire la **cotisation annuelle** d’un contrat d’assurance habitation en se basant sur les caractéristiques suivantes :

- **`surface m2`** : superficie du logement en mètres carrés  
- **`statut logement`** : statut d’occupation du logement (propriétaire, locataire)  
- **`patrimoine estime`** : estimation du patrimoine du client  
- **`montant couvert`** : montant total souhaité par le client pour la couverture

L’objectif est de développer un modèle de régression capable de fournir une estimation fiable de la cotisation annuelle, afin d’aider à la tarification ou à la personnalisation des offres.

---

## Contenu du dépôt

| Fichier | Description |
|---------|-------------|
| `bloc3.ipynb` | Préparation des données et entraînement des modèles , Comparaison des performances des modèles (régression, arbres, boosting) |
| `comparaison_bloc5.ipynb` |  |
| `app.py` | Script d'exécution ou interface de prédiction |
| `courbes_apprentissage.png` | Courbes RMSE / MAE des modèles entraînés |
| `README.md` | Présentation du projet (ce fichier) |


---

##  Installation

python -m venv env

source env/bin/activate  # sur Linux/macOS

env\Scripts\activate     # sur Windows

pip install -r requirements.txt


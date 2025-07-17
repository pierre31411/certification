#  Scoria – Prédiction de Cotisations d'Assurance Habitation

**Scoria** est un projet de modélisation prédictive visant à estimer la **cotisation annuelle** d’un contrat d’assurance habitation à partir de caractéristiques client et logement.

---

## Données simulées (DataFrame)

Les personas sont générés de manière synthétique à l’aide de la bibliothèque **Faker** et de règles statistiques personnalisées, car il est difficile d’obtenir des données publiques détaillées sur les contrats d’assurance habitation en France.

Chaque persona représente un **client fictif** avec des caractéristiques réalistes, basées sur des données statistiques officielles telles que celles de **l’INSEE** (répartition par âge, statut d’occupation, revenus moyens).

Ce processus permet de construire un jeu de données cohérent et  réaliste  .

---

##  Objectif du projet

Ce projet vise à prédire la **cotisation annuelle** d’un contrat d’assurance habitation en se basant sur les caractéristiques suivantes :

- **`surface_m2`** : superficie du logement en mètres carrés  
- **`statut_logement`** : statut d’occupation du logement (propriétaire, locataire)  
- **`patrimoine_estime`** : estimation du patrimoine du client  
- **`montant_couvert`** : montant total souhaité par le client pour la couverture

L’objectif est de développer un **modèle de régression** capable de fournir une estimation fiable de la cotisation, afin de contribuer à la tarification ou à la personnalisation des offres d’assurance.

---

##  Contenu du dépôt

| Fichier                    | Description |
|---------------------------|-------------|
| `bloc3.ipynb`             | Préparation des données et entraînement des modèles ; comparaison des performances (régression linéaire, forêts, boosting) |
| `bloc_5.ipynb` |   Préparation des données et entraînement par apprentissage profond (ANN)  |
| `app.py`                  | Script d'exécution ou interface de prédiction |
| `README.md`               | Présentation du projet |

---

##  Installation

Version Python recommandée : **3.12.1**

Créer et activer un environnement virtuel :

```bash
python -m venv env
env\Scripts\activate        # sous Windows
source env/bin/activate     # sous macOS / Linux




# 📊 Supplier KPI Analysis & Performance Dashboard

## 📝 Description du Projet

 L'objectif est d'explorer, nettoyer et analyser le jeu de données afin d'en extraire des insights stratégiques sur les achats.

Le dataset d'origine provient de Kaggle:https://www.kaggle.com/datasets/shahriarkabir/procurement-kpi-analysis-dataset/data

## 📂 Structure du Projet
```text
SUPPLIER_KPI_ANALYSIS/
│
├── data/
│   ├── Dataset_brut.csv      # Données brutes initiales
│   └── Dataset_clean.csv     # Données nettoyées et enrichies
│
├── src/
│   ├── nettoyage.py          # Script de nettoyage et d'ingénierie des caractéristiques
│   └── analyse.py            # Script d'analyse statistique et de visualisation
│
├── nettoyage.ipynb           # Notebook Jupyter interactif pour le nettoyage et analyse
└── README.md                 # Documentation du projet
```
## ⚙️ Pipeline de Nettoyage (`nettoyage.py`)

Le script de nettoyage réalise les opérations suivantes :

1.Normalisation des textes : Suppression des espaces superflus (.strip()), mise en majuscules des identifiants (PO_ID), formatage des noms de fournisseurs (.title()) et des catégories.

2.Gestion des dates : Conversion des dates de commande (Order_Date) et de livraison (Delivery_Date) au format datetime (errors='coerce').

3.Calcul des KPIs dérivés :

- Expected_Spend = Quantity × Unit_Price (Dépense théorique)
- Total_Spend = Quantity × Negotiated_Price (Dépense réelle)
- Savings_per_Order = Expected_Spend - Total_Spend (Économies réalisées)
- Defect_Rate = (Defective_Units / Quantity) × 100 (Taux de défaut en %)
- Lead_time = Delivery_Date - Order_Date (Délai de livraison en jours)

4.Filtrage et Export : Suppression des doublons et des lignes aberrantes (Lead time négatif), puis exportation vers data/Dataset_clean.csv


## 📈 Indicateurs & Analyses Clés (`analyse.py`)
Le projet analyse plusieurs axes critiques :

Dépenses Totales (Total_Spend) : Classement des fournisseurs par volume d'achat global (pour les commandes livrées).

Qualité (Defect_Rate) : Suivi du taux de défaut moyen par fournisseur pour identifier les risques qualité.

Efficacité Opérationnelle (Lead_time & Compliance) : Évaluation du délai moyen de livraison, de sa stabilité (écart-type std) et du taux de conformité des commandes.

## 🚀 Guide d'Utilisation

1.Cloner le dépôt ou ouvrir le dossier du projet dans votre environnement de travail (ex: VS Code).

2.Activer l'environnement virtuel 
Lancer le nettoyage des données :

3.Exécutez le script de nettoyage ou le notebook nettoyage.ipynb pour générer Dataset_clean.csv.

4.Lancer l'analyse et les visualisations :
Ouvrez analyse.ipynb ou exécutez vos scripts de visualisation (matplotlib / seaborn) pour afficher les graphiques de performance.

## 🛠️ Prérequis Techniques
* Python 3.12+
* Bibliothèques requises : `pandas`, `matplotlib`, `seaborn`
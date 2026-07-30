# 📊 Supplier KPI Analysis & Performance Dashboard

## 📝 Description du Projet

L'objectif est d'explorer, nettoyer et analyser le jeu de données afin d'en extraire des insights stratégiques sur les achats.

Le dataset d'origine provient de Kaggle : https://www.kaggle.com/datasets/shahriarkabir/procurement-kpi-analysis-dataset/data

## 📁 Structure du Projet

```text
SUPPLIER_KPI_ANALYSIS/
│
├── data/
│   ├── Dataset_brut.csv        # Données brutes initiales
│   ├── Dataset_clean.csv       # Données nettoyées et enrichies (incl. Compliance_Flag)
│   └── Supplier_Summary.csv    # Résumé des KPI par fournisseur (référence/validation)
│
├── src/
│   ├── nettoyage.py            # Script de nettoyage et d'ingénierie des caractéristiques
│   └── analyse.py              # Script d'analyse statistique et de visualisation
│
└── README.md                   # Documentation du projet
```

## ⚙️ Pipeline de Nettoyage (`nettoyage.py`)

Le script de nettoyage réalise les opérations suivantes :

1. **Normalisation des textes** : Suppression des espaces superflus (`.strip()`), mise en majuscules des identifiants (`PO_ID`), formatage des noms de fournisseurs (`.title()`) et des catégories.

2. **Gestion des dates** : Conversion des dates de commande (`Order_Date`) et de livraison (`Delivery_Date`) au format datetime (`errors='coerce'`).

3. **Calcul des KPIs dérivés** :
   - `Expected_Spend` = Quantity × Unit_Price (Dépense théorique)
   - `Total_Spend` = Quantity × Negotiated_Price (Dépense réelle)
   - `Savings_per_Order` = Expected_Spend - Total_Spend (Économies réalisées)
   - `Defect_Rate` = (Defective_Units / Quantity) × 100 (Taux de défaut en %)
   - `Compliance_Flag` = conversion de Compliance (Yes/No) en valeur binaire (1/0)
   - `Lead_time` = Delivery_Date - Order_Date (Délai de livraison en jours)

4. **Filtrage et Export** : Suppression des doublons et des lignes aberrantes (Lead time négatif), puis exportation vers `data/Dataset_clean.csv`

## 📈 Indicateurs & Analyses Clés (`analyse.py`)

Le projet analyse plusieurs axes critiques (calculés sur les commandes livrées, sauf mention contraire) :

- **Dépenses Totales** (`Total_Spend`) : Classement des fournisseurs par volume d'achat global, et répartition par catégorie de produit (`Item_Category`).
- **Économies** (`Savings_per_Order`) : Taux d'efficacité de négociation global.
- **Qualité** (`Defect_Rate`) : Suivi du taux de défaut moyen par fournisseur pour identifier les risques qualité.
- **Conformité** (`Compliance`) : Taux de conformité global et par fournisseur, avec une analyse croisée pour vérifier son impact sur le taux de défaut et le délai de livraison.
- **Efficacité Opérationnelle** (`Lead_time`) : Délai moyen de livraison par fournisseur, comparé à la moyenne globale.

Un tableau récapitulatif (`supplier_summary`) regroupant ces mesures par fournisseur est généré en fin de script et exporté vers `data/Supplier_Summary.csv`.

## 📊 Fichiers de Sortie pour Power BI

- **`Dataset_clean.csv`** : table de faits (une ligne par commande), à importer dans Power BI comme source principale. Contient toutes les colonnes nettoyées ainsi que `Compliance_Flag`, utilisé pour calculer le taux de conformité via DAX.

- **`Supplier_Summary.csv`** : tableau récapitulatif des KPI par fournisseur (dépense totale, taux de défectuosité moyen, délai de livraison moyen, économies totales, taux de conformité). Sert de référence pour valider les mesures DAX — l'import direct de `Dataset_clean.csv` avec des mesures DAX est recommandé pour plus de flexibilité dans le dashboard.
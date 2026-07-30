#===============================================
#  Nettoyage
#===============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Dataset_brut.csv')
nb_ligne_brut = df.shape[0]

df['PO_ID']=df['PO_ID'].str.strip().str.upper()
df['Supplier']= df['Supplier'].str.strip().str.title()
df['Item_Category'] =df['Item_Category'].str.strip().str.lower()
df['Order_Status'] =df['Order_Status'].str.strip().str.capitalize()

df['Order_Date'] = df['Order_Date'].str.strip()
df['Order_Date'] = pd.to_datetime(df['Order_Date'],format = 'mixed', errors = "coerce")
df['Delivery_Date'] = df['Delivery_Date'].str.strip()
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'],format = 'mixed', errors='coerce')

df['Defective_Units'] = df['Defective_Units'].fillna(0)
df['Expected_Spend'] = df['Quantity']*df['Unit_Price']
df['Total_Spend'] = df['Quantity'] * df['Negotiated_Price']
df['Savings_per_Order'] = df['Expected_Spend'] - df['Total_Spend']
df['Defect_Rate'] = (df['Defective_Units'] / df['Quantity']) * 100

df['Lead_time'] = (df['Delivery_Date']-df['Order_Date']).dt.days

df = df.drop_duplicates()
df = df[(df['Lead_time'] >= 0) | (df['Lead_time'].isna())].copy()
nb_ligne_clean = df.shape[0]
nb_ligne_sup= nb_ligne_brut-nb_ligne_clean

print(f'Nbre de lignes supprimée(s) : {nb_ligne_sup}')

df.to_csv('data/Dataset_clean.csv', index=False)
print("Données nettoyées exportées avec succès vers 'Dataset_clean.csv'")


#===============================================
#  Analyse
#===============================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Dataset_clean.csv')

condition = df['Order_Status']== 'Delivered'
df_deliverd = df[condition].copy()

# ----Cost Performance-----------
total_savings = df['Expected_Spend'].sum()-df['Total_Spend'].sum()
print(f'Total économie : {total_savings:.2f}')

Negotiation_Efficiency = total_savings / df['Expected_Spend'].sum()
print(f"Le taux de rentabilité de négociation : {Negotiation_Efficiency*100:.2f}%")

Spend_supplier = df_deliverd.groupby('Supplier')['Total_Spend'].sum().sort_values(ascending=False)
print(Spend_supplier)
for i,(nom,val),in enumerate(Spend_supplier.items(),1):
    pourcentage = (val/df['Total_Spend'].sum())*100
    print(f" Numéro {i} | fournisseur : {nom:<15} | montant d'achat : {val:.2f} | pourcentage :{pourcentage:.2f}%")

#-----Supplier Performance---------
Defect_Rate_Supplier = df.groupby('Supplier')['Defect_Rate'].mean().sort_values(ascending=False)
print(Defect_Rate_Supplier)
for i,(nom,taux) in enumerate(Defect_Rate_Supplier.items(),1):
    print(f"Numéro {i}  | nom de fournisseur : {nom:<15} | taux de defectueux:{taux:.2f}%")


#-----Lead_Time_Performance---------
temps_livraison_moyenne = round(df_deliverd['Lead_time'].mean(),2)
print(temps_livraison_moyenne)
Lead_Time_Performa = df_deliverd.groupby('Supplier')['Lead_time'].mean().sort_values(ascending=False)
print(Lead_Time_Performa )
for i,(nom,jours) in enumerate(Lead_Time_Performa.items()):
    if jours > temps_livraison_moyenne:
        print(f" Temps de livraison en moyenne de {nom} est supérieur que la moyenne :{temps_livraison_moyenne} jours")


#-----Summary rapport---------
supplier_summary = df_deliverd.groupby('Supplier').agg({
    'Total_Spend': 'sum',
    'Defect_Rate': 'mean',
    'Lead_time': 'mean',
    'Savings_per_Order': 'sum'
}).sort_values(by='Savings_per_Order', ascending=False)
print(supplier_summary)
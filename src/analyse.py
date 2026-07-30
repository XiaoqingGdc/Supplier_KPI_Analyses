#===============================================
#  Analyse
#===============================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Dataset_clean.csv', parse_dates=['Order_Date', 'Delivery_Date'])
print(df.columns)

condition = df['Order_Status'] == 'Delivered'
df_deliverd = df[condition].copy()


# ----Cost Performance / Performance des Coûts / 成本绩效-----------
total_savings = df['Expected_Spend'].sum() - df['Total_Spend'].sum()
print(f'Total économie : {total_savings:.2f}')

Negotiation_Efficiency = total_savings / df['Expected_Spend'].sum()
print(f"Le taux de rentabilité de négociation : {Negotiation_Efficiency*100:.2f}%")

Spend_supplier = df_deliverd.groupby('Supplier')['Total_Spend'].sum().sort_values(ascending=False)
print(Spend_supplier)
for i, (nom, val) in enumerate(Spend_supplier.items(), 1):
    pourcentage = (val / df['Total_Spend'].sum()) * 100
    print(f" Numéro {i} | fournisseur : {nom:<15} | montant d'achat : {val:.2f} | pourcentage :{pourcentage:.2f}%")

# Dépense par Catégorie / 按品类花费
Spend_Category = df_deliverd.groupby('Item_Category')['Total_Spend'].sum().sort_values(ascending=False)
print(Spend_Category)


#-----Supplier Performance / Performance des Fournisseurs / 供应商表现---------
Defect_Rate_Supplier = df_deliverd.groupby('Supplier')['Defect_Rate'].mean().sort_values(ascending=False)
print(Defect_Rate_Supplier)
for i, (nom, taux) in enumerate(Defect_Rate_Supplier.items(), 1):
    print(f"Numéro {i}  | nom de fournisseur : {nom:<15} | taux de defectueux:{taux:.2f}%")

# Taux de Conformité / 合规率
taux_conformite_global = df['Compliance_Flag'].mean() * 100
print(f"Taux de conformité global : {taux_conformite_global:.2f}%")

Compliance_Supplier = (df.groupby('Supplier')['Compliance_Flag'].mean() * 100).sort_values(ascending=False)
print(Compliance_Supplier)

# Vérification : la conformité influence-t-elle la performance ?
Compliance_Impact = df.groupby('Compliance')[['Defect_Rate', 'Lead_time']].mean()
print(Compliance_Impact)


#-----Lead_Time_Performance / Performance des Délais de Livraison / 交期表现---------
temps_livraison_moyenne = round(df_deliverd['Lead_time'].mean(), 2)
print(temps_livraison_moyenne)

Lead_Time_Performa = df_deliverd.groupby('Supplier')['Lead_time'].mean().sort_values(ascending=False)
print(Lead_Time_Performa)
for i, (nom, jours) in enumerate(Lead_Time_Performa.items()):
    if jours > temps_livraison_moyenne:
        print(f" Temps de livraison en moyenne de {nom} est supérieur que la moyenne :{temps_livraison_moyenne} jours")


#-----Summary rapport / Rapport de Synthèse / 总结报告---------
supplier_summary = df_deliverd.groupby('Supplier').agg({
    'Total_Spend': 'sum',
    'Defect_Rate': 'mean',
    'Lead_time': 'mean',
    'Savings_per_Order': 'sum',
    'Compliance_Flag': 'mean'
}).rename(columns={'Compliance_Flag': 'Taux_Conformite'}).sort_values(by='Savings_per_Order', ascending=False)

# Conversion en pourcentage pour lisibilité
supplier_summary['Taux_Conformite'] = supplier_summary['Taux_Conformite'] * 100

print(supplier_summary)


#===============================================
#  Export pour Power BI
#===============================================
supplier_summary.to_csv('data/Supplier_Summary.csv')
print("Résumé fournisseurs exporté avec succès vers 'data/Supplier_Summary.csv'")

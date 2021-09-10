import pandas as pd
df = pd.read_csv(r'C:\Users\Ruben Gudmundsrud\Documents\MODULER\Modul_12_Graduation_project\Graduation-project\moh\moh_final.csv')
df2 = pd.read_csv(r'C:\Users\Ruben Gudmundsrud\Documents\MODULER\Modul_12_Graduation_project\Graduation-project\moh\originalkoordinater.csv')
new_df = pd.merge(df, df2,  how='inner', left_on=['x', 'y'], right_on = ['Østkoordinat', 'nordkoordinat'])
new_df.to_csv(r'C:\Users\Ruben Gudmundsrud\Documents\MODULER\Modul_12_Graduation_project\Graduation-project\moh\koord_moh.csv',index=False)

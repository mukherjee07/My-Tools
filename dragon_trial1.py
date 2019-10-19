###### DRAGON TRIAL ######
import pandas as pd
from chemml.chem import Dragon
import numpy as np
#df=pd.read_csv('energy.csv')
#l=df['index'].tolist()
#print min(l)
#print max(l)
#m={j+1:{'file':'dragon_trial1/Li1_Opt_C%i.mol2'%i} for i,j in zip(l,range(len(l)))}
m='Li1_Opt_C1.mol2'
#print m
model = Dragon(version=7, blocks = range(1,31), molFile = m, molInput='file')
model.script_wizard(script='new', output_directory='./')
model.run()
print (model.data_path)
df_path = model.data_path
print (df_path)
#df = pd.read_csv(df_path,delimiter='\t', engine='python')
#df = df.drop(['No.','NAME'],axis=1)
#df = df.loc[:, (df != df.ix[0]).any()]
#df1= df.replace(to_replace='nan',value=np.nan)
#df1=df1.replace(to_replace='na',value=np.nan)
#df1.dropna(axis=1,inplace=True)
#df1.to_csv('final_energy.csv',header=True)

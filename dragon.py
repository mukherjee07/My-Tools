import pandas as pd
from cheml.chem import Dragon
#from cheml.initialization import XYZreader
#from cheml.initialization import ConvertFile
import numpy as np
#r=XYZreader(['mol[0-9].xyz','mol[1-3][0-9].xyz'],'/projects/academic/hachmann/aditya/DES/ffopt/MMFF94s/xyz/',reader='manual',path_only=True)

#m=r.read()
#print m

#m={i+1:{'file':'../xyz/dft_%i.xyz'%i,'mol':None}for i in range(36)}


#f=open('a.txt','w')
#f.write(str(m))
#f.close()
#cv=ConvertFile(m,'xyz','mol2')
#path=cv.convert()

#p=pd.DataFrame(path,columns=['path'])
#p.to_csv('paths.csv')
#df = pd.read_csv('newchclhbdmp.csv')
#ss = pd.DataFrame(list(df['HBD SMILES']),columns=['hbd_smi'])
#ss.to_csv('HBD_SMILES.csv',header=False,index=False)
#print path
df=pd.read_csv('duplicate_free_hildebrand.csv')
l=df['Unnamed: 0'].tolist()
print min(l)
print max(l)
m={j+1:{'file':'dragon_trial1/Li1_Opt_C%i.mol2'%i} for i,j in zip(l,range(len(l)))}
print m
model = Dragon(version=7,blocks = range(1,31),molFile=m,molInput="file")
model.script_wizard(script='new', output_directory='test')
model.run()
print model.data_path
df_path = model.data_path
print df_path
df = pd.read_csv(df_path,delimiter='\t', engine='python')
df = df.drop(['No.','NAME'],axis=1)
df = df.loc[:, (df != df.ix[0]).any()]
df1= df.replace(to_replace='nan',value=np.nan)
df1=df1.replace(to_replace='na',value=np.nan)
df1.dropna(axis=1,inplace=True)
df1.to_csv('final_energy.csv',header=True)


import re
import pandas as pd

with open('onelinefile.txt','r') as f: #1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry4Ddd9.55Biology5Eee4.0Social6Fff7.6English7Ggg3.111Maths8Hhh9.99Physics9Iii1.23Civics

   
    column1 = []
    column2 = []
    column3 = []
    column4 = []
   
    fcon = f.read()
    f.close()

    data = fcon
   
    while len(data)>0:
      
      patternformat = re.search('[0-9]+',data)
      stend = patternformat.span()
      column1.append(data[stend[0]:stend[1]])
      data = "" + data[stend[1]:]
      

      patternformat2 = re.search('[A-Z][a-z][a-z]',data)
      stend2 = patternformat2.span()      
      column2.append(data[stend2[0]:stend2[1]])
      data = "" + data[stend2[1]:]
      
      patternformat3 = re.search('[+-]?[0-9]+\.[0-9]+',data)
      stend3 = patternformat3.span()
      column3.append(data[stend3[0]:stend3[1]])
      data = "" + data[stend3[1]:]
      

      patternformat4 = re.search('[A-Z][a-z]+',data)
      stend4 = patternformat4.span()
      column4.append(data[stend4[0]:stend4[1]])
      data = "" + data[stend4[1]:]
         


map(int,column1)
map(str,column2)
map(float,column3)
map(str,column4)

df = pd.DataFrame(list(zip(column1,column2,column3,column4)), index=None, columns=None)

csvfile = df.to_csv('onelinefile.csv',index=None,header=False)

df_csv = pd.read_csv('onelinefile.csv',header=None)
print("csv dataframe:\n",df_csv,"\n")


print("Contents in the onelinefile.csv file:\n")
with open('onelinefile.csv') as f2:
    f2con = f2.readline()

    while(len(f2con)>0):
        print(f2con)
        f2con = f2.readline()

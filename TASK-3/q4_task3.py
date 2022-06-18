import pandas as pd
inputs = input().split(" ")
series = pd.Series(inputs)
#series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
converted = series.map(lambda u: u[0].upper() + u[1:])
ls = list([converted[i] for i in range(0,len(converted))])
string = str(' '.join(ls))
print(string)
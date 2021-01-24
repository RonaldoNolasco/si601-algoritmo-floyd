import pandas as pd
df = pd.read_excel('floyd_data.xlsx', index_col=0)

print(df)

# print(df.loc["n1", "n3"])

print(len(df.index))
print(len(df.columns))
"""
arr = [ [1,2,3],
        [3,2,5]]

for i in range(0,2):
    for j in range(0,3):
        print(arr[i][j])
"""
""" NO
for index, row in df.iterrows():
    for j in range(0,4):
        print(row[j])
"""
"""
i = 0
j = 0
while(i<4):
    while(j<4):
        print(df[i][j])
        j+=1
    j=0
    i+=1
"""
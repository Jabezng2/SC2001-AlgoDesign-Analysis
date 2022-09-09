import pandas as pd
import random

ARRSIZE = 10000000 #array size

ascending_sorted = [x for x in range(0, ARRSIZE)] #sorted array in ascending order
descending_sorted = [x for x in range(ARRSIZE, 0, -1)] #sorted array in descending order
df = pd.DataFrame({'Ascending': ascending_sorted, 'Descending': descending_sorted}) #initialise dataset with two columns of sorted arrays

itersize = 10
count = 0
while count < itersize: #generate columns with values in random order
    colname = 'rand' + str(count) #generate column name
    df[colname] = [random.randint(0, ARRSIZE) for x in range(0, ARRSIZE)] #add new column with new random array
    count += 1

df.to_csv("exampleClass1DatasetSize" + str(ARRSIZE) +".csv")

print(df)
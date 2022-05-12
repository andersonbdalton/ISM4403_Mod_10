import pandas as pd
import csv

f = pd.read_csv('lab9_flat_file_try3.csv')

reader = csv.reader(f)
headers = next( reader, None )

print( headers )
 
column = {}
for h in headers:
    column[h] = []

print( column )

for row in reader:
    for h, v in zip( headers, row ):
        column[h].append(v)
        
# How do we skip a row???
print( "Columns: ", len( column ) )
print( "Rows: ", len( column['id'] ) )

print( "Entire sheet: \n", column )

for c in column:
    print( c.lower(), "," , end="", sep='' )
    
print()
for x in range(0, len( column['id'] )):
    line = ""
    for c in column:
        print( column[c][x].strip().lower(), ",", end='', sep='' )
        line += column[c][x].strip() + ","
    print("")
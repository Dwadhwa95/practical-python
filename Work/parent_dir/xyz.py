import fileparse 
import gzip 
with gzip.open('Data/portfolio.csv.gz', 'rt') as file: 
    port = fileparse.parse_csv(file, types = [str, int, float], delimiter = ',', silence_errors = True)
    print(port)

lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
port = fileparse.parse_csv(lines, types=[str,int,float], delimiter = ',', silence_errors = True )
print(port)



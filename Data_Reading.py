import pandas as pd

data = pd.read_csv("Ecommerce Customers")
#print(data)

print(data.head(),"\n",data.info(),"\n",data.describe())


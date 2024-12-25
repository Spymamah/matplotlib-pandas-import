import pandas as pd
from sklearn.datasets import load_breast_cancer
import numpy as np

breast_cancer = load_breast_cancer()

# print(type(breast_cancer))
   
#  print(breast_cancer)

breast_cancer_df = pd.DataFrame(breast_cancer.data, columns = breast_cancer.feature_names)
# print(breast_cancer_df.tail())

# breast_df = pd.read_csv("C:/Users/user/Desktop/HousingData.csv")
# print(breast_df.head())
# print(type(breast_df))
# print(breast_df.size)

# breast_df.to_excel("health1.xlsx ")

# now = breast_df.info()
# print(now)
print(breast_cancer) 
breast_cancer_df['Price'] = breast_cancer.target
print(breast_cancer_df.head())
now1 = breast_cancer_df.value_counts('Price')
print(now1)
now2 = breast_cancer_df.groupby('Price').mean()
print(now2)
print(breast_cancer_df.corr())
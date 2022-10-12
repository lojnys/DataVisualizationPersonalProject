# import csv
import pandas as pd
import matplotlib.pyplot as plt

"""This project is for displaying a graph of adult criminal courts, number of cases
and cahrges by type of decision. The data is extracted from Statistics Canada."""

filename = '/Users/yushinnam/Desktop/python3/DataVisualizationPersonalProject/NumberOfCases:CourtProject/data_total.csv'
df = pd.read_csv(filename)


# Extracting years from the data as a list (to iterate)


# Classifying data by year
classified_list = []

for i in range(0, len(df.index)):
    if df['REF_DATE'][i] == '2016/2017':
        classified_list.append(df['VALUE'][i])
    
print(classified_list)

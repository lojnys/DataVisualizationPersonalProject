# import csv
import pandas as pd

"""This project is for displaying a graph of adult criminal courts, number of cases
and cahrges by type of decision. The data is extracted from Statistics Canada."""

class Data(): 

    filename = '/Users/yushinnam/Desktop/python3/DataVisualizationPersonalProject/NumberOfCases:CourtProject/data_total.csv'
    df = pd.read_csv(filename)


    # EFFECTS: Extracting years from the data as a list (to iterate)
    def getYears() -> list:
        """a method to extract a list of years from the data"""
        """this method can be used for x values of the graph"""

        year_list = []
        for i in range(0, len(df.index)):
            if not(df['REF_DATE'][i] in year_list): 
                year_list.append(df['REF_DATE'][i])
        
        return year_list


    # EFFETS: Classifying data by year
    # REQUIRES: year > 0 and 
    #           the number of elements in typeOfDecisionList and classified_list must be the same
    def classifyByYear(year: int) -> list:
        year1 = str(year)
        year2 = str(year+1)
        classified_list = []
        classified_dict = {}
        typeOfDecisionList = ["Total decisions", "Guilty", "Percentage guilty", "Acquitted", "Stayed or withdrawn", "Other decisions"]
        final_list = [f'{year1}/{year2}']

        for i in range(0, len(df.index)):
            if df['REF_DATE'][i] == f'{year1}/{year2}':
                classified_list.append(df['VALUE'][i])


        for j in range(0, len(typeOfDecisionList)): 
            classified_dict.update({typeOfDecisionList[j]: classified_list[j]})
        
        final_list.append(classified_dict)

        return final_list


    # EFFECTS: gets the values of the given type of decision
    def getValues(type: str) -> list:
        """This method can be used for the y values of the graph"""

        classfied_values = []

        for i in range(0, len(df.index)): 
            if (df["Type of decision"][i] == type):
                classfied_values.append(df['VALUE'][i])

        return classfied_values


# print(classifyByYear(2016))
# print(getYears())
# print(getValues("Total decisions"))
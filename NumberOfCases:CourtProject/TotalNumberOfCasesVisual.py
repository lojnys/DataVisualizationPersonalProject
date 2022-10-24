import matplotlib.pyplot as plt
from TotalNumberOfCases import Data

if __name__ == "__main__":
    filename = '/Users/yushinnam/Desktop/python3/DataVisualizationPersonalProject/NumberOfCases:CourtProject/data_total.csv'
    data = Data(filename)

    type = input("Which type of decisions would you like to see? ")

    x_values = data.getYears()
    y_values = data.getValues(type)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    plt.plot(x_values, y_values, linewidth=3)

    ax.set_title(type, fontsize=24)
    ax.set_xlabel("Years", fontsize=14)

    plt.show()

'''This program by the admirable Michael Rodriguez
   handles various tasks in SDEV300's Lab 5 assignment'''

import matplotlib.pyplot as plt
import pandas as pd

def menu():
    '''Prints a menu for which csv and column to analyze'''
    selecting = True

    #Loops until the exact proper input is selected for which csv to use
    while selecting:
        print('\nWelcome to the Python Data Analysis App!!!\n' +
              '(1): Population Data\n' +
              '(2): Housing Data\n' +
              '(0): Exit Program\n')

        mainMenuSelection = input("Choose a numbered option: ")

        if mainMenuSelection == '1':
            populationAnalysisMenu(mainMenuSelection)

        elif mainMenuSelection == '2':
            housingAnalysisMenu(mainMenuSelection)

        elif mainMenuSelection == '0':
            print("Thanks for using the data analysis app!\n")
            selecting = False

        else:
            print('Improper input Please make another selection\n')

def histogram(columnHeader, csvSelection):
    '''Creates a numPy array given the selection of a csv and column.
       Presents histogram and final statistics'''

    #Since there is an extreme outlier in the data, I trimmed it to data between -15,000 and 25,000
    if csvSelection == '1' and columnHeader == 'Change Pop':
        populationColumn = pd.read_csv('PopChange.csv', usecols=[columnHeader]).to_numpy()
        plt.hist(populationColumn, 50, range=(-15000, 25000))
        finalStatistics(populationColumn)
        plt.show()

    #Similar extreme outlier in data requiring a different range of trimming. (min to 200,000)
    elif csvSelection == '1':
        populationColumn = pd.read_csv('PopChange.csv', usecols=[columnHeader]).to_numpy()
        plt.hist(populationColumn, 50, range=(populationColumn.min(), 200000))
        finalStatistics(populationColumn)
        plt.show()

    #Handles housing csv data, default histogram settings work nicely
    elif csvSelection == '2':
        housingColumn = pd.read_csv('Housing.csv', usecols=[columnHeader]).to_numpy()
        plt.hist(housingColumn)
        finalStatistics(housingColumn)
        plt.show()

def finalStatistics(columnData):
    '''Calculates the column count, mean, standard deviation, min, and max'''

    #All values have a convenient method that just needed some rounding
    print(f'Total Values:{columnData.size}\n' +
          f'Mean: {columnData.mean():.2f}\n' +
          f'Standard Deviation: {columnData.std():.2f}\n' +
          f'Smallest Value: {columnData.min()}\n' +
          f'Biggest Value: {columnData.max()}\n')

def populationAnalysisMenu(mainMenuSelection):
    '''Generates the menu for analyzing the population csv'''
    analyzingPopulation = True

    #Loops until the exact proper input is selected for which column to analyze
    while analyzingPopulation:
        print('\nSelect the data you want to analyze.\n' +
              '(1): Population April 1\n' +
              '(2): Population Jul 1\n' +
              '(3): Population Change\n' +
              '(0) Exit\n')

        submenuSelection = input('Make a selection: ')

        if submenuSelection == '1':
            histogram('Pop Apr 1', mainMenuSelection)
        elif submenuSelection == '2':
            histogram('Pop Jul 1', mainMenuSelection)
        elif submenuSelection == '3':
            histogram('Change Pop', mainMenuSelection)
        elif submenuSelection == '0':
            print('Exiting population analysis...')
            analyzingPopulation = False
        else:
            print('Invalid input. Please try again.')

def housingAnalysisMenu(mainMenuSelection):
    '''Generates the menu for analyzing the housing csv'''
    analyzingHousing = True

    #Loops until the exact proper input is selected for which column to analyze
    while analyzingHousing:
        print('\nWelcome to the Python Data Analysis App!!!\n' +
              '(1): Age\n' +
              '(2): Bedrooms\n' +
              '(3): Built\n' +
              '(4): Rooms\n' +
              '(5): Utility\n' +
              '(0): Exit\n')

        submenuSelection = input('Make a selection: ')

        if submenuSelection == '1':
            histogram('AGE', mainMenuSelection)
        elif submenuSelection == '2':
            histogram('BEDRMS', mainMenuSelection)
        elif submenuSelection == '3':
            histogram('BUILT', mainMenuSelection)
        elif submenuSelection == '4':
            histogram('ROOMS', mainMenuSelection)
        elif submenuSelection == '5':
            histogram('UTILITY', mainMenuSelection)
        elif submenuSelection == '0':
            print('Exiting population analysis...')
            analyzingHousing = False
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    menu()
    
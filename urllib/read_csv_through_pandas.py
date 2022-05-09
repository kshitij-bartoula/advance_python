import pandas as pd

# Define the column names as a list
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
# Read in the CSV file from the webpage using the defined column names
df = pd.read_csv("adult.data", header=None, names=names)
                      
print(df.head())

#read csv ..
#  sep - this defaults to a comma, but we can specify anything we want. For example, CSV format is poor if some of your columns contain commas. A better option might be a |.
#   header - which row (if any) have the column names.
#    names - column names to use.

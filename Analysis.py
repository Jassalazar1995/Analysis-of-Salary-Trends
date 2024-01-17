import pandas as pd

# load the data
data = pd.read_csv('./jobs_in_data.csv')

# Identifies structure of the data
def data_organization(data):
    print('\nData structure and types\n')
    print(data.info())
    return

# Check for missing values
def missing_values(data):
    print('\nMissing values in each column:\n')
    print(data.isnull().sum())
    return

# Checks the columns have the same datatype
def check_datatype(data):
    are_same_type = len(set(data.dtype)) == 1
    print(f"All columns are of the same data type: {are_same_type}")
    return

# Sorts and filters data
def sort_and_filter(data):
    unique_job_titles = data['job_title'].unique()
    sorted_filtered_data_dict = {}

    for job_title in unique_job_titles:
        sorted_filtered_data_dict[job_title] = data[data['job_title'] == job_title].sort_values(by='salary_in_usd', ascending=False)
    print(sorted_filtered_data_dict)
    return 
# Creates a pivot table
def create_pivot_table(data):
    pivot_table = data.pivot_table(values = 'salary_in_usd', index='job_title', columns = 'experience_level', aggfunc='mean')
    print('\nPivot Table\n')
    print(pivot_table)
    return

#data_organization(data)
#missing_values(data)
#check_datatype(data)
sort_and_filter(data)
#create_pivot_table(data)
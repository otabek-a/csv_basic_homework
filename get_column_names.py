import csv
#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    reader=csv.reader(f)
    keyingi=next(reader)
    return keyingi
    
f=open("data.csv")
print(get_column_names("data.csv"))

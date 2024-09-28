import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV. 
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    reader=csv.reader(f)
    javob=next(reader)
    return len(javob)
    
f=open("data.csv")
print(find_number_of_columns("data.csv"))





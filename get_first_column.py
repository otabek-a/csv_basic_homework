import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    reader=csv.reader(f)
    javob=[]
    for row in reader:
        javob.append(row[0])
    return javob
    
f=open("data.csv")
print(get_first_column("data.csv"))
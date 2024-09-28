import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    reader=csv.reader(f)
    i=0
    javob=0
    for row in reader:
        javob+=1
    return javob

f=open("data.csv")
print(find_number_of_rows("data.csv"))



import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   reader=csv.reader(f)
   natija=next(reader)
   return natija

  

f=open("data.csv")
print(get_first_row("data.csv"))
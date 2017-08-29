####################################################################

######### Part 2 ################################


import csv
       
def calculate_profit(row):
  return int(row['Original Fico']) - int(row['Current Fico'])
 
def parser():
  with open('myfile5.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    # Create a dict reader from an open file
    # handle and iterate through rows.
    # The  rst interes ng line is redirect = csv.DictReader(open(opts.file, 'rU')). 
    # There are two things worth poin ng out on this line alone. 
    # First, we're opening the  le using Universal Newline support. 
    # This is because Excel will save the CSV  
    # file according to our pla orm's conven on. 
    # We want Python just to hide all of that for us here.
    # Secondly, we're crea ng an instance of csv.DictReader. 
    # The basic approach to accessing CSV data is via the csv.reader method. 
    # However, this requires us to access each row via an array index. 
    # The csv.DictReader class uses the  rst row in the CSV  le (by default) as the dic onary keys. 
    # This makes it much easier to access data by name.
  
    for row in reader:
      # print(row)
      print('{},{},{}'.format(row['First'], row['Last'], calculate_profit(row)))
parser()
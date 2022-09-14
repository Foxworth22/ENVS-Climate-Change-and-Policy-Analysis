# code template provided by GeeksforGeeks
# importing csv module
import csv
# csv file name
filename = "arctic-sea-ice-extent.csv"
# initializing the titles and rows list
fields = []
rows = []
# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	# extracting field names through first row
	fields = next(csvreader)
	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)
	# get total number of rows processed
	print("Total no. of rows: %d\n"%(csvreader.line_num))

# creating a variable for cummulative sum
cummulative_range = 0
cummulative_high = 0
for row in rows:
    # extracting interdecile values
    interdecile_range_low = row[4]
    interdecile_range_high = row[5]
    cummulative_range += float(interdecile_range_high) - float(interdecile_range_low)
    cummulative_high  += float(interdecile_range_high)
# outputing desired integration
print(str(cummulative_range) + " million km^2")
percent_decrease = cummulative_range/cummulative_high * 100
print(str(percent_decrease) + "%")
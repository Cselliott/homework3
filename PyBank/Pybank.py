#  creating a Python script for analyzing the financial records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# your task is to create a Python script that analyzes the records to calculate each of the following:
#    The total number of months included in the dataset
#    The net total amount of "Profit/Losses" over the entire period
#    The average of the changes in "Profit/Losses" over the entire period
#    The greatest increase in profits (date and amount) over the entire period
#    The greatest decrease in losses (date and amount) over the entire period

#==================================================================================================
#import
import os
import csv



#==================================================================================================
#set path
datafile = os.path.join('Resources/budget_data.csv')


#==================================================================================================
 #opens CSV file
with open(datafile) as csvfile:
    # Read  
    csvreader=csv.reader(csvfile,delimiter=',')
    # Initialize Variable
    months=0
    revenue=0
    # Count Total Rows
    rows=[r for r in csvreader]
    # First Value available  
    change_revenue=int(rows[1][1])
    max = rows[1]
    min=rows[1]
    #Loop  
    for i in range(1,len(rows)):
        
        months=months+1
        row=rows[i]
        revenue= int(row[1]) + revenue
        
        #Excludes the Header Row
        if i > 1:
            change_revenue=change_revenue + int(row[1])-int(rows[i-1][1])
        #Finding and Max Revenue
        if int(max[1]) < int(row[1]):
            max=row
        #Finding and Min Revenue
        if int(min[1]) > int(row[1]):
            min=row
#Calculating Average and the Change in Revenue
average= int(revenue /months)
average_change_revenue=int(change_revenue/months)





#==================================================================================================
# Print to screen the election results
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total Revenue: " +"$" +str(revenue))       
print("Average Revenue Change: " +"$"+ str(average))
print("Average Change in Revenue Change: " +"$"+ str(average_change_revenue))
print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")

print(datafile)

#==================================================================================================
# Output section 
output_file = datafile 
datafile = f"{output_file}pybank_results.txt"
# Open write file
filewriter = open(datafile, mode = 'w')
# Print write files
filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total months: {months}\n")
filewriter.write("Total Revenue: " +"$" +str(revenue)+"\n")       
filewriter.write("Average Revenue Change: " +"$"+ str(average)+"\n")
filewriter.write("Average Change in Revenue Change: " +"$"+ str(average_change_revenue)+"\n")
filewriter.write("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")"+"\n")
filewriter.write("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")


# Close file
filewriter.close()

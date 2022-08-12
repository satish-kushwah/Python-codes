file_name=input("Enter name of an input file containing voter participation data: ")
f=open(file_name,'r')
file_data=f.readlines();
i=0
total_ballots=0
total_avg_reg=0
lessThan60=0
moreThan80=0
fout=open("REPORT-"+file_name,'w')
while(i<len(file_data)):
	year=int(file_data[i])
	i=i+1
	total=int(file_data[i])
	i=i+1
	registered=int(file_data[i])
	i=i+1
	voted=int(file_data[i])
	total_ballots=total_ballots+voted
	i=i+1
	print("In %d, %.2f%c registered and %.2f%c voted" % (year,registered*100/total,'%',voted*100/total,'%'))
	fout.write("In %d, %.2f%c registered and %.2f%c voted\n" % (year,registered*100/total,'%',voted*100/total,'%'))
	total_avg_reg=total_avg_reg+round(registered*100/total,2)
	
	if(voted*100/registered<60):
		lessThan60=lessThan60+1
	if(voted*100/registered>80):
		moreThan80=moreThan80+1

print()
print("The total number of years listed: %d" % int(len(file_data)/4))
fout.write("\nThe total number of years listed: %d" % int(len(file_data)/4))
print("Total ballots cast in all these years:",f'{total_ballots:,}')
fout.write("\nTotal ballots cast in all these years: "+str(f'{total_ballots:,}'))
print("Average percentage of eligible voters registered: %.2f%c" % (total_avg_reg/(len(file_data)/4),'%'))
fout.write("\nAverage percentage of eligible voters registered: %.2f%c\n" % (total_avg_reg/(len(file_data)/4),'%'))
print("Number of years with less than 60% of registered voters casting ballots:",lessThan60)
fout.write("\nNumber of years with less than 60% of registered voters casting ballots: "+str(lessThan60))
print("Percentage of years with more than 80%c of registered voters casting ballots: %.2f%c" % ('%',moreThan80*100/(len(file_data)/4),'%'))
fout.write("\nPercentage of years with more than 80%c of registered voters casting ballots: %.2f%c" % ('%',moreThan80*100/(len(file_data)/4),'%'))
print("An output file named REPORT-"+file_name+" has been created.")
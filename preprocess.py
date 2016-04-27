import sys
import matplotlib.pyplot as plt

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) % 2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

def get_info_for_Department(department, all_data):
	#returns [count, avg_salary, median_salary]
	#all_data is in format [name, title, department, salary, basis, general fund]
	title_data = [t for t in all_data if department in t[2].lower()]
	sal_data = sorted(map(lambda x: float(x[3]), title_data))
	return {"department" : department, "count" : len(sal_data), "average" : float(sum(sal_data)) / len(sal_data), "median" : median(sal_data),
			"min" : min(sal_data), "max" : max(sal_data)}

def get_info_for_Title(title, all_data):
	#If the Title in the data contains this local variable title, it is included in the data.
	title_data = [t for t in all_data if title in t[1].lower()]
	sal_data = sorted(map(lambda x: float(x[3]), title_data))
	return {"title" : title, "count" : len(sal_data), "average" : float(sum(sal_data)) / len(sal_data), "median" : median(sal_data),
			"min" : min(sal_data), "max" : max(sal_data)}







sal_data = []
for line in open("salaries.txt", 'r'):
	line = line.replace('\n', '')
	lineData = line.split('   ')
	lineData = [x for x in lineData if x != '']
	if(len(lineData) > 4 and lineData[0] != '' and lineData[0] != "EMPLOYEE NAME" and not lineData[1].startswith("As of") and not lineData[0].startswith("As of")):
		entry = []
		for data in lineData:
			data = data.strip()
			#sys.stdout.write("'" + data + "'" + ',')
			entry.append(data)
			#sal_data.append([data[0], data[1], data[2], data[3], data[4], data[5], data[6]])
		sal_data.append(entry)

sorted_sal_data = sorted(sal_data, key=lambda x: float(x[3]))


salaries = [float(t[3]) for t in sorted_sal_data]
cs_data = [t for t in sorted_sal_data if "computer" in t[2].lower()]

departments = [t[2] for t in sal_data]
departments_set = set([t[2] for t in sal_data])
#departments_sorted_by_freqency = sorted(departments, key=)
# print list(departments_set)[60]
# print list(departments_set)[49]
# print list(departments_set)[48]
#
# print list(departments_set)[38]
# print list(departments_set)[19]
# print list(departments_set)[2]
uValues = list(set(departments))
xVals = range(0, len(uValues))
yVals = map(lambda x: departments.count(uValues[x]), xVals)
departments_frequencies = sorted(map(lambda x: [departments.count(uValues[x]), uValues[x]], xVals), key = lambda j: j[0])
# print get_info_for_Title("professor", sal_data)
# print get_info_for_Title("lecturer", sal_data)
# print get_info_for_Title("cook", sal_data)
# print get_info_for_Title("president", sal_data)
# print get_info_for_Title("engineer", sal_data)
# print get_info_for_Title("senior", sal_data)
# print get_info_for_Title("research", sal_data)

print get_info_for_Department("computer", sal_data)
# for i in range(-10, 0):
# 	print departments_frequencies[i]
# import pylab
# pylab.bar(xVals, yVals)
# pylab.show()
# print "hehre"
#print cs_data
#print sum(cs_salaries) / float(len(cs_salaries))
# plt.hist(salaries, 100)
# plt.title("Michigan Tech Salary Distribution")
# plt.xlabel("Salary")
# plt.ylabel("Frequency")
# plt.show()
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


def insertAllDataIntoDatabase(all_data, db_name):
	import sqlite3
	conn = sqlite3.connect("sal_data")
	c = conn.cursor()
	#c.execute("create table employee(name text, title text, department text, salary real, primary key(name, title, department));")
	for dataPt in all_data:
		command = 'insert into employee(name, title, department, salary) values("%s", "%s", "%s", %s);'%(dataPt[0], dataPt[1], dataPt[2], dataPt[3])
		c.execute(command)
	conn.commit()
	conn.close()

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

def getSalariesForDepartment(dep, level):
	salaries = [float(t[3]) for t in sorted_sal_data if dep.lower() in t[2].lower()]
	lev = [level for t in salaries]
	return [salaries, lev]

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

#insertAllDataIntoDatabase(sal_data, "hello")


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

for i in range(-10, 0):
	print departments_frequencies[i]
# import pylab
# pylab.bar(xVals, yVals)
# pylab.show()
# print "hehre"
#print cs_data
#print sum(cs_salaries) / float(len(cs_salaries))
plt.hist(salaries, 100)
plt.title("Michigan Tech Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

information_technology_salaries = [float(t[3]) for t in sorted_sal_data if "Information Technology".lower() in t[2].lower()]
facilities_management_salaries = [float(t[3]) for t in sorted_sal_data if "Facilities Management".lower() in t[2].lower()]
info_tech_level = [1 for t in information_technology_salaries]
facil_man_level = [2 for t in facilities_management_salaries]
# print information_technology_salaries
# plt.scatter(information_technology_salaries, info_tech_level)
# plt.show()


# fig = plt.figure()
# ax1 = fig.add_subplot(111)
##CD93D2
colors = ["#CD93D2","#70C641", "#CD6BD6", "#CAAA32", "#737EDD", "#618731", "#D84894", "#49B47B","#DB512F","#3DAAB6","#D64C5D","#6489BB","#B67031","#8E5B99", "#BA5F7A"]
colors2 = ["#8C4500","#405CC5","#3DC318","#B380EC","#8DAB3E","#302664","#E09237","#1699E0","#870237","#032B3D","#F084A9","#3A2717"]
# for i in range(-10, 0):
# 	dep_name = departments_frequencies[i][1]
# 	dep_info = getSalariesForDepartment(dep_name, abs(i))
# 	ax1.scatter(dep_info[0], dep_info[1], s=100, c=colors[abs(i)], marker="s", label=dep_name)
#
# ax1.set_ylim([-5,11])
#
# # ax1.scatter(information_technology_salaries, info_tech_level, s=10, c='b', marker="s", label='Information Technology')
# # ax1.scatter(facilities_management_salaries,facil_man_level, s=10, c='r', marker="o", label='Facilites Management')
# fig.suptitle('Salary Distribution', fontsize=20)
# plt.xlabel('Salary', fontsize=18)
# plt.ylabel('Department', fontsize=16)
# plt.legend(loc='lower right');
# plt.show()

sets = []
dep_names = []
for i in range(-10, 0):
	dep_name = departments_frequencies[i][1]
	dep_names.append(dep_name)
	dep_info = getSalariesForDepartment(dep_name, abs(i))
	sets.append(dep_info[0])
	#ax1.scatter(dep_info[0], dep_info[1], s=100, c=colors[abs(i)], marker="s", label=dep_name)

plt.figure()
plt.hist(sets,bins=100, stacked=True, color=colors2[:len(sets)], label=dep_names)
plt.legend(prop={'size': 15})
plt.show()


import sys
import matplotlib.pyplot as plt

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
print()

print(sorted_sal_data[len(sorted_sal_data) - 4])
print(sorted_sal_data[len(sorted_sal_data) - 3])
print(sorted_sal_data[len(sorted_sal_data) - 2])
print(sorted_sal_data[len(sorted_sal_data) - 1])

salaries = [float(t[3]) for t in sorted_sal_data]

plt.hist(salaries)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
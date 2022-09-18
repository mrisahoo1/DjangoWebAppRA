# example file

import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data/hi.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
  
plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Returns')
# plt.title('Ages of different persons')s
plt.legend()
plt.show()
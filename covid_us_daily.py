import requests
import matplotlib.pyplot as plt

'''
Data Source
https://covidtracking.com/data/api
'''

r = requests.get('https://api.covidtracking.com/v1/us/daily.json')
d = r.json()
dates = []
death = []
for i in range(len(d)):
  if d[i]['death'] != None:
    dates.append(i)
    death.append(d[i]['death'])
    print(d[i]['death'])
death.reverse()
plt.yscale('log') 
plt.plot(dates, death)
plt.show()
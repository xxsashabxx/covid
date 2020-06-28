import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.tsa.gov/coronavirus/passenger-throughput"

r = requests.get(url)

data = pd.read_html(r.text, header =0)
l = data[0]

l.columns = ['Date', 'Throughput', 'Throughput_lastyear']
l['Percent of Previous Year Throughput'] = l.Throughput/l.Throughput_lastyear

df = pd.DataFrame(l, columns=['Date', 'Throughput', 'Throughput_lastyear', 'Percent of Previous Year Throughput'])
df['Date']=pd.to_datetime(df['Date'])

df.plot(x = 'Date', y = 'Percent of Previous Year Throughput', kind = 'line', title='Change in Passenger Throughput During the COVID-19 Pandemic')

plt.show()
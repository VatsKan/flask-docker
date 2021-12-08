import pandas, moment, datetime

data = pandas.read_csv('testdata.csv')
time_sales_data = data[['Time', 'Sales']]
time_ranges = [
'2019-12-14 11:10',
'2019-12-14 11:15',
'2019-12-14 11:20',
'2019-12-14 11:25',
'2019-12-14 11:30', 
'2019-12-14 11:35'
]

def getSales():  
  sales = {}
  for index in range(len(time_ranges)-1):
    start = moment.date(time_ranges[index]).date 
    end = moment.date(time_ranges[index+1]).date
    total_sales = 0
    for row in time_sales_data.iterrows():
      time_str = row[1]['Time']
      sale = row[1]['Sales']
      timestamp = moment.date(time_str).date
      if start <= timestamp < end:
        total_sales += sale
    sales[start.strftime("%H:%M")] = total_sales
  return sales
  
  
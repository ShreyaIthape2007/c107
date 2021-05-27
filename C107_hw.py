import csv
import pandas as pd
import plotly.express as pt


file = pd.read_csv('data2.csv')

studentdata = file.groupby(['student_id','level'],as_index=False)['attempt'].mean()

print(studentdata)




graph = pt.scatter(studentdata,x='student_id',y='level',size='attempt',color='attempt')

graph.show()



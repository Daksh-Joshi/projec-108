import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["(Note : This parameter denotes the name of the bell-curve which we plotted)"], show_hist=False)
fig.show()
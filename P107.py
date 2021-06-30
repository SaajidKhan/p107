import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv("STUDENT2.csv")
print(df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Scatter(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation='h'
))
fig.show()

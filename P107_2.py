import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv("STUDENT2.csv")
stud_df=df.loc[df["student_id"]=="TRL_abc"]
print(stud_df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Scatter(
    x=stud_df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation='h'
))
fig.show()
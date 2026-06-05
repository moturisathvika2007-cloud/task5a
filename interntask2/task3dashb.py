import pandas as pd
import plotly.express as px

df = pd.read_excel("apextask3.xlsx")

fig = px.scatter(
    df,
    x="Experience_Years",
    y="Salary",
    color="Department",
    size="Performance_Score",
    hover_name="Name",
    title="Interactive Experience vs Salary Dashboard"
)

fig.show()
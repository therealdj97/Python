import plotly.express as px
import pandas as pd
import numpy as np
#scatter plots
#creating figure instance
#x=y=[1,2,3]
#fig = px.line(x,y)
fig=px.scatter(x=np.array([0,1,2,3,4]),y=np.array([0,1,4,9,16]))
fig.show()
#printing the figure instance
#print(fig)
#fig.show()
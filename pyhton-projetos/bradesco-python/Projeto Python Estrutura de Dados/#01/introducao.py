
import pandas as pd

# o objeto Series é um tpo array inidimensional

series_objeto = pd.Series([1,7,9,13,17,99])
series_objeto
print(series_objeto)

series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])
print(series_objeto2)

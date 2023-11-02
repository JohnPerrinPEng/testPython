import pandas as pd
url = 'https://en.wikipedia.org/wiki/History_of_Python'
dfs = pd.read_html(url)
print(len(dfs))
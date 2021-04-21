import pandas as pd

# Read the 'cities.csv' file
df = pd.read_csv('Resources/cities.csv')

# Save df to html, and save it into a table
df.to_html('data.html', index=False)

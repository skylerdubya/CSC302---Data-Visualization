from google.colab import drive
drive.mount('/content/drive/')
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/DATA/causes_of_death.csv')

# 3a
print("3a - Number of rows and columns (format: (rows,columns) )")
df.shape

# 3b 
print("3b - Average death rate across country")
df['Deaths'].mean()

# 3c
deaths = df.groupby('State').sum()
print('3c - Total death count per state:')
deaths['Deaths']

# 3d
avg_deaths = df.groupby('State').mean()
print('3d - Average death count per state:')
avg_deaths['Deaths']

# 3e 
deaths_by_gender = df.groupby(['Gender','State']).sum()
print('3e - Deaths for each gender per state:')
deaths_by_gender['Deaths']

# 3f
print('3f - Drop NA columns:')
df.dropna()

# 3g
print('3g - Create ratio column and assign death:population ratios')
df['ratio'] = (df['Deaths'] / df['Population'])
df.head()

# 3h
print('3h - View rows with Ten-Year Age Groups Code = 1')
df[df['Ten-Year Age Groups Code']=="1"]

# 3i
print('3i - View rows with Ten-Year Age Groups Code = 1, sorted by highest Crude Rate')
df[df['Ten-Year Age Groups Code']=="1"].sort_values('Crude Rate',ascending=False)

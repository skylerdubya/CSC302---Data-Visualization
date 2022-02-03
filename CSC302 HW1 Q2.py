from google.colab import drive
drive.mount('/content/drive/')
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/DATA/olympic_medals.csv')

# 2a
# uses DataFrame attribute .shape to show row+column count in format (row,column)
print("2a - Rows and columns in this dataset:")
print(df.shape)

# 2b
print("2b - All data types per column:")
print(df.dtypes)

# 2c
print("2c - Unique locations:")
locations = df['Location'].unique()
print(locations)

# 2d
df['Nationality'].unique()
USA_wins = df.loc[df['Nationality']=='USA', 'Medal']
print("2d - USA medals:")
print(len(USA_wins))

# 2e
print("2e - Medals won per nationality")
medals_and_nationalities = df.groupby('Nationality').count()
medals_and_nationalities['Medal']from google.colab import drive
#drive.mount('/content/drive/')
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/DATA/olympic_medals.csv')

# 2a
# uses DataFrame attribute .shape to show row+column count in format (row,column)
print("2a - Rows and columns in this dataset:")
print(df.shape)

# 2b
print("2b - All data types per column:")
print(df.dtypes)

# 2c
print("2c - Unique locations:")
locations = df['Location'].unique()
print(locations)

# 2d
df['Nationality'].unique()
USA_wins = df.loc[df['Nationality']=='USA', 'Medal']
print("2d - USA medals:")
print(len(USA_wins))

# 2e
print("2e - Medals won per nationality")
medals_and_nationalities = df.groupby('Nationality').count()
medals_and_nationalities['Medal']

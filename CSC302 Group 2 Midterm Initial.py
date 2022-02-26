import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joypy as jp
from google.colab import drive
drive.mount('/content/drive')

df_credits = pd.read_csv('/content/drive/My Drive/CSC 302 Files/tmdb_5000_credits.csv')
df_movies = pd.read_csv('/content/drive/My Drive/CSC 302 Files/tmdb_5000_movies.csv')

# Do the top 50 "long" movies (> 140 minutes) generate more revenue than the top 50 "short" movies (<140 minutes)? [double bar graph]
df_length = df_movies
df_length['profit'] = df_length['revenue'] - df_length['budget']
df1 = df_length.loc[df_length['runtime']>140].sort_values('profit', ascending = False).head(50)
df2 = df_length.loc[df_length['runtime']<=140].sort_values('profit', ascending = False).head(50)
 
df2['profit'].mean() # 727449765.46
df1['profit'].mean() # 724420375.76

sns.lineplot('runtime', 'profit', data=df1)
sns.lineplot('runtime', 'profit', data=df2)


# Were the classics really better? (Show histogram of ratings over time)
from matplotlib import cm

df_classics = df_movies

df_classics['release_date'] = pd.to_datetime(df_classics['release_date'])
df_classics['release_date'] = df_classics['release_date'].dt.strftime('%Y')

fig, axes = jp.joyplot(df_classics, by='release_date', column='vote_average', range_style='own', 
                          grid="y", linewidth=1, legend=False, figsize=(6,14),
                          title="Average movie ratings per year (scale of 1 to 10)", colormap=cm.summer_r
                          )

#Does genre have an effect on revenue
import matplotlib.pyplot as plt

df_genrev = df_movies

plt.scatter(x=df_genrev['genres'], y=df_genrev['revenue'])
plt.xlabel('Genre')
plt.ylabel('Revenue')
plt.title('Genres Effects on Revenue')

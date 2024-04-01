from data import yt_results_to_df as yt_to_df
from data import google_trends
from itertools import product
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import grangercausalitytests

# Load YouTube results data, I c
yt_res_df = yt_to_df.yt_results_to_df('data/youtube_results/Massimo Dutti Pants')

# Extract date components
yt_res_df['Fecha'] = pd.to_datetime(yt_res_df['Video_Timestamp']).dt.date
yt_res_df['Semana'] = pd.to_datetime(yt_res_df['Video_Timestamp']).dt.isocalendar().week
yt_res_df['Month'] = pd.to_datetime(yt_res_df['Video_Timestamp']).dt.month
yt_res_df['Year'] = pd.to_datetime(yt_res_df['Fecha']).dt.year

# Obtain unique years and months in the dataset
años_únicos = yt_res_df['Year'].unique()
meses_únicos = yt_res_df['Month'].unique()

# Create all possible combinations of years and months
combinaciones = list(product(años_únicos, meses_únicos))

# Create a DataFrame with all combinations
combinaciones_df = pd.DataFrame(combinaciones, columns=['Year', 'Month'])

# Merge the original DataFrame with the combinations, filling missing values with 0
yt_res_df = pd.merge(combinaciones_df, yt_res_df, how='left', on=['Year', 'Month']).fillna(0)
yt_res_df['YearMonth'] = yt_res_df['Year'].astype(str) + '-' + yt_res_df['Month'].astype(str).str.zfill(2)

# Group by year and month
videos_por_mes_df = yt_res_df.groupby('YearMonth').size().reset_index(name='Number of videos')

# Initialize scaler
scaler = MinMaxScaler()

# Rescale the number of videos
videos_por_mes_df['Number of videos'] = scaler.fit_transform(videos_por_mes_df[['Number of videos']])

# Fetch Google Trends data
timeframe = '2022-01-01 2023-12-31'
kw_list = ["Massimo Dutti pants"]
go_df = google_trends.get_google_trends_data(kw_list, timeframe)
go_df['Semana'] = pd.to_datetime(go_df['date']).dt.isocalendar().week
go_df['Month'] = pd.to_datetime(go_df['date']).dt.month
go_df['Year'] = pd.to_datetime(go_df['date']).dt.year

# Group by year and month
suma_por_mes = go_df.groupby(['Year', 'Month'])[kw_list].sum().reset_index()
suma_por_mes['YearMonth'] = suma_por_mes['Year'].astype(str) + '-' + suma_por_mes['Month'].astype(str).str.zfill(2)

# Rescale Google Trends data
suma_por_mes['Google Searches'] = scaler.fit_transform(suma_por_mes[kw_list])

# Merge YouTube and Google Trends data
merged_df = pd.merge(videos_por_mes_df, suma_por_mes, on=['YearMonth'])

# Calculate the covariance matrix
covariance_matrix = merged_df[['Number of videos', 'Google Searches']].cov()

# Compute the correlation coefficient
correlation_coefficient = merged_df['Number of videos'].corr(merged_df['Google Searches'])
print("Correlation coefficient")
print(correlation_coefficient)

# Visualize the covariance matrix and print the correlation coefficient
plt.figure(figsize=(8, 6))
sns.heatmap(covariance_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})
plt.title('Covariance Matrix between YouTube Videos and Google Searches')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Actualizar para usar 'MonthYear'
sns.boxplot(x='YearMonth', y='Number of videos', data=videos_por_mes_df, ax=axes[0])
axes[0].set_title('YouTube Videos')
axes[0].tick_params(labelrotation=45)  # Rotar las etiquetas para mejor visualización
axes[0].set_xlabel('Number of videos posted containing keyword')

sns.boxplot(x='YearMonth', y='Google Searches', data=suma_por_mes, ax=axes[1])
axes[1].set_title('Google Trends')
axes[1].tick_params(labelrotation=45)  # Rotar las etiquetas para mejor visualización
axes[1].set_ylabel('Search volumne for Massimo Dutti pants')

plt.tight_layout()
plt.show()

#Youtube and google search plots
videos_por_mes_df['YearMonth'] = pd.to_datetime(videos_por_mes_df['YearMonth'])
videos_por_mes_df = videos_por_mes_df.sort_values('YearMonth')
suma_por_mes['YearMonth'] = pd.to_datetime(suma_por_mes['YearMonth'])
suma_por_mes = suma_por_mes.sort_values('YearMonth')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=videos_por_mes_df, x='YearMonth', y='Number of videos', marker='o', label='YouTube Videos', ax=ax)
sns.lineplot(data=suma_por_mes, x='YearMonth', y='Google Searches', marker='x', label='Google Searches', ax=ax)
ax.set_title('YouTube Videos vs Google Searches')
ax.tick_params(axis='x', rotation=45)
ax.set_ylabel('Video Count / Search Volume')
ax.set_ylim(0, max(videos_por_mes_df['Number of videos'].max(), suma_por_mes['Google Searches'].max()) * 1.1)

plt.legend()
plt.tight_layout()
plt.show()

#csv file with 3 columns, date, youtube numbers, google numbers, load this in pandas, translate 2 columns of youtube in 2 lists of numbers
#lists are the same length, 

merged_df2 = pd.merge(videos_por_mes_df , suma_por_mes, on=['YearMonth']) 
print("MERGED DF2")
print(merged_df2)

print (len(merged_df2) // (2*2), "primero",len(merged_df) )

import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

# Assuming your DataFrame is named merged_df2
data_for_granger = merged_df2[['Number of videos', 'Google Searches']]

max_lags = 3
  # Adjusted based on your dataset size

# Perform Granger causality test without specifying 'test' argument
granger_result_videos_predict_normalized = grangercausalitytests(data_for_granger, max_lags, verbose=True, addconst=True)
granger_result_normalized_predict_videos = grangercausalitytests(data_for_granger[['Google Searches', 'Number of videos']], max_lags, verbose=True, addconst=True)

# Interpretation guide remains the same
print("\nInterpretation:")
print("If the P-value is less than a significance level (commonly 0.05), then we reject the null hypothesis and conclude that the first series Granger-causes the second series.")

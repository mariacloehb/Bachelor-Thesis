from data import yt_results_to_df as yt_to_df
from data import google_trends
import pandas as pd
yt_res_df = yt_to_df.yt_results_to_df('data/youtube_results/adidas gazelle_2022-01-01_2022-05-01.json')
yt_res_df['Fecha'] = pd.to_datetime(yt_res_df['Video_Timestamp']).dt.date
yt_res_df['Semana'] = pd.to_datetime(yt_res_df['Video_Timestamp']).dt.isocalendar().week
yt_res_df['Year'] = pd.to_datetime(yt_res_df['Fecha']).dt.year

# Elimina la columna original 'Video_Timestamp' si ya no la necesitas
yt_res_df = yt_res_df.drop(columns=['Video_Timestamp'])
print(yt_res_df)

timeframe='2022-01-01 2023-01-12'
kw_list = ["ganni blouse"]
go_df = google_trends.get_google_trends_data(kw_list,timeframe)
go_df['Semana']= pd.to_datetime(go_df['date']).dt.isocalendar().week
go_df['Year'] = pd.to_datetime(go_df['date']).dt.year
print("Hole", go_df)


merged_df = pd.merge(yt_res_df, go_df, on=['Year', 'Semana'])  # Puedes ajustar 'how' según tus necesidades

# Imprimir el DataFrame resultante
print(merged_df)


# Calcular la matriz de covarianza
covariance_matrix = merged_df.cov()

# Imprimir la matriz de covarianza
print("Matriz de Covarianza:")
print(covariance_matrix)












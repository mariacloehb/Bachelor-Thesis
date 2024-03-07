import pandas as pd
import json
def yt_results_to_df(filePath= 'youtube_results/adidas gazelle_2022-01-01_2022-05-01.json') : 
    with open(filePath, 'r') as file:
        data = json.load(file)

    # Convierte los datos a un DataFrame
    df = pd.json_normalize(data['items'])

    return df


#normalizar los dos resultados antes de hacer correlacion

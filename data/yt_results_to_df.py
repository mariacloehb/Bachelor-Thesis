import pandas as pd
import json
import os
def yt_results_to_df(carpetaPath= 'data/youtube_results') : 

    total_data= []
    for archivo in os.listdir(carpetaPath):
        if archivo.endswith('.json'): 
            ruta_completa = os.path.join(carpetaPath, archivo)

            #Read content of Json files
            with open(ruta_completa, 'r') as file:
                datos_json = json.load(file)
                total_data.append(datos_json)
    

    if total_data:
        # Joining all elements of the list in a joint dataframe
        df = pd.concat([pd.json_normalize(datos['items']) for datos in total_data], ignore_index=True)
        return df
    else:
        #Error control, if no content, return empty df
        return pd.DataFrame()

    return df




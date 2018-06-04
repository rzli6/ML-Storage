import numpy as np
import pandas as pd
import os

data_dir = "./data/data_Q1_2018/"

Hit_features = ['serial_number', 'date', 'smart_1_normalized', 'smart_1_raw', 'smart_3_normalized', 'smart_3_raw', 'smart_5_normalized', 'smart_5_raw', 
    'smart_194_normalized', 'smart_194_raw', 'smart_196_normalized', 'smart_196_raw', 'smart_197_normalized', 'smart_197_raw', 'failure']
    
Sgt_features = ['serial_number', 'date', 'smart_1_normalized', 'smart_1_raw', 'smart_5_normalized', 'smart_5_raw', 'smart_7_normalized', 'smart_7_raw',
    'smart_184_normalized', 'smart_184_raw', 'smart_187_normalized', 'smart_187_raw', 'smart_188_raw', 'smart_189_normalized', 'smart_189_raw', 
    'smart_190_normalized', 'smart_190_raw', 'smart_193_normalized', 'smart_193_raw', 'smart_194_normalized', 'smart_194_raw', 'smart_197_normalized', 
    'smart_197_raw', 'smart_198_normalized', 'smart_198_raw', 'smart_240_raw', 'smart_241_raw', 'smart_242_raw', 'failure']

models_dir = {
    'SgtA': {
        'name': 'ST4000DM000',
        'features': Sgt_features
    },

    'SgtB': {
        'name': 'ST31500541AS',
        'features': Sgt_features
    }, 

    'HitA': {
        'name': 'Hitachi HDS722020ALA330',
        'features': Hit_features
    },

    'HitB': {
        'name': 'Hitachi HDS5C3030ALA630',
        'features': Hit_features
    }    
}

def process(df, model):
    df = df.loc[df['model'] == model['name']]
    return df[model['features']]
    
def process_data():
    for model_key, model in models_dir.items():
        pd.concat([process(pd.read_csv(os.path.join(data_dir, filename)), model) for filename in os.listdir(data_dir)]) \
            .sort_values('date', ascending=True).groupby('serial_number', as_index=False).apply(lambda feature: feature.astype(str).apply(lambda x: ','.join(x))).reset_index() \
            .drop(['serial_number', 'date'], axis=1).to_csv(os.path.join('./data', model_key + '.csv'))
            
def find_failures():
    pass

def changepoint_detect():
    pass

if __name__ == "__main__":
    process_data()
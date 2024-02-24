# %% [markdown]
# # Imports

# %%
import pandas as pd
import json

# %% [markdown]
# # Clean

# %%
df = pd.read_json('devices.json')

df = df.sort_values(by=['name'], key=lambda x: x.str.lower())

df = df.reset_index().drop(columns=['index'])

df = df[['name', 'id', 'key', 'mac']]

df['mac'] = df['mac'].str.upper()

df.head()

# %% [markdown]
# # Export to `json` file

# %%
filename = "tuya-devices"

def export_df_to_json(df_filtered, tag=None):
    with open(filename + '.json', 'w') as json_file:
        json.dump(json.loads(df_filtered.to_json(orient='records')), json_file, indent=4)
        print('\"' + filename + '.json' + '\"' + ' created or customized!')

export_df_to_json(df)
print(str(len(df)) + ' devices found!')



# %%
import pandas as pd 
import os 
import pathlib
# pd.set_option("display.max_rows", 100)

from sudulunu.helpers import pp, make_num, dumper
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder

# %%



pathos = pathlib.Path(__file__).parent
os.chdir(pathos)


#%%

def combine_from_folder(stemmo, pathos):
  
    listo = []

    foldos = os.listdir(pathos)

    foldos = [pathos + x for x in foldos if x != '.DS_Store']
    for foldo in foldos:
        fillos = os.listdir(foldo)
        fillos = [foldo + '/' + x for x in fillos if x != '.DS_Store']
        fillos = [x for x in fillos if stemmo in x]
        # print(fillos)
        for fillo in fillos:
            # print(fillo)

            inter = pd.read_csv(fillo)
            # inter['City'] = stemmo

            listo.append(inter)

    cat = pd.concat(listo)

    return cat

for city in ['Adelaide', 'Brisbane', 'Canberra', 'Hobart', 'Melbourne', 'Perth', 'Sydney']:

    print(city)
    data = combine_from_folder(city, 'data/raw/')

    df = data.copy()

    # print(len(df))
    df.sort_values(by=['Date'], ascending=False, inplace=True)
    timeo = [x for x in df.columns.tolist() if "time" in x.lower()][0]
    df.drop_duplicates(subset=[timeo, 'Date'], keep='first', inplace=True)

    print(len(df))

    # print(df['Date'].min())
    # print(df['Date'].max())

    dumper('data', city, df)
# pp(df)


#%%
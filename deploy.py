# importing the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# reading all the files neccesary
## model_df, apps_data, engineered_data, saved_model
ASSETS_DIRECTORY = "assets"

# has genres and appId's for the entirely fetched apps.
apps_data = pd.read_csv(f"{ASSETS_DIRECTORY}/apps_data.csv")
# to have a cleaned data.
engineered_apps_data = pd.read_csv(
    f"{ASSETS_DIRECTORY}/engineered_apps_data.csv")
# st.write(engineered_apps_data.head())
# has all the standardised data which goes into the model training.
model_df = pd.read_csv(f"{ASSETS_DIRECTORY}/Model_df.csv")
# st.write(model_df.head())
# importing the saved model to execute predictions


# Giving a title for the App.
st.title('A dive into the Google Playstore!!')

# Get the caption
st.caption('Get your app recommendations by answering few questions.')

# writing the input fields to get the information from the user
# selecting genres
options = st.multiselect(
    'What are your favorite genres?',
    list(apps_data.genre.unique()))

# radio button to choose between free or paid apps --> try using Model_df for reference
amount_bool = st.radio(
    "Preferred type of app",
    ('Free', 'Paid'),
    horizontal=True)
if amount_bool == 'Free':
    amount_bool = 1
else:
    amount_bool = 0

# give the range for number of installs
min_installs = st.radio(
    "What do you want the minimum number of installs to be?",
    ('100K', '10M', '100M', '1B'),
    horizontal=False)
if min_installs == '100K':
    min_installs = 100000
elif min_installs == '10M':
    min_installs = 10000000
elif min_installs == '100M':
    min_installs = 100000000
else:
    min_installs = 10000000000

# list of apps to select
genre_list, free, installs = [], 0, 0
if options:
    genre_list = options
    free = amount_bool
    installs = min_installs
# empty temporary dataframe
temp_df = pd.DataFrame([], columns=engineered_apps_data.columns)
for i in range(len(genre_list)):
    a = engineered_apps_data[engineered_apps_data['genre'] == genre_list[i]]
    b = a[a['free'] == free]
    c = b[b['installs'] >= installs]
    d = c.sort_values('score', ascending=False).head(5)
    temp_df = pd.concat([temp_df, d], ignore_index=True, axis=0)

options = st.multiselect(
    'Select few apps from the below list?',
    list(temp_df.title))
st.write(list(temp_df.title))

# getting the top rated apps with the above filters from the Model_df.csv
# our dataframe here is named as model_df.


# querying the necessary data or mapping

# give the most important field of selecting apps of the users choice
# the options must be given based on the querying from the above fields

# load the saved model

# get or query the necessary arguments for the predict method to work 1,000,000


# df = pd.read_csv('assets/engineered_apps_data.csv')
# st.write(df.head())
# df_apps = pd.read_csv('assets/apps_data.csv')
# st.write(df.installs.max(), df.installs.min())
# st.write('You selected:', options)

# '''
#     genre -- multiple options,
#     free or paid -- radio button,
#     number of installs -- range using two slidbars,
#     which app would you likely try or have tried and liked from the above selected genres? -- multiple selections,

#     give out the top recomendation and show it's details.
# '''

# inputs ===> genres, free_or_paid, installs, apps.
# 1) predict args ====> {
#     select the chosen appId,
#     get the number for the appId selected from the apps_dict,

# },
# { userId === fix it to 1000 },
# { features ===> from the appIds, fetch ( load model_df take reference from the notebook and call the necesary columns and pass it as an array. ) }

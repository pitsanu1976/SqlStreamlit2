import sqlite3
import csv
import streamlit as st 
import pandas as pd

#st.write('Hi Pitsanu')
conn = sqlite3.connect('PMDB.db')
df_pmbom = pd.read_csv('Maintenance_BOM_Listing_1.csv')

df_rout = pd.read_csv('Maintenance_Routing.csv')

df_pm_sch = pd.read_csv('PM_Schedule.csv')

df_pmbom.to_sql(
    name='pmbom',
    con=conn,
    if_exists='replace',
    index = False,
    dtype={
        'Field':'text',
        'Activity':'text',
        'Activity Description':'text',
        'Operation Seq':'integer',
        'Component':'integer',
        'Component Description':'text',
        'UOM':'text',
        'Quantity':'numeric'
    }
)
df_rout.to_sql(
    name='rout',
    con=conn,
    if_exists='replace',
    index = False,
    dtype={
        'Field':'text',
        'Activity':'text',
        'RowID':'integer',
        'Activity Description':'text',
        'Reporting Name':'text',
        'Operation Seq':'integer',
        'Department Code':'text',
        'Long Description':'text',
        'Required / Std Spec':'text'
    }
)
df_pm_sch.to_sql(
    name='pm_sch',
    con=conn,
    if_exists='replace',
    index = False,
    dtype={
        'Field':'text',
        'RowID':'integer',
        'Schedule Name':'text',
        'Asset Route Flag':'text',
        'Asset Number':'text',
        'Asset Description':'text',
        'Asset Group':'text',
        'Asset Group Description':'text',
        'Activity':'text',
        'Activity Department':'text',
        'SCE':'text'
    }
)

Field = st.radio('Field',options=['JAS','G1','G10','G11'],key='field')
#Field = st.session_state.field
df = pd.read_sql('''
SELECT DISTINCT pm_sch.Field, pm_sch.[Asset Number], pm_sch.[Asset Description]
FROM pm_sch
WHERE pm_sch.Field = :Field
''',
conn,params={'Field':Field})  
st.write('Table Asset')
st.dataframe(df)




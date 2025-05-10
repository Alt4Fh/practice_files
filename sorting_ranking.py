

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return np, pd


@app.cell
def _(pd):
    df = pd.read_csv('emp1.csv')
    return (df,)


@app.cell
def _(df):

    ## striping spaces from strings of each column
    df.columns = df.columns.str.strip()
    for column in list(df.columns):
        if df[column].dtype == 'object':
            df[column] = df[column].str.strip()

    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.sort_values(by='Sales', ascending=False)
    return


@app.cell
def _(df):
    df.sort_values(by='Department').sort_values(by='Sales', ascending=False)
    return


@app.cell
def _():
    ##  delete column -> df.drop('SalesRank_Dense', axis=1)



    return


@app.cell
def _(df):
    df['SalesRank_Dense'] = df['Sales'].rank(method='dense')
    return


@app.cell
def _(pd):
    new_row = pd.DataFrame( {'EmployeeID': [11], 'Name': ['jonothan'], 'Department': ['Sales'], 'Region': ['North'], 'Sales': [30000], 'Month': ['feburary'], 'Year': [2024]})

    return (new_row,)


@app.cell
def _(new_row):
    new_row
    return


@app.cell
def _(df, new_row, pd):
    df_new = pd.concat([df, new_row], ignore_index=True)
    return (df_new,)


@app.cell
def _(df_new):
    df1 = df_new.drop('SalesRank_Dense', axis=1)
    return (df1,)


@app.cell
def _(df1):
    df1['SalesRank_Dense'] = df1['Sales'].rank(method='dense')
    return


@app.cell
def _(df1):
    df1['SalesRank_Dense']
    return


@app.cell
def _(df1):
    df1['Sales'].rank(method='first')
    return


@app.cell
def _(df1):
    df1['Dep_avgRank']= df1.groupby('Department')['Sales'].rank(method='average', ascending=False)
    return


@app.cell
def _(df1):
    df1.sort_values(by=['Department', 'Sales'], ascending=[True, False])[0:3]
    return


@app.cell
def _(df1):
    df1['RegionWiseRank'] = df1.groupby('Region')['Sales'].rank(method='min', ascending=False)
    return


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df1):
    ## highest and lowest sale employee in each department
    ## max sales
    df1.loc[df1.groupby('Department')['Sales'].idxmax()][['Department', 'Name', 'Sales']]

    return


@app.cell
def _(df1):
    ## sales min
    df1.loc[df1.groupby('Department')['Sales'].idxmin()][['Department', 'Name', 'Sales']]
    return


@app.cell
def _(df1):
    df1['SalesRank_Min'] = df1['Sales'].rank(method='min', ascending=False)
    return


@app.cell
def _(df1):
    df1['SalesRank_Min']
    return


@app.cell
def _(df):

    df_with_nan = df.copy()
    return (df_with_nan,)


@app.cell
def _(df_with_nan, np):
    df_with_nan.loc[df_with_nan['Name'] == 'Eve', 'Sales'] = np.nan
    return


@app.cell
def _(df_with_nan):
    df_with_nan
    return


@app.cell
def _(df_with_nan):
    df_with_nan.sort_values(by="Sales", na_position='first')
    return


@app.cell
def _(df):
    df.loc[df.groupby('Region')['Sales'].idxmax()]
    return


@app.cell
def _(pd):
    df_sen = pd.read_csv('sensor_data.csv')
    return (df_sen,)


@app.cell
def _(df_sen):
    df_sen.columns = df_sen.columns.str.strip()
    return


@app.cell
def _(df_sen):
    df_sensor = df_sen.apply(lambda x: x.strip() if isinstance(x, str) else x)
    return (df_sensor,)


@app.cell
def _(df_sensor):
    df_sensor
    return


@app.cell
def _(df_sensor):
    # temp descending order top 5

    df_sensor.sort_values(by="Temperature", ascending=False).head(5)
    return


@app.cell
def _(df_sensor):
    ## each locations humidity rank
    df_sensor['HumidityRank_Location'] = df_sensor.groupby('Location')['Humidity'].rank(method='dense', ascending=False)
    return


@app.cell
def _(df_sensor):
    df_sensor.sort_values(by=['Location', 'Humidity'])
    return


@app.cell
def _(df_sensor):
    ### Sort by DeviceType alphabetically, then by Temperature coldest sensors per type?

    df_sensor.sort_values(by=['DeviceType', 'Temperature'], ascending=[True, True])
    coldest_per_type = df_sensor.groupby("DeviceType").first().reset_index()[["DeviceType", "SensorID", "Temperature"]]
    return (coldest_per_type,)


@app.cell
def _(coldest_per_type):
    coldest_per_type
    return


@app.cell
def _(df_sensor):
    # locations with highest average temperature

    avg_temp_by_location = df_sensor.groupby("Location")["Temperature"].mean().sort_values(ascending=False)
    top_location = avg_temp_by_location.idxmax()

    return (top_location,)


@app.cell
def _(top_location):
    top_location
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

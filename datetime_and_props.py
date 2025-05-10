
import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd 

    data = {'date_string': ['2025-05-01', '2025-06-15', '2025-07-20']}

    df = pd.DataFrame(data)
    return df, pd


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, pd):
    df['date'] = pd.to_datetime(df['date_string'])
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['weekday'] = df['date'].dt.weekday  # Monday=0, Sunday=6

    # Show the DataFrame with new columns
    print(df)
    return


@app.cell
def _(pd):
    data1 = {'date_string': ['05/01/2025', '06/15/2025', '07/20/2025']}
    df1 = pd.DataFrame(data1)
    df1
    return (df1,)


@app.cell
def _(df1, pd):
    df1['date'] = pd.to_datetime(df1['date_string'], format='%m/%d/%Y')
    return


@app.cell
def _(df1):
    print(df1)
    return


@app.cell
def _(pd):
    ### setting date as index  

    data2 = {'date_string': ['2025-01-01', '2025-02-01', '2025-03-01'],
            'value': [10, 15, 20]}
    df2 = pd.DataFrame(data2)
    df2
    return (df2,)


@app.cell
def _(df2, pd):
    df2['date'] = pd.to_datetime(df2['date_string'])
    df2
    return


@app.cell
def _(df2):
    df2.set_index('date', inplace=True)
    return


@app.cell
def _(df2):
    df2
    return


@app.cell
def _(pd):
    ## date difference 

    data3 = {'date_string_1': ['2025-01-01', '2025-02-01'],
            'date_string_2': ['2025-01-10', '2025-02-05']}
    df3 = pd.DataFrame(data3)
    df3
    return (df3,)


@app.cell
def _(df3, pd):
    df3['date_1'] = pd.to_datetime(df3['date_string_1'])
    df3['date_2'] = pd.to_datetime(df3['date_string_2'])
    df3

    return


@app.cell
def _(df3):
    df3['date_diff'] =  (df3['date_2'] - df3['date_1']).dt.days
    df3
    return


@app.cell
def _(pd):
    ## handling time zone 

    data4 = {'date_string': ['2025-05-01 12:00:00', '2025-06-15 14:00:00']}
    df4 = pd.DataFrame(data4)
    df4
    return (df4,)


@app.cell
def _(df4, pd):
    # Convert to datetime and assign a timezone (e.g., UTC)
    df4['datetime'] = pd.to_datetime(df4['date_string']).dt.tz_localize('UTC')
    return


@app.cell
def _(df4):
    df4
    return


@app.cell
def _(df4):
    # Convert to a different timezone (e.g., US Eastern)

    df4['datetime_est'] = df4['datetime'].dt.tz_convert('US/Eastern')

    return


@app.cell
def _(df4):
    df4
    return


@app.cell
def _(pd):
    # Using datetime properties like quarter, is_leap_year
    # Sample data
    data5 = {'date_string': ['2025-01-01', '2025-06-15', '2025-09-01']}
    df5 = pd.DataFrame(data5)
    return (df5,)


@app.cell
def _(df5):
    df5
    return


@app.cell
def _(df5, pd):
    df5['date'] = pd.to_datetime(df5['date_string'])
    return


@app.cell
def _(df5):
    df5['quarter'] = df5['date'].dt.quarter
    return


@app.cell
def _(df5):
    df5
    return


@app.cell
def _(df5):
    df5['is_leap_year'] = df5['date'].dt.is_leap_year
    return


@app.cell
def _(df5):
    df5
    return


if __name__ == "__main__":
    app.run()

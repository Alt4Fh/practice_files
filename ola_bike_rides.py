import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import warnings

    warnings.filterwarnings('ignore', category=FutureWarning)
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('ola.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df, pd):
    df['datetime'] = pd.to_datetime(df['datetime'], yearfirst=True) 
    return


@app.cell
def _(df):
    df['datetime'].dtype
    return


@app.cell
def _(df):
    from datetime import datetime
    def weekend_or_weekday(date: datetime) -> bool:
        return True if date.weekday() > 4 else False

    df['weekend'] = df['datetime'].apply(weekend_or_weekday)
    return


@app.cell
def _(df):
    import holidays

    df['holidays'] = df['datetime'].apply(lambda x: True if holidays.country_holidays('IN').get(x) else False)
    return


@app.cell
def _(df):
    df['holidays']
    return


if __name__ == "__main__":
    app.run()

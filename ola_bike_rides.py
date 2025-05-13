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
    return np, pd, plt, sns


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
    df.head()
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
    df['year'] = df['datetime'].dt.year
    df['month'] = df['datetime'].dt.month
    df['day'] = df['datetime'].dt.day
    df['hour'] = df['datetime'].dt.hour
    return


@app.cell
def _(df):
    import holidays
    ## 

    df['holidays'] = df['datetime'].apply(lambda x: True if holidays.country_holidays('IN').get(x) else False)
    return


@app.cell
def _(df):
    df['holidays']
    return


@app.cell
def _(df, np):
    ##  seasonal features using sine and cosine transformations to capture cyclical patterns.
    ## season vaue given 1 to 4 so reduce by 1 to get the value started by 0
    df['season_sin'] = np.sin(2 * np.pi * (df['season'] - 1 ) / 4 ) 
    df['season_cos'] = np.cos(2 * np.pi * (df['season'] - 1 ) / 4 )
    return


@app.cell
def _(df):
    ## normalize season values 
    ## portion dtype of season

    df['season'].value_counts( normalize=True) * 100
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(12,12))

    for i, col in enumerate(df.select_dtypes(['float64', 'int64', 'int32']).columns):
        plt.subplot(4, 4, i+1)
        sns.histplot(df[col], kde=True)
        plt.title(f'Histogram of {col}')

    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df):
    compare_cols = df.drop(columns='datetime')
    return (compare_cols,)


@app.cell
def _(compare_cols, plt, sns):
    plt.figure(figsize=(12,8))
    sns.heatmap(data=compare_cols.corr(), annot=True, linewidths=0.5, cmap='Blues', fmt='.2f' )
    plt.title(" correlation heatmap")
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()

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

    warnings.filterwarnings("ignore", category=FutureWarning)
    return pd, plt, sns


@app.cell
def _(pd):
    df = pd.read_csv('olympics2024.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.tail()
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
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell(hide_code=True)
def _():
    ## analys
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    ## check for duplicates
    df.duplicated().sum()
    return


@app.cell
def _(df):
    df['Country'].value_counts().sum()
    return


@app.cell
def _(df):
    ## country who recieve none medals

    df[(df['Gold'] == 0) & (df['Silver'] == 0) & (df['Bronze'] == 0)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# visualization""")
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(16,8))
    sns.barplot(x='Country', y='Gold', data=df, order=df['Country'].value_counts().head(50).index)
    plt.xlabel('Country')
    plt.ylabel('Gold Medals')
    plt.title('Countries with gold medals')
    plt.xticks(rotation=90)
    plt.show()
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='Gold', y='Silver', data=df)
    plt.title('Gold vs Silver')
    return


@app.cell
def _(df, plt, sns):
    # histogram of total medals
    df['total'] = df['Gold'] + df['Silver'] + df['Bronze']
    plt.figure(figsize=(10,6))
    sns.histplot(df['total'], bins=10)
    plt.title('Distribution of total medals')
    return


if __name__ == "__main__":
    app.run()

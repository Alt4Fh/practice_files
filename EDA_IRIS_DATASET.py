import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    return pd, plt, sns


@app.cell
def _(pd):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    df = pd.read_csv(url, names=(column_names))
    return (df,)


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
    df.isna().sum()
    return


@app.cell
def _(df, plt):
    df.hist(bins=30, figsize=(10,8))
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(12,8))
    sns.boxplot(data=df.drop('species', axis=1))
    plt.show()
    return


@app.cell
def _(df, sns):
    sns.pairplot(df, hue='species')
    return


if __name__ == "__main__":
    app.run()

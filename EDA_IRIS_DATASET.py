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
    for i, column in enumerate(df.columns[:-1], 1): ## excluse species
        plt.subplot(2,2,i)
        sns.boxplot(x='species', y=column, data=df)
        plt.title(f'{column} by Species')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, sns):
    sns.pairplot(df, hue='species', diag_kind='kde')

    return


@app.cell
def _(df):
    df['species'].unique()
    return


@app.cell
def _(df):
    df_num_only = df.drop(columns=['species'])
    return (df_num_only,)


@app.cell
def _(df_num_only):
    df_num_only.corr()
    return


@app.cell
def _(df_num_only, plt, sns):
    sns.heatmap(df_num_only.corr(), annot=True,linecolor='cyan', linewidths=0.5, cmap='coolwarm')
    plt.title('Feature correlation')

    return


@app.cell
def _(df, sns):
    sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species' )
    return


@app.cell
def _(df):
    df.groupby('species').std()
    return


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.read_csv('superstore.csv')
    return df, pd, plt, sns


@app.cell
def _(df):
    ### remove unnessery columns
    df.drop(columns=['记录数'], inplace=True)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    ## converting category and sub-category to categoral data
    df['Category'] = df['Category'].astype('category')
    df['Sub.Category'] = df['Sub.Category'].astype('category')
    return


@app.cell
def _(df, pd):
    #### Ship.Date, Order.Date to datetime object
    ## df['Order.Date'].isna().sum() ## no na
    ## df['Ship.Date'].isna().sum()  ## no na

    df['Ship.Date'] = pd.to_datetime(df['Ship.Date'])
    df['Order.Date'] = pd.to_datetime(df['Order.Date'])

    #df[['Ship.Date','Order.Date']].head()
    return


@app.cell
def _(df, plt, sns):
    #df['City'].isna().sum()
    ##df.isna().sum() ## zero na
    ## histplot of numerical values

    df_num = df.select_dtypes(include=['number'])
    df_columns = list(df_num.columns)
    n_rows = len(df_columns)//2
    n_columns = 2
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_columns, figsize=(16,16))
    fig.subplots_adjust(hspace=0.5, wspace=0.2)
    for i, ax in enumerate(iterable=axes.flatten()):
        sns.histplot(ax=ax, data=df_num[df_columns[i]], kde=True, bins=40)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.set_title(f'Distribution of {df_columns[i]}')

    plt.show()
    
    return


if __name__ == "__main__":
    app.run()

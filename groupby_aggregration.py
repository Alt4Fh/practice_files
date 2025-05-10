

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import pyarrow as pa
    import numpy as np
    return (pd,)


@app.cell
def _(pd):
    data = {
        'order_id': [101, 102, 103, 104, 105, 106, 107],
        'region': ['North', 'South', 'North', 'West', 'South', 'West', 'North'],
        'product': ['Laptop', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Phone', 'Laptop'],
        'quantity': [1, 3, 2, 1, 4, 2, 1],
        'unit_price': [1000, 300, 1000, 500, 300, 500, 1000]
    }

    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['toatal_price'] = df['quantity'] * df['unit_price']
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # total sold  by 'region' and 'product'

    df.groupby(['region', 'product'])['quantity'].sum()
    return


@app.cell
def _(df):
    # total revenue

    df.rename(columns={'toatal_price': 'total_price'}, inplace=True)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    agg_df = df.groupby(['region', 'product']).agg(
        quantity_sum= ('quantity', 'sum'),
        revenue_sum = ('total_price', 'sum'),
        unit_price_mean = ('unit_price', 'mean')   
    ).reset_index()
    return (agg_df,)


@app.cell
def _(agg_df):
    agg_df.sort_values(by='revenue_sum', ascending=False)
    return


@app.cell
def _(pd):
    df1 = pd.read_csv('sales_data.csv')

    return (df1,)


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df1):
    ## Total sales per store 
    df1['Total_Sales'] = df1['Quantity'] * df1['Price']
    store_sales = df1.groupby('Store')['Total_Sales'].sum()
    return (store_sales,)


@app.cell
def _(store_sales):
    store_sales
    return


@app.cell
def _(df1):
    ## average quantity sold per product
    df1.groupby('Product')['Quantity'].mean()
    return


@app.cell
def _(df1):
    #max price per product
    df1.groupby('Product')['Price'].max()
    return


@app.cell
def _(df1):
    # total sales per product and store

    df1.groupby(['Store','Product'])['Total_Sales'].sum()
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(plt, store_sales):
    store_sales.plot(kind='bar', title='Total sales per person')
    plt.ylabel('Total Sales')
    plt.show()
    return


if __name__ == "__main__":
    app.run()

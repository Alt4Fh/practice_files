

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        | **Use Case**         | **Use `.transform()`**                                                                    | **Use `.agg()`**                                                   |
        | -------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
        | **Result Size**      | Same size as the original (same number of rows)                                           | Smaller (reduced size, one row per group)                          |
        | **Purpose**          | Apply a transformation **within each group**                                              | Compute **summary statistics** for each group                      |
        | **Use Case Example** | Normalize values, rank values, fill missing values                                        | Calculate sum, mean, count, max, etc.                              |
        | **Behavior**         | Transforms data element-wise across groups                                                | Aggregates data to a single value per group                        |
        | **When to Use**      | You want to retain the original structure (e.g., normalizing salaries within departments) | You want to compute summaries like mean, sum, or max across groups |
        | **Function Type**    | Element-wise functions                                                                    | Aggregate functions (e.g., `mean`, `sum`, `max`)                   |
        """
    )
    return


@app.cell
def _(pd):
    data = {
        'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Product': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'A', 'C'],
        'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Furniture', 'Furniture', 'Electronics', 'Furniture'],
        'SalesAmount': [100, 200, 150, 250, 120, 300, 350, 180, 140, 270],
        'Date': pd.to_datetime([
            '2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05',
            '2025-01-06', '2025-01-07', '2025-01-08', '2025-01-09', '2025-01-10'
        ]),
        'CustomerID': [101, 102, 101, 103, 102, 104, 105, 106, 101, 107]
    }

    df = pd.DataFrame(data)

    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.groupby('Product')['SalesAmount'].agg(['mean', 'sum'])
    return


@app.cell
def _(df):
    ## average sales per customer 


    df['AvgSalesPerCustomer'] = df.groupby('CustomerID')['SalesAmount'].transform('mean')
    df[['CustomerID', 'SalesAmount', 'AvgSalesPerCustomer']]
    return


@app.cell
def _(df):
    top_2_sales = df.sort_values(by = ['Category','SalesAmount'], ascending=[True, False]).groupby('Category').head(2)
    return (top_2_sales,)


@app.cell
def _(top_2_sales):
    top_2_sales
    return


@app.cell
def _(df):
    df['p_s_mean_d'] = df.groupby('Product')['SalesAmount'].transform(
        lambda x : (x - x.mean())
    )
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    #rank each sale for every customer within each product category, based on the sales amount

    df['sales_rank'] = df.groupby(['Category', 'CustomerID'])['SalesAmount'].rank(ascending=False)

    df[['Category', 'CustomerID', 'SalesAmount', 'sales_rank']]
    return


@app.cell
def _(df):
    #How would you calculate the total sales per day

    df.groupby(df['Date'].dt.date)['SalesAmount'].sum()

    return


@app.cell
def _(df):
    ## cummulative sales

    df['cumsum'] = df.sort_values('Date').groupby('Product')['SalesAmount'].cumsum()
    df[['Product', 'Date', 'SalesAmount', 'cumsum']]
    return


@app.cell
def _(pd):
    data1 = {
        'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'Product': ['Shampoo', 'Shampoo', 'Toothpaste', 'Shampoo', 'Toothpaste', 'Toothpaste', 'Shampoo', 'Shampoo', 'Toothpaste', 'Toothpaste'],
        'Category': ['Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care', 'Personal Care'],
        'SalesAmount': [10, 12, 5, 15, 7, 6, 9, 14, 5, 8],
        'Quantity': [2, 3, 1, 2, 1, 2, 3, 4, 1, 2],
        'Date': pd.to_datetime([
            '2025-04-01', '2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04',
            '2025-04-05', '2025-04-06', '2025-04-07', '2025-04-08', '2025-04-09'
        ]),
        'CustomerID': [1001, 1002, 1001, 1003, 1004, 1002, 1005, 1001, 1003, 1004]
    }

    df1 = pd.DataFrame(data1)
    return (df1,)


@app.cell
def _(df1):
    df1.head()
    return


@app.cell
def _(df1):
    ## total sales amount and quantity sold

    df1.groupby('Product').agg({'SalesAmount':'sum', 'Quantity': 'sum'})
    return


@app.cell
def _(df1):
    df1.groupby('CustomerID')['SalesAmount'].transform('mean')
    return


@app.cell
def _(df, df1):
    df1.groupby([df['Date'].dt.date, 'Category']).agg({'SalesAmount':'sum', 'Quantity': 'sum'}).reset_index()
    return


@app.cell
def _(df1):
    product_sales = df1.groupby('Product').agg({'SalesAmount':'sum', 'Quantity': 'sum'}).reset_index()
    total_sales = product_sales['SalesAmount'].sum()
    product_sales['SalesPercentage'] = (product_sales['SalesAmount'] / total_sales) * 100

    return (product_sales,)


@app.cell
def _(product_sales):
    product_sales
    return


@app.cell
def _(df1):
    ## Find the most frequently purchased product by each customer

    df1.groupby('CustomerID')['Product'].apply(lambda x: x.mode()[0]).reset_index()
    return


@app.cell
def _(df1):
    ##

    first_week_sales = df1[df1['Date'].between('2025-04-01', '2025-04-07')]

    #df1.sort_values('Date', ascending=True).groupby(['Date','Product'])['SalesAmount'].sum().reset_index()

    sales_first_week = first_week_sales.groupby('Product')['SalesAmount'].sum().reset_index()
    return (sales_first_week,)


@app.cell
def _(sales_first_week):
    sales_first_week
    return


@app.cell
def _(df1):
    max_trans=df1.loc[df1['SalesAmount'].idxmax()]

    max_trans[['CustomerID', 'SalesAmount']]
    return


@app.cell
def _(df1):
    df1.sort_values(by=['CustomerID', 'SalesAmount'], ascending=[True, False]).groupby('CustomerID').head(3)
    return


@app.cell
def _():



    return


if __name__ == "__main__":
    app.run()

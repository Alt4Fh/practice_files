

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd


    ## left join

    df1 = pd.DataFrame({
        'CustomerID': [101, 102, 103],
        'Name': ['John', 'Jane', 'Jake']
    })

    df2 = pd.DataFrame({
        'CustomerID': [102, 103, 104],
        'PurchaseAmount': [200, 250, 300]
    })


    merged_df = df1.merge(df2, on='CustomerID', how='left')

    return merged_df, pd


@app.cell
def _(merged_df):
    merged_df
    return


@app.cell
def _(pd):
    df3 = pd.DataFrame({
        'ProductID': [1, 2, 3],
        'ProductName': ['Shampoo', 'Toothpaste', 'Soap']
    })

    df4 = pd.DataFrame({
        'ProductID': [2, 3, 4],
        'Stock': [50, 60, 40]
    })

    df_merged1 = df3.merge(df4, how='right', on='ProductID')
    return (df_merged1,)


@app.cell
def _(df_merged1):
    df_merged1
    return


@app.cell
def _(pd):
    ### contcat



    dfc1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    dfc2 = pd.DataFrame({
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    df_concat = pd.concat([dfc1, dfc2], axis=1)
    return (df_concat,)


@app.cell
def _(df_concat):
    df_concat
    return


@app.cell
def _():
    data = {
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
        'Store': ['A', 'B', 'A', 'B', 'A'],
        'Product': ['Apple', 'Apple', 'Banana', 'Apple', 'Banana'],
        'Units_Sold': [10, 5, 7, 8, 12],
        'Revenue': [20, 10, 14, 16, 24]
    }


    return


if __name__ == "__main__":
    app.run()

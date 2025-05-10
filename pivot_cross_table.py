

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return np, pd


@app.cell
def _(np):
    n_scores = np.array([
            [63, 72, 75, 51, 83],
            [44, 53, 57, 56, 48],
            [71, 77, 82, 91, 76],
            [67, 56, 82, 33, 74],
            [64, 76, 72, 63, 76],
            [47, 56, 49, 53, 42],
            [91, 93, 90, 88, 96],
            [61, 56, 77, 74, 74],
     ])
    return (n_scores,)


@app.cell
def _(n_scores):
    n_scores.size
    return


@app.cell
def _(n_scores):
    n_scores.shape
    return


@app.cell
def _(n_scores):
    n_scores.max()
    return


@app.cell
def _(pd):
    data = {
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
        'Store': ['A', 'B', 'A', 'B', 'A'],
        'Product': ['Apple', 'Apple', 'Banana', 'Apple', 'Banana'],
        'Units_Sold': [10, 5, 7, 8, 12],
        'Revenue': [20, 10, 14, 16, 24]
    }

    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, pd):
    pivot_df = pd.pivot_table(df, values='Revenue', index='Store', columns='Product', aggfunc='sum', fill_value=0 )
    return (pivot_df,)


@app.cell
def _(pivot_df):
    pivot_df
    return


@app.cell
def _(df, pd):
    ct = pd.crosstab(df['Store'], df['Product'])
    return (ct,)


@app.cell
def _(ct):
    ct
    return


if __name__ == "__main__":
    app.run()

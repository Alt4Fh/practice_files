

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
    df = pd.read_csv('sensor_data.csv')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

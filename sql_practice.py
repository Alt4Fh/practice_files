import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import random

    # Sample names and occupations
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Robert Brown", "Emily Davis", "Michael Wilson", "Jessica Lee",
             "Daniel Thomas", "Laura Moore", "Kevin Harris"]
    occupations = ["Software Engineer", "Data Analyst", "Graphic Designer", "Accountant", "Marketing Manager", "Doctor",
                   "Lawyer", "Mechanical Engineer", "Nurse", "Teacher"]

    # Generate dataset with 100 random entries
    data_set = [{"Name": random.choice(names), "Occupation": random.choice(occupations)} for _ in range(30)]

    # Print the first 10 rows as a sample
    for entry in data_set[:10]:
        print(entry)

    return (data_set,)


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return (pd,)


@app.cell
def _(data_set, pd):
    df = pd.DataFrame(data=data_set)
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df, mo):
    _df = mo.sql(
        f"""
        SELECT CONCAT(Name, ' (', SUBSTRING(Occupation, 1, 1), ')')
        from df

        """
    )
    return


@app.cell
def _(df):
    ## pivot table with pandas

    df.pivot_table(index='Occupation', aggfunc='size')
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

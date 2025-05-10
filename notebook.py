

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import pyarrow as pa
    return pa, pd


@app.cell
def _(pd):
    ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
    return (ser,)


@app.cell
def _(ser):
    ser
    return


@app.cell
def _(pa):
    list_str_type = pa.list_(pa.string())
    return (list_str_type,)


@app.cell
def _(list_str_type, pd):
    ser1 = pd.Series([["hi!"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
    return (ser1,)


@app.cell
def _(ser1):
    ser1
    return


@app.cell
def _():
    from datetime import time 
    return (time,)


@app.cell
def _(pa, pd, time):
    idx = pd.Index([time(12, 30), None], dtype=pd.ArrowDtype(pa.time64("us")))
    return (idx,)


@app.cell
def _(idx):
    idx
    return


@app.cell
def _(pd):
    df = pd.read_csv('emp.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):

    columns = list(df.columns)
    return (columns,)


@app.cell
def _(columns):
    columns_mod = [x.strip() for x in columns]
    return (columns_mod,)


@app.cell
def _(columns_mod):
    columns_mod
    return


@app.cell
def _(columns_mod, df):
    df.columns = columns_mod
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    # emp with salary greater than 100,000
    df.loc[df['Salary'] > 100000 ]
    return


@app.cell
def _(df):
    df.groupby(["Department"])['Salary'].mean()
    return


@app.cell
def _(df):
    department = [x.strip() for x in list(df['Department']) ]
    return (department,)


@app.cell
def _(department, df):
    df["Department"] = department
    return


@app.cell
def _(df):
    list(df["Department"])
    return


@app.cell
def _(df):
    df.query('Age > 30 and Department == "Engineering"')
    return


@app.cell
def _(df):
    df.groupby("Gender")['EmployeeID'].count()
    return


@app.cell
def _(df):
    gender_counts = df['Gender'].value_counts()
    return (gender_counts,)


@app.cell
def _(gender_counts):
    gender_counts
    return


@app.cell
def _(df, pd):
    from datetime import date
    df['JoinDate'] = pd.to_datetime(df['JoinDate'])

    return


@app.cell
def _(df):
    ## list of employees who joind before 2019
    df.loc[(df['JoinDate'].dt.year < 2019)]
    return


@app.cell
def _(df):
    # alternative and easy
    df[df['JoinDate'] < '2019-01-01']
    return


@app.cell
def _(df):
    df['Salary_bonus'] = df['Salary'] * 1.1
    return


@app.cell
def _(df):
    df.groupby('Department')[['Salary', 'Name']].max() 
    return


@app.cell
def _(df):
    # alternative 

    idx_max = df.groupby('Department')['Salary'].idxmax()
    df.loc[idx_max]
    return


@app.cell
def _(df):
    df.query('Age > 35 and Salary > 100000')
    # df.query('Age > 35')

    return


@app.cell
def _(df):
    # Filter the dataset to get employees who belong to the HR or Marketing department and whose salary is between $80,000 and $100,000.

    df[df['Department'].isin(['HR', 'Marketing']) & (df['Salary'] > 80000) & (df['Salary'] < 100000) ]
    return


@app.cell
def _(df):
    df[(df['Department'].isin(['HR', 'Marketing'])) & (df['Salary'].between(80000, 100000))]
    return


@app.cell
def _(df):
    # average age of employee in each department
    df.groupby('Department')['Age'].mean()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

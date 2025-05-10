

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
def _():
    data = {
        'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    return (data,)


@app.cell
def _(data, pd):
    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.rename(columns={'First Name': 'Name', 'City': 'Location'}, inplace=True)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Location'] = df['Location'].replace({'New York' :'NY', 'Los Angeles' : 'LA', 'Chicago' : 'CHI', 'Houston' : 'HOU'})
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(pd):
    data1 = {
        'review': [
            '  Excellent product! Highly recommend.  ',
            'Terrible experience. Will not buy again.',
            'Average quality, okay for the price.',
            'Loved it!! Will buy AGAIN :)',
            'not bad... could be better.',
            'EXCELLENT value!!! '
        ]
    }

    df1 = pd.DataFrame(data1)
    return (df1,)


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df1):
    # remove leading and trailing spaces of review columns

    df1['review'].str.strip()
    return


@app.cell
def _(df1):
    df1['is_positive'] = list(df1['review'].str.contains("excellent", case=False) | df1['review'].str.contains("loved", case=False))
    return


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df1):
    #replace multiple exclamation marks with one.
    df1['review'] = df1['review'].str.replace(pat= r'(!)\1+', repl= '!', regex=True)
    return


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df1):
    # remove any characters that are not letters, numbers, spaces, or exclamation points.

    df1['review'] = df1['review'].str.replace(r'[^a-zA-Z0-9 !]', '', regex=True)
    return


@app.cell
def _(df1):
    df1['review'] = df1['review'].str.lower()
    return


@app.cell
def _(df1):
    ## percentage of positive reviews
    

    t, f = df1['is_positive'].value_counts()

    percentage_positive_review = (t/(t+f))*100
    return (percentage_positive_review,)


@app.cell
def _(percentage_positive_review):
    percentage_positive_review
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

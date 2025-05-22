import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    This Jupyter Notebook contains the code used in the [RealPython]()https://www.realpython.com) tutorial [**Aggregating and Grouping Data in Polars**](https://realpython.com/aggregating-and-grouping-data-in-polars-groupby/)

    # Aggregating Data
    """
    )
    return


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _(pl):
    _math_students = pl.read_parquet('./materials-polars-groupby/math.parquet')
    _math_students.select(pl.col('absences').max())
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('./materials-polars-groupby/math.parquet')
    _math_students.select(pl.col('student_id', 'absences')).filter(pl.col('absences') == pl.col('absences').max())
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('./materials-polars-groupby/math.parquet')
    _math_students.select(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean())
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('./materials-polars-groupby/math.parquet')
    _math_students.select('student_id', 'G1', 'G2', 'G3', total=pl.sum_horizontal('G1', 'G2', 'G3'), mean=pl.mean_horizontal('G1', 'G2', 'G3'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Grouping Data for Aggregation With .groupby()
    ## Grouping Data - Basic Principles
    """
    )
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('math.parquet')
    _math_students.select(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean())
    return


@app.cell
def _(pl):
    portuguese_students = pl.read_parquet("portuguese.parquet")

    (
        portuguese_students.select(
            min=pl.col("absences").min(),
            max=pl.col("absences").max(),
            mean=pl.col("absences").mean(),
        )
    )
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by('subject').agg(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Grouping Data - The Power of Expressions""")
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('math.parquet')
    _math_students.group_by('age').agg(passes=pl.col('G3'))
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('math.parquet')
    _math_students.group_by('age').agg(passes=pl.col('G3').filter(pl.col('absences') > pl.col('absences').mean(), pl.col('G3') >= 13))
    return


@app.cell
def _(pl):
    _math_students = pl.read_parquet('math.parquet')
    _math_students.group_by('age').agg(passes=pl.col('G3').filter(pl.col('absences') > pl.col('absences').mean(), pl.col('G3') >= 13).count(), poor_attenders=pl.col('G3').filter(pl.col('absences') > pl.col('absences').mean()).count()).select(pl.col('age', 'passes', 'poor_attenders'), percentage=pl.col('passes') / pl.col('poor_attenders') * 100).with_columns(pl.col('percentage').replace(float('NaN'), 0)).sort('age')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Grouping and Aggregating by Multiple Columns""")
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by(['subject', 'reason']).agg(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean()).sort('subject')
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by(['subject', 'reason']).agg(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean()).sort('subject', 'reason')
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by(['subject', 'reason']).agg(min=pl.col('absences').min(), max=pl.col('absences').max(), mean=pl.col('absences').mean()).sort('reason', descending=True).sort('subject')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Grouping and Aggregating Time Series With .group_by_dynamic()""")
    return


@app.cell
def _(pl):
    _math_attendance = pl.read_parquet('./materials-polars-groupby/math_classes.parquet')
    _math_attendance.head()
    return


@app.cell
def _(pl):
    _math_attendance = pl.read_parquet('./materials-polars-groupby/math_classes.parquet')
    _math_attendance.group_by_dynamic(index_column='class_start', every='1w', closed='both').agg(total_absences=pl.col('absences').sum(), mean_absences=pl.col('absences').mean())
    return


@app.cell
def _(pl):
    _math_attendance = pl.read_parquet('math_classes.parquet')
    _math_attendance.group_by_dynamic(index_column='class_start', every='1q', closed='both', group_by='class_subject').agg(pl.col('absences').sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Grouping and Aggregating Using Window Functions""")
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.select(pl.col('subject', 'school', 'student_id', 'reason', 'absences'), mean_absences=pl.col('absences').mean().over('subject', 'school', 'reason'))
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.select(pl.col('subject', 'school', 'student_id', 'reason', 'absences'), mean_absences=pl.col('absences').mean().over('subject', 'school', 'reason')).filter(pl.col('absences') > pl.col('mean_absences'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Grouping and Aggregating Using Pivot Tables""")
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by(['subject', 'school']).agg(mean_absence=pl.col('absences').mean(), mean_failure=pl.col('failures').mean())
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.pivot(on='school', index='subject', values=['absences', 'failures'], aggregate_function='mean')
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.pivot(on='school', index='subject', values=['absences', 'failures'], aggregate_function='mean').select(pl.col('subject', 'absences_GP', 'failures_GP', 'absences_MS', 'failures_MS'))
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.pivot(on='school', index=['subject', 'reason'], values=['absences', 'failures'], aggregate_function='mean').select(pl.col('subject', 'reason', 'absences_GP', 'failures_GP', 'absences_MS', 'failures_MS'))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

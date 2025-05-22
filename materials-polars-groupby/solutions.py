import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    math_students = pl.read_parquet("math.parquet")

    (
        math_students.select(
            median_result=pl.col("G3").median(),
            most_frequent_result=pl.col("G3").mode(),
            variance=pl.col("G3").var(),
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Grouping Data
        """
    )
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.group_by(['subject', 'internet']).agg(total=pl.col('student_id').count(), passes=pl.col('G3').filter(pl.col('G3') > 12).count()).select(pl.col('subject', 'internet', 'total', 'passes'), percentage=pl.format('{}%', (pl.col('passes') * 100 / pl.col('total')).round(2))).sort('subject')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Grouping Time Series Data With .group_by_dynamic()
        """
    )
    return


@app.cell
def _(pl):
    math_attendance = pl.read_parquet("math_classes.parquet")

    (
        math_attendance.group_by_dynamic(
            index_column="class_start",
            every="1mo",
            closed="both",
            group_by="lecturer_initials",
        ).agg(pl.col("absences").mean())
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Grouping and Aggregating Using Window Functions
        """
    )
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.select(pl.col('subject', 'reason', 'G1'), mean_G1=pl.col('G1').mean().over('subject', 'reason'), G2=pl.col('G2'), mean_G2=pl.col('G2').mean().over('subject', 'reason')).filter((pl.col('G1') > pl.col('mean_G1')) & (pl.col('G2') > pl.col('mean_G2')))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Grouping and Aggregating Using Pivot Tables
        """
    )
    return


@app.cell
def _(pl):
    _all_students = pl.read_parquet('course.parquet')
    _all_students.pivot(on='school', index=['subject', 'sex'], values=['G1', 'G2'], aggregate_function='mean')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

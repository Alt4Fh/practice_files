import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Coding Exercises (Part 2)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Full Data Workflow A-Z: Reshaping and Pivoting
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 14: Reshaping and Pivoting DataFrames
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now, you will have the opportunity to analyze your own dataset. <br>
        __Follow the instructions__ and insert your code! You are either requested to 
        - Complete the Code and __Fill in the gaps__. Gaps are marked with "__---__" and are __placeholders__ for your code fragment. 
        - Write Code completely __on your own__ 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If you need a hint, check the __Hints Section__ at the end of this Notebook. Exercises and Hints are numerated accordingly.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If you need some further help or if you want to check your code, you can also check the __solutions notebook__.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Have Fun!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        --------------------------------------------------------------------------------------------------------------
        """
    )
    return


@app.cell
def _():
    #run the cell
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    #run the cell
    cars = pd.read_csv("cars.csv")
    return (cars,)


@app.cell
def _(cars):
    #run the cell
    cars.head()
    return


@app.cell
def _(cars):
    #run the cell
    cars.tail()
    return


@app.cell
def _(cars):
    #run the cell
    cars.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        127. Calculate the __mean mpg__ for all combinations of __model_year__ and __origin__! __Save__ the resulting DataFrame in the variable __mpg_year_origin__! <br>__Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    mpg_year_origin = cars.groupby([\"model_year\", \"origin\"]).---.---.unstack().round(2)
    mpg_year_origin
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        128. __Transpose__ mpg_year_origin!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Import the __mean_mpg.csv__ file, save in the variable __mean_mpg__ and inspect!
        """
    )
    return


@app.cell
def _(pd):
    # run the cell
    mean_mpg = pd.read_csv("mean_mpg.csv")
    mean_mpg
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        129. __Pivot__ mean_mpg! Resulting wide-format DataFrame shall have three columns __europe__, __japan__ and __usa__. __model_year__ shall be the __index__!<br>
        __Save__ new DataFrame in the variable __pivot__!
        """
    )
    return


@app.cell
def _(pivot):
    #run the cell!
    pivot.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Reset the index!
        """
    )
    return


@app.cell
def _(pivot):
    # run the cell!
    pivot.reset_index(inplace= True)
    return


@app.cell
def _(pivot):
    # run the cell!
    pivot.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        130. __Melt__ the DataFrame __pivot__ from wide format __back to long format__! __Fill in the gaps!__
        """
    )
    return


app._unparsable_cell(
    r"""
    pivot.melt(id_vars= ---, value_vars= ---, var_name = ---, value_name = ---)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        131. Return the __number of cars__ for each __combination of model_year and origin__ with __pd.crosstab()__ (e.g. 5 cars from europe in 1970)! <br>
        __How many__ cars from __usa__ are built in __1972__?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ... 18 Cars from usa are built in 1972.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Well Done!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        -----------------------------------------------------
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Hints (Spoiler!)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        127. mpg, mean() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        128. T attribute / transpose() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        129. pivot() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        130. check the parameters of melt() with SHIFT + TAB
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        131. cars.model_year, cars.origin
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

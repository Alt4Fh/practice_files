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
        ## Full Data Workflow A-Z: Group Operations
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 13: GroupBy
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Option 1: Self_guided
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Import the cars dataset (cars.csv).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Calculate__ the mean/average mpg __by origin__ (mean mpg for usa, for europe and for japan)! Who built the __least__ fuel efficient cars?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Calculate__ the mean/average mpg __by model_year__ (mean mpg for the years 70, 71, ...). Can you see a __trend__? __Visualize__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Calculate__ the mean/average mpg for each __combination of model_year & origin__ and __visualize__ how the mean mpg evolved over time for usa, europe and japan. <br>
        Can you see the __same trend__ for all three orgins?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Calculate the __mean__, __min__ and __max__ mpg for each combination of model_year & origin!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Return the columns __name__ and __mpg__ for the __two most fuel efficient cars__ for __each combination of model_year & origin__! <br>(hint: a __user defined function__ might help!)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Calculate the __mean mpg__ for each combination of __model_year & origin__ and __assign__ the corresponding __group-specific value__ to all cars (__new column__!).<br>
        Then, __filter__ all cars, where the __absolute difference__ between __mpg__ and __group-specific mpg__ is __greater than 10__. These cars are outliers/special cases in their respective group.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ------------------------
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Option 2: Guided and Instructed
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
    )
    return


@app.cell
def _():
    #run the cell
    import pandas as pd
    import matplotlib.pyplot as plt
    plt.style.use("seaborn")
    return pd, plt


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
        117. __Group__ cars by the column __origin__ and __calculate__ the __mean__/average __mpg__ for each origin (mean mpg for usa, for europe and for japan)! <br>
        Who built the __least__ fuel efficient cars?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The least fuel efficient cars are from ... usa.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        118. __Group__ cars by the column __model_year__ and __calculate__ the __mean__/average __mpg__ for each model_year (mean mpg for 70, 71, 72,...)! <br>__Save__ the result in the variable __mpg_by_year__ and __round__ to two decimals!
        """
    )
    return


@app.cell
def _(mpg_by_year):
    # run the cell
    mpg_by_year
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__! Can you see a __trend__?
        """
    )
    return


@app.cell
def _(mpg_by_year, plt):
    # run the cell!
    mpg_by_year.plot()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The cars are getting ... more fuel efficient over time.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        119. __Group__ cars by the columns __model_year and origin__ and return the __mean mpg__ for each group! <br> __Save__ the resulting DataFrame in the variable __mpg_year_origin__!
        __Column labels__ of mpg_year_origin shall be __europe__, __japan__ & __usa__. __Fill in the gaps__! 
        """
    )
    return


app._unparsable_cell(
    r"""
    mpg_year_origin = cars.groupby(---).mpg.mean().---.round(2)
    """,
    name="_"
)


@app.cell
def _(mpg_year_origin):
    # run the cell
    mpg_year_origin
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__! Do we have the __same trend__ for europe, japan and usa?
        """
    )
    return


@app.cell
def _(mpg_year_origin, plt):
    # run the cell
    mpg_year_origin.plot()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It seems that manufacturer from europe, japan and usa were able to improve efficiency!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        120. __Group__ cars by __model_year and origin__ and return __mean__, __max__ and __min mpg__ for all groups! __Fill in the gaps!__
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.groupby([\"model_year\", \"origin\"]).mpg.---(---).unstack().round(2)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Next, return the columns __name__ and __mpg__ for the __two most fuel efficient cars__ for __each combination of model_year & origin__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        121. First, __create__ the __user defined function__ get_most_efficient! __Fill in the gaps!__ 
        """
    )
    return


app._unparsable_cell(
    r"""
    def get_most_efficient(group):
        return group.---(n = ---, columns = \"mpg\").loc[:, [\"name\", \"mpg\"]]
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        122. __Apply__ get_most_efficient on the appropriate __groupby object__! __Save__ the resulting DataFrame in the variable __most_eff__. __Fill in the gaps!__
        """
    )
    return


app._unparsable_cell(
    r"""
    most_eff = cars.groupby([---, ---]).---(---)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Tidy up and __Inspect__!
        """
    )
    return


@app.cell
def _():
    # run the cell
    most_eff = most_eff.droplevel(-1)
    return (most_eff,)


@app.cell
def _(most_eff):
    # run the cell
    most_eff.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        123. __Select__ the 2 most efficient cars from __japan__ in __1980__! __Fill in the gaps!__ The __most efficient__ car is...?
        """
    )
    return


app._unparsable_cell(
    r"""
    most_eff.loc[---]
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The most efficient car is... the mazda glc.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Calculate the __mean mpg__ for each combination of __model_year & origin__ and __assign__ the corresponding __group-specific value__ to all cars (__new column__!). Then, __filter__ all cars where the __absolute difference__ between __mpg__ and __group-specific mpg__ is __greater than 10__. These cars all outliers/special cases in their respective group.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        124. First, __group__ cars by __model_year & origin__ and calculate the __mean mpg__ for each group via the --- method to create the new column __"group_mpg"__. <br>
        __Fill in the gaps!__
        """
    )
    return


app._unparsable_cell(
    r"""
    cars[\"group_mpg\"] = cars.groupby([\"model_year\", \"origin\"]).mpg.---(---).round(2)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect!__ The group-specific mpg for the vw pickup is ... ?
        """
    )
    return


@app.cell
def _(cars):
    # run the cell
    cars.head()
    return


@app.cell
def _(cars):
    # run the cell
    cars.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The group-specific mpg for the vw pickup is... 40.0!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        125. __Create__ the column __"mpg_outlier"__ by __substracting__ the __group_mpg__ column from the __mpg__ column. __Round__ to 2 decimals! 
        """
    )
    return


@app.cell
def _(cars):
    # run the cell
    cars.mpg_outlier.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        126. __Filter__ cars for all cars/rows, where the __absolute value__ in the __mpg_outlier__ column is __greater than 10__! __Fill in the gaps!__<br>
        There is only one car, that is __significantly less fuel efficient__ than it´s peer group. Which one?
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[--- > 10]
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The... mazda rx-7 gs is significantly less fuel efficient than it´s peer group (negative value in mpg_outlier column).
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
        -------------------
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Hints (Spolier!)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        117. cars.groupby("---").---.mean()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        118. mpg_by_year = cars.groupby("---").---.---.round(2)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        119. Don´t forget unstack() method!

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        120. agg() method, unstack() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        121. nlargest() method; 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        122. group cars by model_year & origin; pass get_most_efficient to the apply() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        123. outer index level: 80; inner index level: "japan"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        124. transform() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        125. (_pandas series_ - _pandas series_).round()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        126. abs() method
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

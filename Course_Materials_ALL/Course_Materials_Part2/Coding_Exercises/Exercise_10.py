import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Coding Exercises (Part 2)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Full Data Workflow A-Z: Importing Data""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Exercise 10: Importing Data from messy csv-files""")
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
    mo.md(r"""In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If you need a hint, check the __Hints Section__ at the end of this Notebook. Exercises and Hints are numerated accordingly.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If you need some further help or if you want to check your code, you can also check the __solutions notebook__.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Have Fun!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""--------------------------------------------------------------------------------------------------------------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Option 1: Self_guided""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""__Import__ the cars Dataset from the messy csv-file __cars_raw.csv__ into a Pandas DataFrame. Use appropriate __parameters__ in the __pd.read_csv()__ method to bring the DataFrame into a clean format. __Columns__ should have the following __labels__:""")
    return


@app.cell
def _():
    labels = ['mpg',
     'cylinders',
     'displacement',
     'horsepower',
     'weight',
     'acceleration',
     'model year',
     'origin',
     'name']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Finally, __save__ and __export__ the dataset as new csv-file (__cars_imp.csv__).""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Option 2: Guided and Instructed""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""77. __Import__ Pandas (pd)!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""78. __Import__ the csv-file __cars_raw.csv__ with the appropriate pandas method and __inspect__ the data!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use appropriate __parameters__ in the __pd.read_csv()__ method to clean the format. The following issues need to be solved:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""79. __Remove__ the __first row(s)__ containing nonsense content.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""80. __Remove__ the __last row(s)__ containing nonsense content.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""81. Define that there are __no appropriate column labels/headers__ in the data.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""82. __Set__ the following __column labels/headers__:""")
    return


@app.cell
def _():
    labels_1 = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
    return


app._unparsable_cell(
    r"""
    #complete the code and run the cell!
    pd.read_csv(---)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""83. Once you are happy with the import, __save__ the DataFrame in the variable __cars__!""")
    return


app._unparsable_cell(
    r"""
    #complete the code and run the cell!
    cars = pd.read_csv(---)
    """,
    name="_"
)


@app.cell
def _(cars):
    # run the cell!
    cars.head()
    return


@app.cell
def _(cars):
    # run the cell!
    cars.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""84. __Export__ and __save__ cars as new csv-file (__cars_imp.csv__). Do __not__ export any __RangeIndex__!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""__Reimport__ cars_imp.csv and check!""")
    return


@app.cell
def _(pd):
    #run the cell!
    pd.read_csv("cars_imp.csv")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Well Done!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""----------------------------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Hints (Spoiler!)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""77. at this point, you should know this ;-) !""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""78. pd.read_csv("filename")""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""79. parameter skiprows""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""80. parameter skipfooter""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""81. header = N---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""82. parameter names""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""83. see hints 79-82""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""84. to_csv() method""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

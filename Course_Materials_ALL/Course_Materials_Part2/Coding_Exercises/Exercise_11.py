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
        ### Exercise 11: Cleaning messy Data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Full Data Workflow A-Z: Cleaning Data
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
        __Import__ the cars dataset from the csv-file __cars_unclean.csv__ and inspect. Then, __clean up__ the dataset:

        - Identify and handle __inconsistent data__
        - Each column/feature should have the __appropriate/most functional datatype__
        - Identify and handle __missing values__
        - Identify and handle __duplicates__
        - Have a closer look into columns with __strings__ and clean up
        - Identify and handle __erroneous outliers__ in numerical columns
        (hint: there might be a "fat finger" issue in one column and some value(s) in the mpg column could be in "gallons per mile" units)
        - __Save and export__ the cleaned dataset in a new csv-file (cars_clean.csv)
        - Change the datatype of appropriate columns to __categorical__.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        --------------------------
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
    # run the cell!
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return pd, plt


@app.cell
def _(pd):
    # run the cell!
    cars = pd.read_csv("cars_unclean.csv")
    return (cars,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ the DataFrame and identify obviously __inconsistent data__!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.head(20)
    return


@app.cell
def _(cars):
    # run the cell!
    cars.tail(10)
    return


@app.cell
def _(cars):
    # run the cell! 
    cars.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        85. __Identify__ one __column label__ that should be changed and adjust/__rename__ the column label! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.---(columns = {--- : ---}, inplace = True)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        86. Have a closer look to the __origin__ column by analyzing the __frequency/count__ of unique values! Can you find __any inconsistency__?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are the values ... usa and United States
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        87. __Replace__ the value __"United States"__ in the origin column! __Save__ the change!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Inspect and __identify__ the __problem__ in the column __horsepower__!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.horsepower.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Datatype should be ... numerical. But first of all, we need to remove...?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        88. Apply the appropriate __string operation__ to __remove "hp"__ from the horsepower column! Pay attention to __whitespaces__! __Overwrite__ the horsepower column!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell and inspect!
    cars.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Run and inspect, anything __strange__?
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.horsepower.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are 6 entries with the value ... "Not available"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        89. Create __"real" missing values__ in the column horsepower! __Save__ the change! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.horsepower.---(\"Not available\", ---, inplace = True)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        90. Now you can __convert the datatype__ in the column __horsepower__! __Overwrite__ the column!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Inspect!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.info()
    return


@app.cell
def _(cars):
    # run the cell!
    cars.head(7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Any __inconsistencies__ in the column __name__? Inspect one element! 
        """
    )
    return


@app.cell
def _(cars):
    #run the cell!
    cars.loc[4, "name"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It seems like some names are uppercase, while others are lowercase. And there are some excess whitespaces in the strings.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        91. __Convert__ all names to __lowercase__ and __remove all whitespaces__ on the left ends and right ends! __Overwrite!__
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Run the next two cells and identify (erroneous) outliers in the numercial columns!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.describe()
    return


@app.cell
def _(cars, plt):
    # run the cell!
    cars.plot(subplots = True, figsize = (15,12))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        92. Inspect the column __model_year__ in more detail by analyzing the __frequency/counts__ of unique values! Anything __strange__?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are 5 entries with ... 1973 instead of 73. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        93. __Replace__ the value __1973__! __Save__ the change!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        94. Inspect the column __weight__ by __sorting__ the values from __high to low__. Can you see the __extreme value__?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The by far highest value is ... 23000 lbs. Must be an error!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        95. __Select__ the complete __row__ of the outlier with the method __idxmax()__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It´s an opel manta ... could be a "fat finger" problem, weight could be 2300 instead of 23000.

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        96. __Overwrite__ the erroneous outlier! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[---, ---] = 2300
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Inspect the column __mpg__! Any strange __outlier__?
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.mpg.sort_values()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        An mpg of ... 0.060606 cannot be correct...
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        97. __Select__ the complete __row__ of the outlier with the method __idxmin()__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        98. After some research we have found out that this extreme value is in __"gallons per mile"__ units instead of "miles per gallon". <br>
        __Convert__ to __"miles per gallon"__ units! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[---, ---] = ---/cars.loc[---, ---]
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        99. Next, select all __rows__ with at least one __missing__/na value! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[cars.---.---]
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are 6 cars, where the horsepower is unknown.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        100. As horsepower is an important feature in the cars dataset, we decide to remove all 6 rows. __Remove__ and __save__ the change!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now let´s find __duplicates__. First, we need to understand __which columns__ we have to take into consideration to identify duplicates.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        101. The first __naive assumption__ is that two cars cannot have the __same name__. Let´s count the number of __name-duplicates__. __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.duplicated(--- = [---]).sum()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are ... 86 potential duplicates to remove.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        102. Let´s inspect the __duplicated pairs__ by selecting __all instances__ of a name duplicate! __Fill in the gaps__! <br>
        Should the __name__ be the __only criteria__ to identify duplicates?
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[cars.duplicated(--- = [---], --- = False)].sort_values(\"name\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        No! Cars can have several vintages/model_year and several variants with different technical specifications (e.g. weight, horsepower)  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        103. To be on the safe side, let´s include __all columns__ to identify duplicates. __Count__ the number of duplicates! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.---.---
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There are ... 10 potential duplicates.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        104. Let´s inspect the __duplicated pairs__ by selecting __all instances__ of a duplicate! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars.loc[cars.duplicated(---)].sort_values(\"name\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        All pairs seem to be real duplicates.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        105. __Drop one instance__ of each duplicated pair! __Save__ the change!
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
    # run the cell!
    cars.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        106. Our dataset seems to be pretty clean now! __Save__ and __export__ to a new csv-file (cars_clean.csv)! Do not export the RangeIndex!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Call the __describe()__ method on all __non-numerical columns__!
        """
    )
    return


@app.cell
def _(cars):
    # run the cell!
    cars.describe(include = "O")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Are there any __categorical features__ (only few unique values) where the datatype could be __converted to "category"__? <br>
        107. If so, __convert__ and __overwrite__ the column(s)!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__. Did we __reduce memory usage__?
        """
    )
    return


@app.cell
def _(cars):
    #run the cell!
    cars.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Yes, we reduced memory usage!
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
        -----------------------------------------
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
        85. rename() method, column "model year"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        86. value_counts() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        87. replace() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        88. string(str) method replace(), " hp"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        89. replace() method, np.nan
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        90. astype() method, "float"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        91. string(str) methods lower() and strip()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        92. value_counts() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        93. replace() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        94. sort_values() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        95. Filter cars with cars.weight.idxmax()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        96. cars.weight.idxmax(), "weight"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        97. Filter cars with cars.mpg.idxmin()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        98. cars.mpg.idxmin(), "mpg", 1/x
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        99. methods isna() and any()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        100. dropna() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        101. subset parameter, "name"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        102. keep parameter
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        103. methods duplicated() and sum()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        104. keep parameter
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        105. drop_duplicates() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        106. to_csv() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        107. astype() method
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

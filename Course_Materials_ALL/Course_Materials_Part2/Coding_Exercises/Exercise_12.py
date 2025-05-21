import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Coding Exercises (Part 1)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Full Data Workflow A-Z: Merging, Joining, Concatenating
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 12: Merging, joining, aligning and concatenating Data 
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
        ### Concatenating DataFrames vertically
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Import__ the cars dataset (with cars from usa and europe) from the csv-file __cars_clean.csv__. <br>
        Also __import__ the csv-file __cars_jap.csv__ (with cars from japan) and __concatenate__ both DataFrames __vertically__! <br>
        __Save__ the __concatenated DataFrame__ in the variable __cars_all__! <br>
        Finally, __sort__ cars_all by the model_year from __low to high__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Left Join
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Import__ the csv-files __summer.csv__ (as summer) and __dictionary.csv__ (as dic) which contains the __full country name__ for the olympic country codes as well as __population__ and __gdp__ statistics for some countries.<br>

        __"Copy and paste"__ the __full country name__, __population__ and __gdp__ from the dic DataFrame __into the summer DataFrame__ with a __Left Join__!<br>
        __Save__ the new merged DataFrame in the variable __summer_new__!<br>

        __Inspect__ summer_new and determine the __olympic country codes__ for which the dic DataFrame does __not provide__ any information!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Arithmetic operations between DataFrames / Alignment
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Import__ the csv-files __ath_2008.csv__ and __ath_2012.csv__ with all medals winners in the Sport __Athletics__ in the Editions __2008__ and __2012__.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For __all Athletes__ in the two DataFrames, __aggregate/add__ the total number of __Gold__, __Silver__ and __Bronze__ Medals over both editions! __Save__ the aggregated DataFrame in the variable __add__. (Hint: add should contain an index with the Athlete names and three columns, Gold, Silver, Bronze)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Sort__ add by Gold, Silver, Bronze from __high to low__! Change datatype to __integer__, if necessary! The first Athlete in your DataFrame should be ... no surprise ... Usain Bolt with 6 Gold and 0 Silver and Bronze Medals.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        -------------------------------------
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
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Concatenating DataFrames vertically
        """
    )
    return


@app.cell
def _(pd):
    #run the cell
    cars = pd.read_csv("cars_clean.csv")
    return (cars,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ the __cars__ DataFrame!
        """
    )
    return


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
        __Inspect__ the cars_jap DataFrame!
        """
    )
    return


@app.cell
def _(pd):
    #run the cell
    cars_jap = pd.read_csv("cars_jap.csv")
    return (cars_jap,)


@app.cell
def _(cars_jap):
    #run the cell
    cars_jap.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before we can concatenate both DataFrames, we need to __align__ them!<br>
        108. __Insert__ the column __origin__ to __cars_jap__ at the most appropriate position! __Fill in the gaps!__
        """
    )
    return


app._unparsable_cell(
    r"""
    cars_jap.---(---, ---, \"japan\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Also the column labels should match. <br>
        109. __Overwrite__ the column labels in __cars_jap__ and use the same column labels that we have in cars!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__!
        """
    )
    return


@app.cell
def _(cars_jap):
    #run the cell
    cars_jap.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        110. __Concatenate__ both DataFrames __vertically__ and create a __new RangeIndex__! __Save__ the new DataFrame in the variable __cars_all__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__!
        """
    )
    return


@app.cell
def _(cars_all):
    #run the cell
    cars_all.head()
    return


@app.cell
def _(cars_all):
    #run the cell!
    cars_all.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        111. __Sort cars_call__ by the __model_year__ from __low to high__! Create a __new RangeIndex__ (drop the old)! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    cars_all = cars_all.---(\"model_year\").---(drop = True)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__!
        """
    )
    return


@app.cell
def _(cars_all):
    #run the cell
    cars_all.head()
    return


@app.cell
def _(cars_all):
    #run the cell
    cars_all.tail()
    return


@app.cell
def _(cars_all):
    #run the cell
    cars_all.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ----------------------------------------------------------------------
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Left Join
        """
    )
    return


@app.cell
def _(pd):
    # run the cell!
    summer = pd.read_csv("summer.csv")
    return (summer,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ the __summer__ DataFrame!
        """
    )
    return


@app.cell
def _(summer):
    # run the cell!
    summer.head()
    return


@app.cell
def _(pd):
    # run the cell!
    dic = pd.read_csv("dictionary.csv")
    return (dic,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ dict!
        """
    )
    return


@app.cell
def _(dic):
    # run the cell!
    dic.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __dic__ contains the Olympic Games __Country Codes__ ("Code") with the corresponding __full country names__ ("Country") as well as recent __Population__ and __GDP__ statistics.<br>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        112. __Create__ the columns __Country__, __Population__ and __GDP per Capita__ in the __summer__ DataFrame by using a __Left Join__ with __pd.merge()__. <br>
        __Save__ the merged Dataframe in the variable __summer_new__! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    summer_new = pd.merge(---, ---, how = \"left\", left_on= ---, right_on = ---)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ summer_new!
        """
    )
    return


@app.cell
def _(summer_new):
    # run the cell!
    summer_new.head()
    return


@app.cell
def _(summer_new):
    # run the cell!
    summer_new.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Apparently, __dic__ does __not contain__ additional information for __all olympic country codes__ that are in the __summer__ Dataframe.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        113. __Filter__ summer_new for the elements in the column __Country_x__, where the __corresponding value__ in the column __Code__ is __missing__! <br>
        __Count__ the frequency! __Fill in the gaps__!
        """
    )
    return


app._unparsable_cell(
    r"""
    summer_new.loc[summer_new.Code.---, \"Country_x\"].---
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For these country codes, we need to find __other sources__ for additional information on the __full country name__, __population__ and __gdp__ (most of these countries do not exist any more.) -> BONUS EXERCISE ;-)
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
        ### Arithmetic operations between DataFrames / Alignment
        """
    )
    return


@app.cell
def _(pd):
    #run the cell
    ath_2008 = pd.read_csv("ath_2008.csv")
    ath_2012 = pd.read_csv("ath_2012.csv")
    return ath_2008, ath_2012


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ the __ath_2008__ DataFrame. It contains all athletes who won medals in __Athletics__ in the Edition __2008__.
        """
    )
    return


@app.cell
def _(ath_2008):
    #run the cell
    ath_2008.head()
    return


@app.cell
def _(ath_2008):
    #run the cell
    ath_2008.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__ the __ath_2012__ DataFrame. It contains all athletes who won medals in __Athletics__ in the Edition __2012__.
        """
    )
    return


@app.cell
def _(ath_2012):
    #run the cell
    ath_2012.head()
    return


@app.cell
def _(ath_2012):
    #run the cell
    ath_2012.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For __all Athletes__ in the two DataFrames, __aggregate/add__ the total number of __Gold__, __Silver__ and __Bronze__ Medals over both editions! __Save__ the aggregated DataFrame in the variable __add__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        114. First, __set__ the __Athlete__ column as the __index__ in both DataFrames! __Save__ the changes!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        115. __Add__ both DataFrames with the __most appropriate method__! __Save__ the resulting DataFrame in the variable __add__!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        __Inspect__!
        """
    )
    return


@app.cell
def _(add):
    #run the cell
    add.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        116. __Sort__ the athletes by the number of __Gold__, __Silver__ and __Bronze__ medals from __high to low__!<br>
        __Fill in the gaps!__ Who is the top athlete?
        """
    )
    return


app._unparsable_cell(
    r"""
    add = add.sort_values(---, ascending = ---).astype(\"int\")
    """,
    name="_"
)


@app.cell
def _(add):
    # run the cell!
    add.head()
    return


@app.cell
def _(add):
    # run the cell!
    add.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        No surprise, it´s Usain Bolt!
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
        ------------------------------------------------
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
        108. insert() method, index pos. 7
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        109. columns attribute
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        110. pd.concat() method, ignore index
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        111. methods sort_values() and reset_index()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        112. left DataFrame: summer, on "Country" and "Code"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        113. methods isnull() and value_counts()
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        114. set_index() method
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        115. add() method, fill_value = 0
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        116. pass a list of columns to sort_values() method (sequence matters!)
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

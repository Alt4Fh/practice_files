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
        ## Full Data Workflow A-Z: Advanced Visualization with Seaborn
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 16: Seaborn
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
        142. __Import__ the cars dataset and __drop__ any missing values (__cars.csv__)!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        143. __Create__ the following plot!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        144. __Create__ the following plot! Cars with the lowest __fuel efficiency__ come from...?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        145. __Create__ the following plot! Do you think that the lower fuel efficiency of us cars is __statistically significant__? 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        146. __Create__ the following plot! Do you think that manufacturers from __all three regions significantly increased fuel efficiency__ from 1970 till 1982?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        147. Create __similar plots__ (as above) with __horsepower__, __weight__ and __displacement__ on the y-axis! <br> Can you identify __differences__ in the ways how manufacturers managed to __increase fuel efficiency__?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        148. __Add__ a new column __"gpm"__ with fuel efficiency in gallons per 100 miles unit. __Drop__ the mpg column!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        149. __Create__ the following plot! Is there a __significant__ (linear) __relationship__ between horsepower and gpm?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        150. Also create the following plot!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        151. __Create__ the following __heatmap__ (correlation matrix)!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        152. __Drop__ the columns __displacement__ and __acceleration__ and create the following __pairplot__ (sns.pairplot) for cars (kind = scatter)! 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![image.png](attachment:image.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        153. __Run__ the cell and __inspect__!
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    # run!
    sns.set(font_scale=1.5)
    sns.pairplot(data = cars[["gpm", "horsepower", "origin"]], kind = "scatter", hue = "origin", aspect =2, height = 3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        -----------------
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
        ### No further guidance this time! Prepare yourself for the final challenge! (Take a look at the Hints, if necessary)
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
        142. cars.dropna(inplace= True)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        143. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    plt.figure(figsize=(12,8))
    sns.set(font_scale=1.5, palette="viridis")
    sns.countplot(data = cars, hue = "origin", x = "model_year")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        144. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    plt.figure(figsize=(12,8))
    sns.set(font_scale=1.5, palette="viridis")
    sns.violinplot(data = cars, x = "origin", y = "mpg", dodge = True)
    sns.swarmplot(data = cars, x = "origin", y = "mpg", dodge = True, color = "black")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        145. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    plt.figure(figsize=(12,8))
    sns.set(font_scale=1.5)
    sns.barplot(data = cars, x = "origin", y = "mpg", dodge = True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        146. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    plt.figure(figsize=(12,8))
    sns.set(font_scale=1.5)
    sns.pointplot(data = cars, x = "model_year", y = "mpg", hue = "origin", dodge = True, ci = 95)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        147. pass horsepower, weight & displacement to y!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        148. 1 / mpg * 100
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        149.  
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    sns.set(font_scale=1.5)
    sns.jointplot(data = cars, x = "horsepower", y = "gpm", height = 8, kind = "reg")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        150. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    sns.set(font_scale=1.5)
    sns.lmplot(data = cars, x = "weight", y = "horsepower", col = "origin")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        151.
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    plt.figure(figsize=(12,8))
    sns.set(font_scale=1.4)
    sns.heatmap(cars.corr(), annot= True, cmap = "Reds")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        152. 
        """
    )
    return


@app.cell
def _(cars, plt, sns):
    sns.set(font_scale=1.5)
    sns.pairplot(data = cars, kind = "scatter")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        153. Nothing to do!
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

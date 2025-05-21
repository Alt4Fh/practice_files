import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Coding Exercises (Part 1)""")
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
    mo.md(r"""If you need some further help or if you want to check your code, you can also watch the __solutions videos__ or check the __solutions notebook__.""")
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
    mo.md(r"""## Visualization with Matplotlib""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Exercise 9: Plotting Data with Matplotlib""")
    return


@app.cell
def _():
    # run the cell!
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # run the cell!
    cars = pd.read_csv("./Course_Materials_ALL/Course_Materials_Part1/Coding_Exercises/cars.csv")
    return (cars,)


@app.cell
def _(cars):
    # run the cell!
    cars.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""73. __Import__ matplotlib.pyplot (as plt) and set the __style__ to __"seaborn"__! __Fill in the gaps!__""")
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    plt.style.use("seaborn-v0_8")
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""74. __Create__ the graph below (lineplot for all numerical columns)!""")
    return


@app.cell
def _(cars, plt):
    import matplotlib
    matplotlib.rcParams.update({'font.size':20})
    cars.select_dtypes(include=['number']).plot(subplots=True, sharex=False, figsize=(16,16))
    plt.suptitle('Distribution')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""75. __Create__ the graph below (Histogramm for the __"mpg"__ column with 40 bins)!""")
    return


@app.cell
def _(cars, plt):
    cars['mpg'].hist(bins=40, edgecolor='red', linewidth=0.5, )
    plt.title('MPG distribution')
    plt.xlabel('MFG')
    plt.ylabel('frequency')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""76. __Create__ the graph below (Scatterplot with __horsepower__ and __mpg__)! __Fill in the gaps!__""")
    return


@app.cell
def _(cars, plt):
    # c='cylinders' maps each cylinder count to a color
    cars.plot(kind = 'scatter', x ='horsepower', y = 'mpg', figsize = (12,8) , marker = 's', c='cylinders', colormap = "viridis")
    plt.title('mpg vs horsepower', fontsize = 18)
    plt.xlabel("horsepower", fontsize = 15)
    plt.ylabel("mpg", fontsize = 15)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Well Done!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""-----------------------------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Hints (Spoiler!)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""73. plt.style.use()""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""74. plot() method, figure size = (15,15), subplots shall not share x-axis, don´t forget plt.show()""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""75. hist() method, plt.title(), plt.xlabel(), plt.ylabel(), plt.show(), fontsize for title: 15, fontsize for labels: 13, figure size: (12,8)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""76. "scatter" plot, color of points determined by cylinders column""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

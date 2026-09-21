import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    définition de la fonction fibonacci
    """)
    return


@app.function
def fibonacci(n):
    f_0 = 0
    f_1 = 1
    for i in range (n>=2):
        f_n = f_0 + f_1
        f_0 = f_1
        f_1 = f_n
    return (f_n)


if __name__ == "__main__":
    app.run()

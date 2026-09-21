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
def fibonacci(n:int):
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    et définition des tests
    """)
    return


@app.cell
def _():
    def test_fibonacci_0():
        assert fibonacci(0) == 0

    def test_fibonacci_1():
        assert fibonacci(1) == 1

    def test_fibonacci_3():
        assert fibonacci(3) == 2

    return


if __name__ == "__main__":
    app.run()

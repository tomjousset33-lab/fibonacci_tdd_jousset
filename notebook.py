import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This notebook is my first marimo notebook. Its purpose is to make me manipulate marimo but also the TDD. I will try these functionalities with a classic fibonacci function.
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition of the Fibonacci's function
    """)
    return


@app.function
def fibonacci(n:int):
    if n == 0:
        return 0
    if n == 1 :
        return 1
        
    f0 = 0
    f1 = 1
    for i in range(2, n+1):
        fn= f0 + f1
        f0 = f1
        f1 = fn
    return fn


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition of the tests
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


@app.function
def test_fibonacci_multiple():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    definition of a widget
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.number(start=0, stop=1000, value = 5)
    n
    return (n,)


@app.cell
def _(mo, n):
    mo.md(f"""
    Fibonacci({n.value}) = **{fibonacci(int(n.value))}**
    """)
    return


if __name__ == "__main__":
    app.run()

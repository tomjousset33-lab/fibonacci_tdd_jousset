# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "fibonacci-tdd-kata-jousset==0.1.0",
#     "marimo>=0.25.1",
# ]
# ///

import marimo

__generated_with = "0.24.2"

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):

    mo.md(r"""
    This notebook is my first marimo notebook. Its purpose is to make me
    manipulate marimo but also the TDD. I will try these functionalities
    with a classic fibonacci function.
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from fibonacci_tdd_kata import fibonacci

    return (fibonacci,)


@app.cell
def _(fibonacci):
    def test_fibonacci_0():
        assert fibonacci(0) == 0

    def test_fibonacci_1():
        assert fibonacci(1) == 1

    def test_fibonacci_3():
        assert fibonacci(3) == 2

    return


@app.cell
def _(fibonacci):
    def test_fibonacci_multiple():
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    definition of a widget
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.number(start=0, stop=1000, value=5)
    n
    return (n,)


@app.cell
def _(fibonacci, mo, n):
    mo.md(f"""
    Fibonacci({n.value}) = **{fibonacci(int(n.value))}**
    """)
    return


@app.cell
def _(fibonacci):
    def test_large_values():
        assert fibonacci(100000) > 1000000
        assert fibonacci(1000000) > fibonacci(999999)

    return


if __name__ == "__main__":
    app.run()

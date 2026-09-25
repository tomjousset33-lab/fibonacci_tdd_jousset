import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This notebook is my first marimo notebook. Its purpose is to make me manipulate marimo but also the TDD. I will try these functionalities with a classic fibonacci function.
    """)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition of the Fibonacci's function
    """)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now that we want to optimize the computation time of the execution of Fibonacci's function on large values, we need to refactor our function. That's why we used fast_doubling here. This method permits to reduce the complexity from O(n) to O(log n), by dividing the main computation by two others computation. For n=1000000, we will only have to deal with log2(1000000) levels of recursion (about 20) instead of 1000000 iterations !
    """)


@app.function
def fibonacci(n: int):
    if n == 0:
        return 0

    def fast_doubling(n):
        if n == 1:
            return (1, 1)

        a, b = fast_doubling(n // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fast_doubling(n)[0]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definition of the tests
    """)


@app.cell
def _():
    def test_fibonacci_0():
        assert fibonacci(0) == 0

    def test_fibonacci_1():
        assert fibonacci(1) == 1

    def test_fibonacci_3():
        assert fibonacci(3) == 2



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


@app.function
def test_large_values():
    assert fibonacci(100000) > 1000000
    assert fibonacci(1000000) > fibonacci(999999)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before optimization, the time to pass all the tests was more than 15 seconds and now it is done in a one second time ! This optimization is huge.
    """)


if __name__ == "__main__":
    app.run()

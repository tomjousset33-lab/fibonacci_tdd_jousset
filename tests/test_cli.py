import pytest

from fibonacci_tdd_kata.cli import main


def test_cli_single_number(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "10"])

    main()

    assert capsys.readouterr().out == "55\n"


def test_cli_range(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "0", "--end", "5"],
    )

    main()

    assert capsys.readouterr().out == "0\n1\n1\n2\n3\n5\n"


@pytest.mark.parametrize(
    "args",
    [
        ["fibonacci-kata"],
        ["fibonacci-kata", "--start", "0"],
        ["fibonacci-kata", "--start", "5", "--end", "2"],
    ],
)
def test_cli_invalid_arguments(monkeypatch, args):
    monkeypatch.setattr("sys.argv", args)

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

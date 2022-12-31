import pandas as pd


def test_logs():
    """Very simple initial test: check for CSV file"""
    df=pd.read_csv("training.log")
    assert df.empty == False

def test_cool_stuff():
    """WIP: Use data analysis techniques on our logs!"""
    pass


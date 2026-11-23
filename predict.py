"""Deliberately broken: a test case for haggle's ship checks (Hour Detective). Its requirements.txt names a package that isn't on PyPI, so the install fails."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
pd.DataFrame({"project_id": test["project_id"], "hours_spent": train["hours_spent"].mean()}).to_csv("predictions.csv", index=False)

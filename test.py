import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    for i in range(len(employees)):
        if (employees.iloc[i]['employee_id'] % 2 == 1) and (employees.iloc[i]["name"][0] != "M"):
            employees.at[i, "bonus"] = 2 * employees.iloc[i]["salary"]

    return employees[["employee_id","bonus"]]
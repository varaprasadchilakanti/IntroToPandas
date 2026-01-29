#!/usr/bin/env python3
"""
2881. Create a New Column

DataFrame employees
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+
A company plans to provide its employees with a bonus.
Write a solution to create a new column name bonus that contains the doubled values of the salary column.
The result format is in the following example.

Example 1:
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
Output:
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
Explanation: 
A new column bonus is created by doubling the value in the column salary.

Hint 1
Consider using the `[]` brackets with the new column name at the left side of the assignment. The calculation of the value is done element-wise.



Developer Insights
Problem Nature
We must add a new column bonus to a DataFrame, where each value is double the salary.
This is a data transformation problem under the Intro to Pandas study plan.

Key Observations
Pandas supports vectorized arithmetic: df["salary"] * 2.
New columns can be created by assignment: df["bonus"] = ....
This operation is element‑wise and efficient.

Strategy
Accept DataFrame employees.
Compute employees["salary"] * 2.
Assign result to new column employees["bonus"].
Return updated DataFrame.

Complexity
Time: O(n) for n rows (vectorized, highly optimized).
Space: O(n) for new column.

Edge Cases
Empty DataFrame → returns empty DataFrame with new column bonus.
Negative salaries → bonus column reflects doubled negative values.
Missing salary column → raises KeyError (expected, schema defined).

Pseudocode
function createBonusColumn(employees):
    employees["bonus"] = employees["salary"] * 2
    return employees

"""

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'bonus' by doubling the salary.

    Args:
        employees (pd.DataFrame): Input DataFrame containing employee data
            with columns ['name', 'salary'].

    Returns:
        pd.DataFrame: Updated DataFrame with new column 'bonus'.

    Design:
        - Uses vectorized arithmetic for efficiency.
        - Assigns new column via bracket notation.
        - Preserves existing DataFrame structure.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame with 'bonus' column.
        - Negative salaries → doubled negative values.
        - Missing 'salary' column → raises KeyError.
    """
    employees["bonus"] = employees["salary"] * 2
    return employees


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
        "salary": [4548, 28150, 1103, 6593, 74576, 24433]
    }
    df = pd.DataFrame(data)
    print(createBonusColumn(df))
    # Expected Output:
    #       name  salary   bonus
    # 0    Piper    4548    9096
    # 1    Grace   28150   56300
    # 2  Georgia    1103    2206
    # 3   Willow    6593   13186
    # 4     Finn   74576  149152
    # 5   Thomas   24433   48866

#!/usr/bin/env python3
"""
2884. Modify Columns

DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
A company intends to give its employees a pay rise.
Write a solution to modify the salary column by multiplying each salary by 2.
The result format is in the following example.


Example 1:
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
Explanation:
Every salary has been doubled.

Hint 1
Considering multiplying each salary value by 2, using a simple assignment operation. The calculation of the value is done column-wise.


Developer Insights
Problem Nature
We must update an existing column (salary) by multiplying each value by 2.
This is a data cleaning/transformation problem under the Intro to Pandas study plan.

Key Observations
Pandas supports vectorized arithmetic: df["salary"] * 2.
Assignment back to the same column updates values in place.
This is efficient and avoids explicit loops.

Strategy
Accept DataFrame employees.
Compute employees["salary"] * 2.
Assign result back to employees["salary"].
Return updated DataFrame.

Complexity
Time: O(n) for n rows (vectorized, highly optimized).
Space: O(1) additional memory (in‑place update).

Edge Cases
Empty DataFrame → returns empty DataFrame unchanged.
Negative salaries → doubled negative values.
Missing salary column → raises KeyError (expected, schema defined).
Non‑integer salaries (floats) → handled correctly, doubled values preserved.

Pseudocode
function modifySalaryColumn(employees):
    employees["salary"] = employees["salary"] * 2
    return employees

"""

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Modify the 'salary' column by doubling its values.

    Args:
        employees (pd.DataFrame): Input DataFrame containing employee data
            with columns ['name', 'salary'].

    Returns:
        pd.DataFrame: Updated DataFrame with modified 'salary' column.

    Design:
        - Uses vectorized arithmetic for efficiency.
        - Updates column in place for clarity and minimal memory use.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame unchanged.
        - Negative salaries → doubled negative values.
        - Missing 'salary' column → raises KeyError.
        - Float salaries → doubled correctly.
    """
    employees["salary"] = employees["salary"] * 2
    return employees


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "name": ["Jack", "Piper", "Mia", "Ulysses"],
        "salary": [19666, 74754, 62509, 54866],
    }
    df = pd.DataFrame(data)
    print(modifySalaryColumn(df))
    # Expected Output:
    #       name  salary
    # 0     Jack   39332
    # 1    Piper  149508
    # 2      Mia  125018
    # 3  Ulysses  109732

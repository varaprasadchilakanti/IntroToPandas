#!/usr/bin/env python3
"""
2883. Drop Missing Data

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
There are some rows having missing values in the name column.
Write a solution to remove the rows with missing values.
The result format is in the following example.

Example 1:

Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 779        | Georgia | 20  | 
| 849        | Willow  | 14  | 
+------------+---------+-----+
Explanation: 
Student with id 217 havs empty value in the name column, so it will be removed.

Hint 1
Consider using a build-in function in pandas library to remove the rows with missing values based on specified data.


Developer Insights
Problem Nature
We must remove rows from a DataFrame where the name column contains missing values (None or NaN).
This is a data cleaning problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.dropna(subset=[...]) to remove rows with missing values in specific columns.
subset=["name"] ensures only rows missing name are dropped.
Operation is stable: preserves row order and other columns.

Strategy
Accept DataFrame students.
Apply dropna(subset=["name"]).
Return cleaned DataFrame.

Complexity
Time: O(n) for n rows (scan for missing values).
Space: O(n) for intermediate structures.

Edge Cases
Empty DataFrame → returns empty DataFrame.
No missing values → returns original DataFrame unchanged.
All rows missing name → returns empty DataFrame.
Mixed missing values in other columns → unaffected, since only name is checked.

Pseudocode
function dropMissingData(students):
    return students.dropna(subset=["name"])

"""

#!/usr/bin/env python3
"""
2883. Drop Missing Data

Remove rows in a DataFrame where the 'name' column has missing values.
"""

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows with missing values in the 'name' column.

    Args:
        students (pd.DataFrame): Input DataFrame containing student data
            with columns ['student_id', 'name', 'age'].

    Returns:
        pd.DataFrame: DataFrame with rows removed where 'name' is missing.

    Design:
        - Uses DataFrame.dropna with subset=['name'].
        - Ensures stable ordering (other rows unaffected).
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - No missing values → returns original DataFrame unchanged.
        - All rows missing 'name' → returns empty DataFrame.
    """
    return students.dropna(subset=["name"])


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "student_id": [32, 217, 779, 849],
        "name": ["Piper", None, "Georgia", "Willow"],
        "age": [5, 19, 20, 14],
    }
    df = pd.DataFrame(data)
    print(dropMissingData(df))
    # Expected Output:
    #    student_id     name  age
    # 0          32    Piper    5
    # 2         779  Georgia   20
    # 3         849   Willow   14

#!/usr/bin/env python3
"""
2886. Change Data Type

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:
The grade column is stored as floats, convert it to integers.
The result format is in the following example.


Example 1:
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
Explanation: 
The data types of the column grade is converted to int.

Hint 1
Consider using a build-in function in pandas library with a dictionary to convert the datatype of columns as specified.


Developer Insights
Problem Nature
We must correct the schema of a DataFrame:
The grade column is stored as float.
Requirement: convert grade to int.
This is a data cleaning problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.astype() for type conversion.
Dictionary mapping allows selective conversion: df.astype({"grade": "int"}).
Conversion is element‑wise and efficient.
Preserves other columns unchanged.

Strategy
Accept DataFrame students.
Apply students.astype({"grade": "int"}).
Return updated DataFrame.

Complexity
Time: O(n) for n rows (conversion applied element‑wise).
Space: O(n) for new column representation.

Edge Cases
Empty DataFrame → returns empty DataFrame unchanged.
Already integer grade → no change.
Non‑numeric values in grade → raises ValueError (expected, schema defined).
Large floats → truncated to integer (floor semantics).

Pseudocode
function changeDatatype(students):
    return students.astype({"grade": "int"})

"""


import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    Change the data type of the 'grade' column from float to int.

    Args:
        students (pd.DataFrame): Input DataFrame containing student data
            with columns ['student_id', 'name', 'age', 'grade'].

    Returns:
        pd.DataFrame: DataFrame with 'grade' column converted to int.

    Design:
        - Uses DataFrame.astype with dictionary mapping.
        - Ensures only 'grade' column is affected.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame unchanged.
        - Already integer column → no change.
        - Non-numeric values in 'grade' → raises ValueError.
        - Large floats → truncated to integer.
    """
    return students.astype({"grade": "int"})


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "student_id": [1, 2],
        "name": ["Ava", "Kate"],
        "age": [6, 15],
        "grade": [73.0, 87.0],
    }
    df = pd.DataFrame(data)
    print(changeDatatype(df))
    # Expected Output:
    #    student_id   name  age  grade
    # 0           1    Ava    6     73
    # 1           2   Kate   15     87

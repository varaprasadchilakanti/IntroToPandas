#!/usr/bin/env python3
"""
2885. Rename Columns

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
Write a solution to rename the columns as follows:

id to student_id
first to first_name
last to last_name
age to age_in_years
The result format is in the following example.


Example 1:
Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
Output:
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
Explanation: 
The column names are changed accordingly.

Hint 1
Consider using a build-in function in pandas library with a dictionary to rename the columns as specified.


Developer Insights
Problem Nature
We must rename DataFrame columns according to a mapping:
id → student_id
first → first_name
last → last_name
age → age_in_years
This is a data cleaning problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.rename(columns={...}, inplace=False) for renaming.
Dictionary mapping ensures clarity and extensibility.
Operation is non‑destructive unless inplace=True.

Strategy
Accept DataFrame students.
Define mapping dictionary for column renames.
Apply students.rename(columns=mapping).
Return updated DataFrame.

Complexity
Time: O(k) for k columns (rename is metadata operation).
Space: O(1).

Edge Cases
Empty DataFrame → returns empty DataFrame with renamed columns.
Missing columns in mapping → unaffected, only specified columns renamed.
Extra columns → preserved unchanged.

Pseudocode
function renameColumns(students):
    mapping = {
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    }
    return students.rename(columns=mapping)

"""


import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Rename specific columns in the DataFrame.

    Args:
        students (pd.DataFrame): Input DataFrame containing student data
            with columns ['id', 'first', 'last', 'age'].

    Returns:
        pd.DataFrame: DataFrame with renamed columns:
            ['student_id', 'first_name', 'last_name', 'age_in_years'].

    Design:
        - Uses DataFrame.rename with dictionary mapping.
        - Non-destructive: returns new DataFrame by default.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame with renamed columns.
        - Missing columns → unaffected.
        - Extra columns → preserved unchanged.
    """
    mapping = {
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years",
    }
    return students.rename(columns=mapping)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "id": [1, 2, 3, 4, 5],
        "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
        "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
        "age": [6, 7, 16, 18, 10],
    }
    df = pd.DataFrame(data)
    print(renameColumns(df))
    # Expected Output:
    #    student_id first_name last_name  age_in_years
    # 0           1      Mason      King             6
    # 1           2        Ava    Wright             7
    # 2           3     Taylor      Hall            16
    # 3           4    Georgia  Thompson            18
    # 4           5     Thomas     Moore            10

#!/usr/bin/env python3
"""
2880. Select Data

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
Write a solution to select the name and age of the student with student_id = 101.
The result format is in the following example.

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.

Hint 1
Consider applying both row and column filtering to select the desired data.


Developer Insights
Problem Nature
We must filter a DataFrame to select specific rows and columns:
Row condition: student_id == 101.
Columns: ["name", "age"].
This is a data selection problem under the Intro to Pandas study plan.

Key Observations
Pandas supports boolean indexing for row filtering.
Column selection can be done by passing a list of column names.
Combined: students.loc[students["student_id"] == 101, ["name", "age"]].

Strategy
Accept DataFrame students.
Apply row filter: students["student_id"] == 101.
Select columns: ["name", "age"].
Return resulting DataFrame.

Complexity
Time: O(n) for row filtering.
Space: O(k) for result subset.

Edge Cases
No student with student_id = 101 → returns empty DataFrame with correct columns.
Multiple rows with student_id = 101 → returns all matches.
DataFrame missing name or age columns → raises KeyError (expected, since schema is defined).

Pseudocode
function selectData(students):
    return students.loc[students["student_id"] == 101, ["name", "age"]]

"""


import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Select the name and age of the student with student_id = 101.

    Args:
        students (pd.DataFrame): Input DataFrame containing student data
            with columns ['student_id', 'name', 'age'].

    Returns:
        pd.DataFrame: A DataFrame containing the filtered row(s) with
        columns ['name', 'age'].

    Design:
        - Uses boolean indexing for row filtering.
        - Uses column selection for narrowing to ['name', 'age'].
        - Preserves DataFrame structure.

    Edge Cases:
        - No match → returns empty DataFrame with correct columns.
        - Multiple matches → returns all matching rows.
    """
    return students.loc[students["student_id"] == 101, ["name", "age"]]


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "student_id": [101, 53, 128, 3],
        "name": ["Ulysses", "William", "Henry", "Henry"],
        "age": [13, 10, 6, 11]
    }
    df = pd.DataFrame(data)
    print(selectData(df))
    # Expected Output:
    #       name  age
    # 0  Ulysses   13

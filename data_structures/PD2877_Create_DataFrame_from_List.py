#!/usr/bin/env python3
"""
2877. Create a DataFrame from List

Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
The result format is in the following example.

Example 1:
Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.

Hint 1
Consider using a built-in function in pandas library and specifying the column names within it.

Developer Insights
Problem Nature
We must transform a 2D list of student data into a Pandas DataFrame with columns student_id and age.
This is a data structure construction problem under the Pandas introduction track.

Key Observations
Pandas provides pd.DataFrame(data, columns=...) for direct construction.
Input is guaranteed to be a 2D list of integers.
Order must be preserved.
Column names must be explicitly set.

Strategy
Accept student_data (List[List[int]]).
Use pd.DataFrame(student_data, columns=["student_id", "age"]).
Return DataFrame.

Complexity
Time: O(n) to build DataFrame.
Space: O(n) for storage.

Edge Cases
Empty list → returns empty DataFrame with correct columns.
Single row → DataFrame with one entry.
Large list → handled efficiently by Pandas.

Pseudocode
function createDataframe(student_data):
    df = DataFrame(student_data, columns=["student_id", "age"])
    return df

"""

from typing import List
import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """
    Create a Pandas DataFrame from a 2D list of student data.

    Args:
        student_data (List[List[int]]): 2D list where each inner list
            contains [student_id, age].

    Returns:
        pd.DataFrame: DataFrame with columns ['student_id', 'age'].

    Design:
        - Uses pd.DataFrame constructor.
        - Explicitly sets column names.
        - Preserves input order.

    Edge Cases:
        - Empty list → returns empty DataFrame with correct columns.
        - Single row → returns DataFrame with one entry.
    """
    return pd.DataFrame(student_data, columns=["student_id", "age"])


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    df = createDataframe(student_data)
    print(df)
    # Expected Output:
    #    student_id  age
    # 0           1   15
    # 1           2   11
    # 2           3   11
    # 3           4   20

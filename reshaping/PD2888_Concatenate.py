#!/usr/bin/env python3
"""
2888. Reshape Data: Concatenate

DataFrame df1
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame df2
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
Write a solution to concatenate these two DataFrames vertically into one DataFrame.
The result format is in the following example.


Example 1:
Input:
df1
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
df2
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
Explanation:
The two DataFramess are stacked vertically, and their rows are combined.

Hint 1
Consider using a built-in function in pandas library with the appropriate axis argument.


Developer Insights
Problem Nature
We must concatenate two DataFrames vertically (row stacking).
This is a reshaping problem under the Intro to Pandas study plan.

Key Observations
Pandas provides pd.concat([df1, df2], axis=0) for vertical concatenation.
ignore_index=True resets the index for a clean continuous sequence.
Concatenation preserves schema if both DataFrames share the same columns.

Strategy
Accept DataFrames df1 and df2.
Use pd.concat([df1, df2], axis=0, ignore_index=True).
Return the concatenated DataFrame.

Complexity
Time: O(n+m) for n and m rows.
Space: O(n+m) for combined DataFrame.

Edge Cases
Empty df1 or df2 → returns the other DataFrame unchanged.
Both empty → returns empty DataFrame.
Different column sets → missing columns filled with NaN.
Duplicate rows → preserved (no deduplication).


Pseudocode
function concatenateTables(df1, df2):
    return pd.concat([df1, df2], axis=0, ignore_index=True)

"""


import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenate two DataFrames vertically.

    Args:
        df1 (pd.DataFrame): First DataFrame with schema ['student_id', 'name', 'age'].
        df2 (pd.DataFrame): Second DataFrame with same schema.

    Returns:
        pd.DataFrame: Concatenated DataFrame with rows from df1 followed by df2.

    Design:
        - Uses pd.concat with axis=0 for vertical stacking.
        - ignore_index=True ensures continuous index.
        - Preserves schema and column order.

    Edge Cases:
        - Empty df1 or df2 → returns the other DataFrame unchanged.
        - Both empty → returns empty DataFrame.
        - Different columns → missing values filled with NaN.
    """
    return pd.concat([df1, df2], axis=0, ignore_index=True)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df1 = pd.DataFrame({
        "student_id": [1, 2, 3, 4],
        "name": ["Mason", "Ava", "Taylor", "Georgia"],
        "age": [8, 6, 15, 17],
    })
    df2 = pd.DataFrame({
        "student_id": [5, 6],
        "name": ["Leo", "Alex"],
        "age": [7, 7],
    })
    print(concatenateTables(df1, df2))
    # Expected Output:
    #    student_id     name  age
    # 0           1    Mason    8
    # 1           2      Ava    6
    # 2           3   Taylor   15
    # 3           4  Georgia   17
    # 4           5      Leo    7
    # 5           6     Alex    7

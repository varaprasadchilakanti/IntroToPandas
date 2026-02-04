#!/usr/bin/env python3
"""
2890. Reshape Data: Melt

DataFrame report
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.
The result format is in the following example.

Example 1:

Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
Output:
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
Explanation:
The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

Hint 1
Consider using a built-in function in pandas library to transform the data


Developer Insights
Problem Nature
We must reshape a wide DataFrame (columns for each quarter) into a long format where:
Each row represents a product’s sales in a specific quarter.
Columns: product, quarter, sales.
This is a reshaping problem under the Intro to Pandas study plan.

Key Observations
Pandas provides pd.melt() for wide → long transformations.
id_vars=["product"] keeps product as identifier.
value_vars=["quarter_1","quarter_2","quarter_3","quarter_4"] specifies columns to unpivot.
var_name="quarter", value_name="sales" rename melted columns.

Strategy
Accept DataFrame report.
Apply pd.melt() with proper arguments.
Return reshaped DataFrame.

Complexity
Time: O(n·m) for n rows and m melted columns.
Space: O(n·m) for reshaped DataFrame.

Edge Cases
Empty DataFrame → returns empty DataFrame.
Missing values in quarters → preserved as NaN.
Additional columns → unaffected if not in value_vars.
Non‑numeric sales → preserved as is.

Pseudocode
function meltTable(report):
    return pd.melt(
        report,
        id_vars=["product"],
        value_vars=["quarter_1","quarter_2","quarter_3","quarter_4"],
        var_name="quarter",
        value_name="sales"
    )

"""


import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape the report DataFrame from wide to long format.

    Args:
        report (pd.DataFrame): Input DataFrame with columns
            ['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'].

    Returns:
        pd.DataFrame: Melted DataFrame with columns:
            ['product', 'quarter', 'sales'].

    Design:
        - Uses pd.melt for wide → long transformation.
        - Keeps 'product' as identifier.
        - Renames melted columns to 'quarter' and 'sales'.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - Missing values → preserved as NaN.
        - Extra columns → unaffected if not in value_vars.
    """
    return pd.melt(
        report,
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales",
    )


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "product": ["Umbrella", "SleepingBag"],
        "quarter_1": [417, 800],
        "quarter_2": [224, 936],
        "quarter_3": [379, 93],
        "quarter_4": [611, 875],
    }
    df = pd.DataFrame(data)
    print(meltTable(df))
    # Expected Output:
    #       product    quarter  sales
    # 0    Umbrella  quarter_1    417
    # 1 SleepingBag  quarter_1    800
    # 2    Umbrella  quarter_2    224
    # 3 SleepingBag  quarter_2    936
    # 4    Umbrella  quarter_3    379
    # 5 SleepingBag  quarter_3     93
    # 6    Umbrella  quarter_4    611
    # 7 SleepingBag  quarter_4    875

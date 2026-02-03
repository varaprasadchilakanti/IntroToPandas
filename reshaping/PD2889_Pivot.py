#!/usr/bin/env python3
"""
2889. Reshape Data: Pivot

DataFrame weather
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
The result format is in the following example.


Example 1:
Input:
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
Output:
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
Explanation:
The table is pivoted, each column represents a city, and each row represents a specific month.

Hint 1
Consider using a built-in function in pandas library to transform the data


Developer Insights
Problem Nature
We must pivot a DataFrame so that:
Each row represents a month.
Each city becomes a separate column.
Values are the corresponding temperature.
This is a reshaping problem under the Intro to Pandas study plan.

Key Observations
Pandas provides DataFrame.pivot(index=..., columns=..., values=...).
index="month", columns="city", values="temperature".
Pivoting transforms long format → wide format.
Resulting DataFrame has months as rows, cities as columns.

Strategy
Accept DataFrame weather.
Apply weather.pivot(index="month", columns="city", values="temperature").
Reset index if needed for clean tabular output.
Return pivoted DataFrame.

Complexity
Time: O(n) for n rows (pivoting requires grouping).
Space: O(n) for reshaped DataFrame.

Edge Cases
Empty DataFrame → returns empty DataFrame.
Duplicate entries for same (month, city) → raises ValueError (must aggregate first).
Missing values → filled with NaN.
Unsorted months → preserved as they appear; can be sorted if required.

Pseudocode
function pivotTable(weather):
    return weather.pivot(index="month", columns="city", values="temperature").reset_index()

"""


import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot the weather DataFrame.

    Args:
        weather (pd.DataFrame): Input DataFrame with columns
            ['city', 'month', 'temperature'].

    Returns:
        pd.DataFrame: Pivoted DataFrame with:
            - index: month
            - columns: cities
            - values: temperature

    Design:
        - Uses DataFrame.pivot for long → wide transformation.
        - Keeps 'month' as index to avoid extra 'index' column.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - Duplicate (month, city) pairs → raises ValueError.
        - Missing values → filled with NaN.
    """
    return weather.pivot(index="month", columns="city", values="temperature")


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "city": [
            "Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville",
            "ElPaso", "ElPaso", "ElPaso", "ElPaso", "ElPaso"
        ],
        "month": ["January", "February", "March", "April", "May",
                  "January", "February", "March", "April", "May"],
        "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43],
    }
    df = pd.DataFrame(data)
    print(pivotTable(df))
    # Expected Output:
    # city      ElPaso  Jacksonville
    # month                           
    # April          2             5
    # February       6            23
    # January       20            13
    # March         26            38
    # May           43            34

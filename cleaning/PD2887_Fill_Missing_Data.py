#!/usr/bin/env python3
"""
2887. Fill Missing Data

DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.


Example 1:
Input:+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Explanation: 
The quantity for Wristwatch and WirelessEarbuds are filled by 0.

Hint 1
Consider using a build-in function in pandas library to fill the missing values of specified columns.


Developer Insights
Problem Nature
We must fill missing values in the quantity column with 0.
This is a data cleaning problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.fillna(value, inplace=False) for filling missing values.
Selective filling can be done with df["quantity"].fillna(0).
Operation is element‑wise and efficient.

Strategy
Accept DataFrame products.
Apply products["quantity"].fillna(0).
Assign result back to products["quantity"].
Return updated DataFrame.

Complexity
Time: O(n) for n rows (scan and fill).
Space: O(1) additional memory (in‑place update).

Edge Cases
Empty DataFrame → returns empty DataFrame unchanged.
No missing values → returns original DataFrame unchanged.
All values missing in quantity → filled entirely with 0.
Mixed missing values in other columns → unaffected, since only quantity is filled.

Pseudocode
function fillMissingValues(products):
    products["quantity"] = products["quantity"].fillna(0)
    return products

"""


import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the 'quantity' column with 0.

    Args:
        products (pd.DataFrame): Input DataFrame containing product data
            with columns ['name', 'quantity', 'price'].

    Returns:
        pd.DataFrame: DataFrame with missing values in 'quantity' replaced by 0.

    Design:
        - Uses Series.fillna for targeted column filling.
        - Updates column in place for clarity and minimal memory use.
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame unchanged.
        - No missing values → returns original DataFrame unchanged.
        - All values missing in 'quantity' → filled entirely with 0.
    """
    products["quantity"] = products["quantity"].fillna(0)
    return products


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
        "quantity": [None, None, 779, 849],
        "price": [135, 821, 9319, 3051],
    }
    df = pd.DataFrame(data)
    print(fillMissingValues(df))
    # Expected Output:
    #              name  quantity  price
    # 0      Wristwatch         0    135
    # 1 WirelessEarbuds         0    821
    # 2       GolfClubs       779   9319
    # 3        Printer       849   3051

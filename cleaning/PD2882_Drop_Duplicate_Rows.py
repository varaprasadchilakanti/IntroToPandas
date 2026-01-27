#!/usr/bin/env python3
"""
2882. Drop Duplicate Rows

DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
There are some duplicate rows in the DataFrame based on the email column.
Write a solution to remove these duplicate rows and keep only the first occurrence.
The result format is in the following example.


Example 1:
Input:
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Output:  
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Explanation:
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

Hint 1
Consider using a build-in function in pandas library to remove the duplicate rows based on specified data.


Developer Insights
Problem Nature
We must remove duplicate rows in a DataFrame based on the email column, keeping only the first occurrence.
This is a data cleaning problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.drop_duplicates(subset=..., keep=...).
subset="email" ensures duplicates are detected only on the email column.
keep="first" retains the first occurrence and drops subsequent ones.
Operation is stable: preserves original row order.

Strategy
Accept DataFrame customers.
Apply drop_duplicates(subset=["email"], keep="first").
Return cleaned DataFrame.

Complexity
Time: O(n) for n rows (hash‑based duplicate detection).
Space: O(n) for intermediate structures.

Edge Cases
Empty DataFrame → returns empty DataFrame.
No duplicates → returns original DataFrame unchanged.
All rows duplicate on email → only first row retained.
Mixed duplicates with different customer_id or name → only first email occurrence kept.

Pseudocode
function dropDuplicateEmails(customers):
    return customers.drop_duplicates(subset=["email"], keep="first")

"""


import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Drop duplicate rows based on the 'email' column.

    Args:
        customers (pd.DataFrame): Input DataFrame containing customer data
            with columns ['customer_id', 'name', 'email'].

    Returns:
        pd.DataFrame: DataFrame with duplicates removed, keeping only the
        first occurrence of each email.

    Design:
        - Uses DataFrame.drop_duplicates with subset=['email'].
        - Ensures stable ordering (first occurrence retained).
        - Preserves schema and column order.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - No duplicates → returns original DataFrame unchanged.
        - All rows duplicate → only first row retained.
    """
    return customers.drop_duplicates(subset=["email"], keep="first")


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "customer_id": [1, 2, 3, 4, 5, 6],
        "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        "email": [
            "emily@example.com",
            "michael@example.com",
            "sarah@example.com",
            "john@example.com",
            "john@example.com",
            "alice@example.com",
        ],
    }
    df = pd.DataFrame(data)
    print(dropDuplicateEmails(df))
    # Expected Output:
    #    customer_id     name               email
    # 0            1     Ella   emily@example.com
    # 1            2    David michael@example.com
    # 2            3  Zachary   sarah@example.com
    # 3            4    Alice     john@example.com
    # 5            6   Violet   alice@example.com

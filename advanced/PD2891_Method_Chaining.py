#!/usr/bin/env python3
"""
2891. Method Chaining

DataFrame animals
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |
+-------------+--------+
Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
Return the animals sorted by weight in descending order.
The result format is in the following example.


Example 1:

Input: 
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
Output: 
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
Explanation: 
All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight.

In Pandas, method chaining enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 
Can you complete this task in just one line of code using method chaining?


Developer Insights
Problem Nature
We must filter animals weighing strictly more than 100 kilograms, sort them by weight in descending order, and return only their names.
This is an advanced Pandas problem emphasizing method chaining for clarity and reproducibility.

Key Observations
Pandas supports boolean indexing: df[df["weight"] > 100].
Sorting: .sort_values(by="weight", ascending=False).
Column selection: [["name"]].
Method chaining allows combining these operations into a single pipeline without intermediate variables.

Strategy
Accept DataFrame animals.
Filter rows where weight > 100.
Sort by weight descending.
Select only the name column.
Return result.

Complexity
Time: O(n log n) due to sorting.
Space: O(n) for filtered DataFrame.

Edge Cases
Empty DataFrame → returns empty DataFrame.
No animals above 100 kg → returns empty DataFrame.
Duplicate weights → stable sort preserves relative order.
Non‑numeric weights → raises error (schema defined as int).

Pseudocode
function findHeavyAnimals(animals):
    return animals[animals["weight"] > 100]
             .sort_values(by="weight", ascending=False)
             [["name"]]


"""


import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    Find heavy animals (>100 kg) and return their names sorted by weight descending.

    Args:
        animals (pd.DataFrame): Input DataFrame with columns
            ['name', 'species', 'age', 'weight'].

    Returns:
        pd.DataFrame: DataFrame containing only the 'name' column of animals
            weighing strictly more than 100 kg, sorted by weight descending.

    Design:
        - Uses method chaining for clarity and reproducibility.
        - Filters with boolean indexing.
        - Sorts with sort_values.
        - Selects only 'name' column.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - No animals above 100 kg → returns empty DataFrame.
        - Duplicate weights → stable sort preserves relative order.
    """
    return (
        animals[animals["weight"] > 100]
        .sort_values(by="weight", ascending=False)[["name"]]
    )


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
        "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
        "age": [98, 50, 6, 45, 100, 26],
        "weight": [464, 41, 328, 463, 50, 349],
    }
    df = pd.DataFrame(data)
    print(findHeavyAnimals(df))
    # Expected Output:
    #        name
    # 0   Tatiana
    # 3  Jonathan
    # 5     Tommy
    # 2      Alex

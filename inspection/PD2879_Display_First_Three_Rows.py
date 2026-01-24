#!/usr/bin/env python3
"""
2879. Display the First Three Rows

DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
Write a solution to display the first 3 rows of this DataFrame.

Example 1:
Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
Output:
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
Explanation: 
Only the first 3 rows are displayed.

Hint 1
Consider using a built-in function in pandas library to retrieve the initial rows.


Developer Insights
Problem Nature
We must return the first three rows of a Pandas DataFrame.
This is a data inspection problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.head(n) to retrieve the first n rows.
Default df.head() returns 5 rows, so we must explicitly pass 3.
Input is guaranteed to be a valid DataFrame.

Strategy
Accept DataFrame employees.
Use employees.head(3) to retrieve the first three rows.
Return the resulting DataFrame.

Complexity
Time: O(1) (head operation is metadata slicing).
Space: O(1).

Edge Cases
DataFrame with fewer than 3 rows → returns all available rows.
Empty DataFrame → returns empty DataFrame.
Large DataFrame → efficient, as Pandas slices only the first 3 rows.

Pseudocode
function selectFirstRows(employees):
    return employees.head(3)

"""

#!/usr/bin/env python3
"""
2879. Display the First Three Rows

Return the first three rows of a Pandas DataFrame.
"""

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Display the first three rows of a DataFrame.

    Args:
        employees (pd.DataFrame): Input DataFrame containing employee data.

    Returns:
        pd.DataFrame: A DataFrame containing the first three rows.

    Design:
        - Uses DataFrame.head(3) to retrieve rows.
        - Preserves column order and data types.
        - Returns fewer than 3 rows if DataFrame is smaller.

    Edge Cases:
        - Empty DataFrame → returns empty DataFrame.
        - <3 rows → returns all available rows.
    """
    return employees.head(3)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "employee_id": [3, 90, 9, 60, 49, 43],
        "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
        "department": ["Operations", "Sales", "Engineering", "InformationTechnology", "HumanResources", "Administration"],
        "salary": [48675, 11096, 33805, 37678, 23793, 40454]
    }
    df = pd.DataFrame(data)
    print(selectFirstRows(df))
    # Expected Output:
    #    employee_id     name       department  salary
    # 0            3      Bob       Operations   48675
    # 1           90    Alice            Sales   11096
    # 2            9   Tatiana      Engineering   33805

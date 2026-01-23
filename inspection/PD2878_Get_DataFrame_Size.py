#!/usr/bin/env python3
"""
2878. Get the Size of a DataFrame

DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.
Return the result as an array:
[number of rows, number of columns]
The result format is in the following example.

Example 1:
Input:
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
Output:
[10, 5]
Explanation:
This DataFrame contains 10 rows and 5 columns.

Hint 1
Consider using a built-in function in pandas library to get the size of a DataFrame.


Developer Insights
Problem Nature
We must compute the shape of a Pandas DataFrame (rows × columns) and return it as a list [rows, columns].
This is a data inspection problem under the Intro to Pandas study plan.

Key Observations
Pandas provides df.shape → returns a tuple (rows, columns).
We must convert this tuple into a list.
Input is guaranteed to be a valid DataFrame.

Strategy
Accept DataFrame players.
Use players.shape to get (rows, cols).
Convert to list [rows, cols].
Return result.

Complexity
Time: O(1) (shape retrieval is metadata only).
Space: O(1).

Edge Cases
Empty DataFrame → returns [0, 0].
DataFrame with only columns but no rows → [0, n].
DataFrame with only rows but no columns → [m, 0].

Pseudocode
function getDataframeSize(players):
    shape_tuple = players.shape
    return list(shape_tuple)

"""


#!/usr/bin/env python3
"""
2878. Get the Size of a DataFrame

Compute the number of rows and columns in a Pandas DataFrame.
Return result as [rows, columns].
"""

from typing import List
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Get the size of a Pandas DataFrame.

    Args:
        players (pd.DataFrame): Input DataFrame containing player data.

    Returns:
        List[int]: A list [rows, columns] representing the shape of the DataFrame.

    Design:
        - Uses DataFrame.shape to retrieve dimensions.
        - Converts tuple to list for required output format.
        - Preserves order: [rows, columns].

    Edge Cases:
        - Empty DataFrame → [0, 0].
        - Only columns, no rows → [0, n].
        - Only rows, no columns → [m, 0].
    """
    return list(players.shape)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    data = {
        "player_id": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
        "name": ["Mason", "Riley", "Bob", "Isabella", "Zachary", "Ava", "Violet", "Thomas", "Jack", "Charlie"],
        "age": [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
        "position": ["Forward", "Winger", "Striker", "Goalkeeper", "Midfielder", "Defender", "Striker", "Striker", "Midfielder", "Center-back"],
        "team": ["RealMadrid", "Barcelona", "ManchesterUnited", "Liverpool", "BayernMunich", "Chelsea", "Juventus", "ParisSaint-Germain", "ManchesterCity", "Arsenal"]
    }
    df = pd.DataFrame(data)
    print(getDataframeSize(df))  # Expected: [10, 5]

from typing import List


class Solution:
    def maximumWealth_pythonic(self, accounts: List[List[int]]) -> int:
        """Uses Python's built-in `max` and `sum` functions with a generator expression.

        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        return max(sum(lst) for lst in accounts)

    def maximumWealth_iterative(self, accounts: List[List[int]]) -> int:
        """Iterates through the accounts manually, calculating the sum for each customer.

        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        max_wealth = 0

        for customer in accounts:
            current_wealth = 0
            for bank in customer:
                current_wealth += bank
            max_wealth = max(max_wealth, current_wealth)

        return max_wealth

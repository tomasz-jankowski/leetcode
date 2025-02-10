from typing import List


class Solution:
    def fizzBuzz_in_place(self, n: int) -> List[str]:
        """Modifies `n` in place to avoid extra space.

        Time Complexity: O(n)
        Space Complexity: O(1)

        warning: in-place modification
        """
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                n[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                n[i - 1] = "Fizz"
            elif i % 5 == 0:
                n[i - 1] = "Buzz"
            else:
                n[i - 1] = str(i)
        return n

    def fizzBuzz_immutable(self, n: int) -> List[str]:
        """Uses an additional list to store results, maintaining immutability.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                    answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

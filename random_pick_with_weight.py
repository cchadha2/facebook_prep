"""
indices = [0, 1, 2, 3, 4, 5]
weights = [1, 3, 2, 5, 1, 9]
total = 21

probs = [1/21, 3/21, 2/21, 5/21, 1/21, 9/21] (which sum to 1)
cumulative_probs = [1/21, 4/21, 6/21, 11/21, 12/21, 1]

Approach:
    - Generate a random number between 0 and 1 (using random.randnum)
    - Binary search over cumulative_probs array, looking for highest number that the random number is less than or equal to
    - Return the index of that number

O(N) time to calculate total and O(1) space if we re-use weights for cumulative_probs.


Could also create a `total` length array and randomly choose an index from that but it will be O(total) space and O(total) time.
"""
import random

from bisect import bisect_left


def pick_index(weights):

    num = random.randnum()

    total = sum(weights)
    curr = 0
    for idx, value in enumerate(weights):
        curr += value / total
        weights[idx] = curr

    return bisect_left(weights, num)

# Alternative to potentially reduce time complexity
def pick_index(weights):

    choices = []
    for idx, weight in enumerate(weights):
        choices.extend([idx] * weight)

    return random.choice(choices)

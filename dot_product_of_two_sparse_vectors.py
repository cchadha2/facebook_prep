"""
Use a hashmap to track the non-zero terms of the sparse vector.
The common non-zero terms between two vectors will then by the intersection of the keys of their respective hashmaps.

This will also work for the follow up where only one of the vectors is sparse.

This approach is O(N) time (to build the hashmap from N elements in the vector) and O(k) space where k is number of non-zero terms.
The dot_product method will then be O(min(k1, k2)) time for the two vectors and O(1) space.

Follow up
    - If the vectors were very large, we would spend a lot of time hashing each key. Could there be a more efficient solution?

Keep tuple pairs of (idx, value) for each non-zero value in the vector. Simultaneously iterate over both while computing dot product.
"""


class SparseVector:
    """O(N) time and O(k) space for init

       O(min(k1, k2)) time and O(1) space for dot_product.
    """

    def __init__(self, nums):
        self.terms = {idx: num for idx, num in enumerate(nums) if num}

    def dot_product(self, vec):
        return sum(self[key] * vec[key] for key in self.keys() & vec.keys())

    def keys(self):
        return self.terms.keys()

    def __getitem__(self, key):
        return self.terms[key]


class SparseVector:
    """O(1) time and space for init

       O(N) time and O(1) space for dot_product.
    """

    def __init__(self, nums):
        self.nums = nums

    def dot_product(self, vec):
        return sum(self[key] * vec[key] for key in range(len(self)))

    def __len__(self):
        return len(self.nums)

    def __getitem__(self, key):
        return self.nums[key]


class SparseVector:
    """O(N) time and O(k) space for init

       O(min(k1, k2)) time and O(1) space for dot_product.
    """

    def __init__(self, nums):
        self.terms = [(idx, term) for idx, term in enumerate(nums) if term]

    def dot_product(self, vec):
        res = p1 = p2 = 0

        while p1 < len(self) and p2 < len(vec):
            first_idx, first_val = self[p1]
            second_idx, second_val = vec[p2]

            if first_idx == second_idx:
                res += first_val * second_val
                p1 += 1
                p2 += 1
            elif first_idx < second_idx:
                p1 += 1
            else:
                p2 += 1

        return res

    def __len__(self):
        return len(self.terms)

    def __getitem__(self, key):
        return self.terms[key]

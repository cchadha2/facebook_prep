class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # O(NlogN) time and O(N) space.
        nums.sort()
        output = []
        path = []

        def perms():
            """Overall O(N^2 * N!) time and O(N) space for path and call stack."""
            if len(path) == len(nums):
                output.append(path.copy())
                return


            # O(N) time.
            for idx, num in enumerate(nums):
                if num is None or (idx and nums[idx - 1] == num):
                    continue

                path.append(num)
                nums[idx] = None

                # Called O(N * N!) times as there are N! permutations
                # of N elements.
                perms()

                nums[idx] = path.pop()

        perms()
        return output
       

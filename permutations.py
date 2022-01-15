class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # O(N * N!) time and O(N) space for path (not counting O(N!) space for output).
        def create_perm(path):
            if len(path) == len(nums):
                output.append(path.copy())
                return

            for idx, num in enumerate(nums):
                if num is None:
                    continue

                nums[idx] = None
                path.append(num)

                create_perm(path)

                nums[idx] = num
                path.pop()

        output = []
        create_perm([])
        return output

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # O(N* N!) time (but better than above solution) and O(N) space
        # for path (not counting O(N!) space for output).
        def create_perm(first=0):
            if first == len(nums):
                output.append(nums.copy())

            for idx in range(first, len(nums)):
                nums[first], nums[idx] = nums[idx], nums[first]

                create_perm(first + 1)

                nums[first], nums[idx] = nums[idx], nums[first]

        output = []
        create_perm()
        return output

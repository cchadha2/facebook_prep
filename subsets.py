class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        # 2^N sets overall as we can decided to take the current digit or leave it.
        # => Overall O(N*2^N) time as we must copy path on each call which is
        # O(N) time. O(N) space required for recursion and path.
        def build_set(idx, path):
            for next_idx in range(idx, len(nums)):
                path.append(nums[next_idx])
                output.append(path.copy())

                build_set(next_idx + 1, path)

                path.pop()


        output = [[]]
        # O(N) time and O(N) space for path.
        build_set(idx=0, path=[])
        return output

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """O(N) time and O(1) space (not counting output array)"""

        output = []
        exp_num = 1
        for num in target:
            if exp_num == num:
                output.append("Push")
                exp_num += 1
                continue

            while exp_num < num:
                output.append("Push")
                output.append("Pop")
                exp_num += 1

            output.append("Push")
            exp_num += 1

        return output

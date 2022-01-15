class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # O(N^2) time and O(N) space.
        return goal in 2 * s and len(goal) == len(s)


    def rotateString(self, s: str, goal: str) -> bool:
        # O(N) time and space solution.
        if not len(s) == len(goal):
            return False

        start = ord("a")
        radix = 26
        goal_hash = 0
        for idx in range(len(goal)):
            goal_hash += (ord(goal[idx]) - start) * (radix ** idx)

        dupe_s = s * 2
        s_hash = 0
        for idx in range(len(goal)):
            s_hash += (ord(dupe_s[idx]) - start) * (radix ** idx)

        if s_hash == goal_hash:
            return True

        for next_idx in range(len(goal), len(dupe_s)):
            s_hash -= (ord(dupe_s[next_idx - len(goal)]) - start)
            s_hash //= radix
            s_hash += (ord(dupe_s[next_idx]) - start) * (radix ** (len(goal) - 1))

            if s_hash == goal_hash:
                return True

        return False

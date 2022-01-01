"""

NOTE: These examples should be arrays of ints instead of strings!

Example = "539241"
Output = "539412"

Example = "783219"
Output = "783291"

Example = "54321"
Output = "12345"

Approach:
    - From the right, find first a[i] where a[i + 1] > a[i]
    - Iterate from i + 1 to len(nums), looking for smallest num that maintains reverse sorted order of (i + 1, len(nums))
    - Swap a[i] with that num
    - Reverse (i + 1, len(nums)) chars

If our iteration from the right reaches -1, reverse the whole array instead.


Time: O(N) at worst as we scan the array fully twice for first two steps and
      then reverse most of the array (if a[i] == a[o])
Space: O(1)

Follow up:
    - What if we wanted to decrease the sequence by one?

Example: "539412" -> "539241"

From the right, find the first num that is not in reverse sorted order,
reverse all nums to the right of that number. Then, find the smallest rightmost
number that maintains sorted order.


"""


def lexicographically_higher(nums):

    def reverse_array(start, end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    swap_idx = None
    for idx in range(len(nums) - 1, 0, -1):
        if nums[idx - 1] < nums[idx]:
            swap_idx = idx - 1
            break

    if swap_idx is None:
        reverse_array(0, len(nums) - 1)
        return

    right_swap_idx = len(nums) - 1
    for idx in range(swap_idx + 1, len(nums)):
        if nums[idx] >= nums[swap_idx]:
            right_swap_idx = idx
        else:
            break


    nums[swap_idx], nums[right_swap_idx] = nums[right_swap_idx], nums[swap_idx]
    reverse_array(swap_idx + 1, len(nums) - 1)
    return

def lexicographically_higher_followup(nums):

    def reverse_array(start, end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    swap_idx = None
    for idx in range(len(nums) - 1, 0, -1):
        if nums[idx - 1] > nums[idx]:
            swap_idx = idx - 1
            break

    if swap_idx is None:
        reverse_array(0, len(nums) - 1)
        return

    reverse_array(swap_idx + 1, len(nums) - 1)

    right_swap_idx = swap_idx + 1
    for idx in range(len(nums) - 1, swap_idx, -1):
        if nums[idx] <= nums[swap_idx]:
            right_swap_idx = idx


    nums[swap_idx], nums[right_swap_idx] = nums[right_swap_idx], nums[swap_idx]
    return


nums = [5,3,9,4,1,2]
exp = [5,3,9,2,4,1]
print(nums)
lexicographically_higher_followup(nums)
print(nums)
print(nums == exp)

nums = [5,3,9,4,3,6,7]
exp = [5,3,9,3,7,6,4]
print(nums)
lexicographically_higher_followup(nums)
print(nums)
print(nums == exp)

lexicographically_higher(exp)
lexicographically_higher(nums)
print(exp == nums)

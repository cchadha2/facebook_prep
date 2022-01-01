"""

            3
           / \
          4   6
         / \ / \
        2  8 9  10
            \
             12
output = [[2], [4], [3,8,9], [6,12], [10]]

if two nodes are in the same column and at the same depth, leftmost node comes first in the output.

Approach:
    - Inorder traversal means we'd always reach the leftmost node of that column first. Use an order int to track the leftmost node.
    - To ensure the most vertical node is first in the output, we should also track the depth of the node as we traverse the tree.
    - Also track the min and max columns we've traversed to - this lets us avoid having to sort the keys of the hashmap.
    - For each column, maintain a hashmap of its index (e.g. -2 is 2 directions to the left of the root which is 0).
    - The values in the hashmap can then be a list of (depth, order, value) tuples.
    - When we're done traversing, build the output list by sorting the keys and sorting the lists for each column, transforming to only include values, and appending to output array.
"""
def vertical_order(root):
    """O(c*klogk) time since k can be height / 2 at most and c is number of columns.
       => c*klogk > N as c*k > N.

       O(N) extra space for hashmap
    """
    if not root:
        return []

    # O(N) extra space.
    columns = {}
    order = 0
    # There can only be 100 nodes in the tree at most from question constraints.
    # Set these min and max key values to impossible integers to begin.
    min_key = 101
    max_key = -101

    def inorder(node, left, right, depth):
        if not node:
            return

        inorder(node.left, left + 1, right, depth + 1)

        nonlocal order, min_key, max_key
        key = right - left
        min_key = min(min_key, key)
        max_key = max(max_key, key)
        order += 1

        columns.setdefault(key, []).append((depth, order, node.val))

        inorder(node.right, left, right + 1, depth + 1)


    # O(N) time and between O(N) and O(logN) space for call stack.
    inorder(root, 0, 0, 0)

    output = []
    # O(c*klogk) time and O(k) space.
    for column in range(min_key, max_key + 1):
        # O(klogk) time and O(k) space.
        columns[column].sort()
        # O(k) time k is number of nodes in a column.
        for idx, (_, _, value) in enumerate(columns[column]):
            columns[column][idx] = value

        output.append(columns[column])

    return output

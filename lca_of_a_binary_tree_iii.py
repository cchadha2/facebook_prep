"""
Given two nodes of a binary tree p and q,
return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is
below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."

Constraints:
    - All node values are unique
    - p and q are guaranteed to exist in the tree so we can't get an empty root


Example:

        9
       / \
      4   5
     / \ / \
    3  7 6  2
   /    \
  1      8


LCA of 8 and 1 is 4

LCA of 4 and 8 is 4

Approach:
    - Iterate both nodes to the root and count distance away
    - If they are the same distance, iterate over both simultaneously until we
      reach the LCA
    - Otherwise, bring the further node to parity with the other and do step 2

O(logN) (if the tree is balanced, else O(N)) time solution as we are directly
navigating up the tree from both nodes. O(1) space.


Could also do this with an array of nodes and finding the the leftmost common
node between p and q and returning but this would be O(logN) (or O(N) as before)
space.
"""


def find_lca(p, q):

    p_distance = 0
    node = p.parent
    while node:
        p_distance += 1
        node = node.parent

    q_distance = 0
    node = q.parent
    while node:
        q_distance += 1
        node = node.parent

    while p_distance > q_distance:
        p = p.parent
        p_distance -= 1
    while q_distance > p_distance:
        q = q.parent
        q_distance -= 1

    while not p is q:
        p = p.parent
        q = q.parent

    return p

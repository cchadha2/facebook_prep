"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Questions:
    - Empty emails? no
    - Can two people share an email? No

Approach:
    - Build a graph of emails and find the connected components of the graph
    - Create an Email class
    - Maintain the graph as a hashmap with a list of hashes to which the email is adjacent

O(V) time and space to build the graph where V is number of total emails in accounts.
O(E + V) time and O(V) space to traverse the graph where E is number of edges and V is number of emails.

So O(E + V) time and O(V) space in total.


A better way to analyze time and space would be to let N = number of accounts and K = max number of emails in all accounts.

=> O(NK*Klog(NK)) time in the worst case where all emails belong to to the one person. O(NK) space for the graph.
"""
class Email:

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __eq__(self, other):
        if not type(other) == Email:
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"Email(value={self.value}, name={self.name})"

class Graph:

    def __init__(self):
        self.table = {}

    def add_vertex(self, vertex, name):
        self.table.setdefault(Email(vertex, name), [])

    def add_edge(self, from_vert, to_vert, name):
        from_email = Email(from_vert, name)
        to_email = Email(to_vert, name)

        self.table.setdefault(from_email, []).append(to_email)
        self.table.setdefault(to_email, []).append(from_email)

    def __repr__(self):
        return f"Graph({self.table})"


def merge_accounts(accounts):

        graph = Graph()

        for account in accounts:
            name, *addresses = account

            for idx, address in enumerate(addresses):
                graph.add_vertex(address, name)
                for adj_address in addresses[idx + 1:]:
                    graph.add_edge(addresses[idx], addresses[idx + 1], name)

        visited = set()
        res = []
        for vertex in graph.table:
            if vertex in visited:
                continue

            stack = [vertex]
            account = [vertex.name]

            while stack:
                email = stack.pop()

                if email in visited:
                    continue

                visited.add(email)
                account.append(email.value)

                for adj_email in graph.table[email]:
                    if not adj_email in visited:
                        stack.append(adj_email)

            # O(KlogK) where K is number of emails in the account.
            account[1:] = sorted(account[1:])
            res.append(account)

        return res

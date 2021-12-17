"""
n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

After first two calls:
stack = [(0, 0), (0, 2)]
on_stack = [[0, 2]]
times = [0, 0]

After third log:
stack = [(0, 0)]
on_stack = [[0]]
# 5 - 2 = 3
times = [3, 0]
"""

def exclusive_times(n, logs):
    if not n:
        return []

    stack = []
    # O(N) time and space.
    times = [0] * n

    # O(L) where L is number of logs.
    # Overall O(L) as L > N and O(N) space.
    for log in logs:
        function_id, action, time = log.split(":")
        function_id, time = int(function_id), int(time)

        if action == "start":
            if stack:
                times[stack[-1][0]] += time - stack[-1][1]
                stack[-1][1] = time

            stack.append([function_id, time])
        else:
            _, start_time = stack.pop()
            times[function_id] += time - start_time + 1

            if stack:
                stack[-1][1] = time + 1

    return times

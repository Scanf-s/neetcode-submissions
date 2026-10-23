from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for follow, pre in prerequisites:
            graph[pre].append(follow)
            indegree[follow] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        attendedCourses = 0

        while q:
            course = q.popleft()
            attendedCourses += 1

            for node in graph[course]:
                indegree[node] -= 1

                if indegree[node] == 0:
                    q.append(node)

        return attendedCourses == numCourses
        
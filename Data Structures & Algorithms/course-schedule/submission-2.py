from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph: dict[int, list[int]] = defaultdict(list)
        indegree: dict[int, int] = {}
        for prereq in prerequisites:
            pre: int = prereq[1]
            follow: int = prereq[0]
            graph[pre].append(follow)
            if follow not in indegree.keys():
                indegree[follow] = 1
            else:
                indegree[follow] += 1
            if pre not in indegree.keys():
                indegree[pre] = 0

        attendedCourses: int = 0
        while attendedCourses < numCourses:
            course: int = -1
            for key, val in indegree.items():
                if val == 0:
                    course = key
                    break
            if course < 0:
                return False

            del indegree[key]
            if not indegree:
                return True
            attendedCourses += 1

            for node in graph[key]:
                indegree[node] -= 1

        return True if attendedCourses == numCourses else False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjLists = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjLists[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            for neighbor in adjLists[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for node in range(numCourses):
            if indegree[node] != 0:
                return False
        return True
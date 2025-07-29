class Solution:
    def backtrack(self, node, edges, colors, m, n):
        if node == n:
            return True
        connected_nodes = []
        for u, v in edges:
            if node == u:
                connected_nodes.append(v)
            if node == v:
                connected_nodes.append(u)
        used_colors = [colors[x] for x in connected_nodes]
        for color in range(m):
            if color not in used_colors:
                colors[node] = color
                if self.backtrack(node + 1, edges, colors, m, n):
                    return True
                colors[node] = -1
        return False
        
    def graphColoring(self, edges, m, n):
        #your code goes here
        colors = [-1 for _ in range(n)]
        return self.backtrack(0, edges, colors, m, n)

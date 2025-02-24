import math
import heapq
import plotting
import env

class AStar:

    def __init__(self, s_start, s_goal, heuristic_type):
        self.s_start = s_start
        self.s_goal = s_goal
        self.heuristic_type = heuristic_type

        self.Env = env.Env()

        self.u_set = self.Env.motion   
        self.obs = self.Env.obs

        self.OPEN = []
        self.CLOSED = []
        self.PARENT = dict()
        self.g = dict()

    def searching(self):

        self.PARENT[self.s_start] = self.s_start
        self.g[self.s_start] = 0
        self.g[self.s_goal] = math.inf

        heapq.heappush(self.OPEN, (self.f_value(self.s_start), self.s_start))

        while self.OPEN: 
            _, s = heapq.heappop(self.OPEN)
            self.CLOSED.append(s)

            if s == self.s_goal:
                break
            for s_n in self.get_neighbor(s):

                new_cost = self.g[s] + self.cost(s, s_n)

                if s_n not in self.g:
                    self.g[s_n] = math.inf

                if new_cost < self.g[s_n]:
                    self.g[s_n] = new_cost
                    self.PARENT[s_n] = s
                    heapq.heappush(self.OPEN, (self.f_value(s_n), s_n))
            
        return self.extract_path(self.PARENT), self.CLOSED
    
    def get_neighbor(self, s):
        return [(s[0]+ u[0], s[1]+ u[1]) for u in self.u_set]
    def cost(self, s_start, s_goal):
        if self.is_collision(s_start, s_goal):
            return math.inf
        return math.hypot(s_goal[0] - s_start[0], s_goal[1] - s_start[1])
    
    def is_collision(self, s_start, s_end):
        if s_start in self.obs or s_end in self.obs:
            return True
        if s_start[0] != s_end[0] and s_start[1] != s_end[1]:
            s1 = (min(s_start[0], s_end[0]), min(s_start[1], s_end[1]))
            s2 = (max(s_start[0], s_end[0]), max(s_start[1], s_end[1]))
        else:
            s1 = (min(s_start[0], s_end[0]), max(s_start[1], s_end[1]))
            s2 = (max(s_start[0], s_end[0]), min(s_start[1], s_end[1]))

        if s1 in self.obs or s2 in self.obs:
            return True
        
        return False

    def f_value(self, s):

        return self.g[s] + self.heuristic(s)
    
    def extract_path(self, PARENT):
        path = [self.s_goal]
        s = self.s_goal

        while True:
            s = PARENT[s]
            path.append(s)

            if s == self.s_start:
                break
        return list(path)
    
    def heuristic(self, s):
        """
        Calculate heuristic.
        :param s: current node (state)
        :return: heuristic function value
        """

        heuristic_type = self.heuristic_type  # heuristic type
        goal = self.s_goal  # goal node

        if heuristic_type == "manhattan":
            return abs(goal[0] - s[0]) + abs(goal[1] - s[1])
        else:
            return math.hypot(goal[0] - s[0], goal[1] - s[1])


def main():
    s_start = (5, 5)
    s_goal = (45, 25)

    astar = AStar(s_start, s_goal, "euclidean")
    plot = plotting.Plotting(s_start, s_goal)

    path, visited = astar.searching()
    plot.animation(path, visited, "A*")  # animation

    # path, visited = astar.searching_repeated_astar(2.5)               # initial weight e = 2.5
    # plot.animation_ara_star(path, visited, "Repeated A*")


if __name__ == '__main__':
    main()
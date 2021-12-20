import random
from datetime import datetime
from exercise.maze import Maze
import bisect


class Search:

    def __init__(self, graph):
        self.graph = graph
        random.seed(datetime.now())

    def breadth_first_solution(self):

        self.graph.reset_state()

        queue = [self.graph.start]
        visited = []

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node != self.graph.target:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours =  current_node.get_neighbours()
                    random.shuffle(neighbours)
                    neighbours.reverse()
                    for next_node in neighbours:
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            queue.append(next_node)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()

    def depth_first_solution(self):

        self.graph.reset_state()

        stack = [self.graph.start]
        visited = []

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node != self.graph.target:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for next_node in neighbours:
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            stack.append(next_node)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()

    # ADD YOU IMPLEMENTATIONS FOR GREEDY AND ASTAR HERE!
    def greedy_search(self):
        self.graph.reset_state()
        queue = [self.graph.start]
        visited = []
        while(len(queue) > 0):
            current_node = queue.pop(0)
            if current_node != self.graph.target:
                if current_node not in visited:
                    visited.append(current_node)
                    for next_node in current_node.get_neighbours():
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            gscore = next_node.manhattan_distance(self.graph.target)
                            next_node.score = gscore
                            bisect.insort(queue, next_node)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()

    def a_star_search(self):
        self.graph.reset_state()
        queue = [self.graph.start]
        visited = []
        while(len(queue) > 0):
            current_node = queue.pop(0)
            if current_node != self.graph.target:
                if current_node not in visited:
                    visited.append(current_node)
                    for neighbour in current_node.get_neighbours():
                        if neighbour not in visited:
                            neighbour.set_parent(current_node) #to compute the distance
                            fscore = neighbour.distance
                            gscore = neighbour.manhattan_distance(self.graph.target)
                            neighbour.score = gscore + fscore
                            if neighbour not in queue:
                                neighbour.set_parent(current_node)
                                neighbour.score = neighbour.distance + neighbour.manhattan_distance(self.graph.target) #fscore + gscore
                                bisect.insort(queue, neighbour) #put it in the array at the right position
                            elif neighbour.distance < current_node.distance:
                                neighbour.set_parent(current_node)
                                neighbour.score = neighbour.distance + neighbour.manhattan_distance(self.graph.target)
                                queue.remove(neighbour)
                                bisect.insort(queue, neighbour)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()



    def highlight_path(self):
        # Compute the path, back to front.
        current_node = self.graph.target.parent

        while current_node is not None and current_node != self.graph.start:
            current_node.set_color((248, 220, 50))
            current_node = current_node.parent

        print("Path length is: {}".format(self.graph.target.distance))

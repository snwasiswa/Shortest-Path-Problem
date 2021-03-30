import heapq
from datetime import datetime


class Dijkstra:

    def __init__(self, file):
        """ Initialise, read the file and  create a graph"""

        self.inputFile = open(file).read()
        self.nodes = self.inputFile.split('\n')

        self.graph = {}

        for i in range(0, len(self.nodes)):
            if len(self.nodes[i]) > 0:
                self.cols = self.nodes[i].split('\t')
                source = self.cols[0]

                self.graph[source] = {}
                for j in range(1, len(self.cols)):
                    if len(self.cols[j]) > 0:
                        edge = self.cols[j].split(',')
                        self.graph[source][edge[0]] = int(edge[1])

    def algorithmone(self, source_node):
        """ Uses other data structures such as set, list and dictionnary"""

        distances = {node: float('infinity') for node in self.graph}

        explored_nodes = set()
        explored_nodes.add(source_node)

        distances[source_node] = 0

        vertices = {x for x in self.graph.keys()}

        while len(vertices) != len(explored_nodes):

            for node in self.graph:

                SortedNode = sorted(self.graph[node].items(), key=lambda x: x[1])

                for adjacent_node, edge_length in self.graph[node].items():

                    if adjacent_node not in explored_nodes:

                        if distances[adjacent_node] > SortedNode[0][1] + edge_length:
                            distances[adjacent_node] = SortedNode[0][1] + edge_length
                            explored_nodes.add(adjacent_node)
                            vertices.remove(adjacent_node)
                        else:
                            continue

            return distances

    def algorithmtwo(self, source_node):
        """ Uses priority queue to keep track of the vertices with the lowest weight"""

        priority_queue = list()

        distances = {node: float('infinity') for node in self.graph}

        distances[source_node] = 0

        for node in self.graph:
            heapq.heappush(priority_queue, (distances[node], node))

        while len(priority_queue) != 0:

            distance, node = heapq.heappop(priority_queue)

            for adjacent_node, edge_length in self.graph[node].items():

                if distances[adjacent_node] > distances[node] + edge_length:
                    distances[adjacent_node] = distances[node] + edge_length
                    heapq.heappush(priority_queue, (distances[adjacent_node], adjacent_node))
                else:
                    continue

        return distances


def main():

    dijkstra = Dijkstra("homework6testcase.txt")
    source_node = '1'
    # print(dijkstra.algorithmone("1"))

    nodes = ['7', '37', '59', '82', '99', '115', '133', '165', '188', '197']
    print("\nDijkstra's Algorithm 1:")

    start_time1 = datetime.now()
    for node in nodes:
        print("\nDistance from " + source_node + " to " + node + " is " +
              str(dijkstra.algorithmone(source_node)[node]))
    end_time1 = datetime.now()

    print('\nDuration: {}'.format(end_time1 - start_time1))

    print("\nDijkstra's Algorithm 2:")

    start_time2 = datetime.now()
    for node in nodes:
        print("\nDistance from " + source_node + " to " + node + " is " +
              str(dijkstra.algorithmtwo(source_node)[node]))
    end_time2 = datetime.now()

    print('\nDuration: {}'.format(end_time2 - start_time2))


# Run main as the only function
if __name__ == "__main__":
    main()

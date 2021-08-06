import sys
from collections import defaultdict


# add line/edge to two cities that have a connection
def add_edge(city_graph, city_node1, city_node2):
    city_graph[city_node1].add(city_node2)
    city_graph[city_node2].add(city_node1)

    return city_graph


# breadth-first search
def is_connected(city_graph, city1, city2):
    # base case
    if city1 == city2:
        return True

    # mark all the nodes as not visited
    visited = {k: False for k in city_graph.keys()}
    queue = []

    # mark the current node as visited and enqueue it
    visited[city1] = True
    queue.append(city1)

    while queue:
        cur_node = queue.pop(0)

        # check all adjacent nodes
        for n in city_graph[cur_node]:
            if n == city2:
                return True

            if not visited[n]:
                visited[n] = True
                queue.append(n)

    return False


if __name__ == '__main__':
    try:
        try:
            file_name = sys.argv[1]
            city1 = sys.argv[2]
            city2 = sys.argv[3]
        except IndexError:
            print("Three command line arguments should be entered: filename cityname1 cityname2")
            sys.exit()
        else:
            if len(sys.argv) > 4:
                print(
                    "Only three command line arguments are needed. Add quotation marks if space exists in the city name.")
                sys.exit()

        # dictionary with values as set, more efficient in case
        # there are too many repetitive connections in the txt file
        city_graph = defaultdict(set)

        # use with open, no need to close the file at the end
        with open(file_name) as f:
            for line in f:
                city_nodes = line.split(",")
                # strip whitespace in the beginning and the end
                city_node1 = city_nodes[0].strip()
                city_node2 = city_nodes[1].strip()

                city_graph = add_edge(city_graph, city_node1, city_node2)

        if is_connected(city_graph, city1, city2):
            print("yes")
        else:
            print("no")

    except Exception as e:
        # catch exception to avoid crash
        print(e)

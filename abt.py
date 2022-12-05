import random

node = 3
colors = ["red", "blue"]


class Agent:

    number_of_node = 0
    color_of_node = ""
    node_neighbours = list()
    neighbours_address = list()

     def __init__(self, number_of_node, color_of_node, node_neighbours):
        self.number_of_node = number_of_node
        self.color_of_node = color_of_node
        self.node_neighbours = node_neighbours
        self.neighbours_address = []

    def handle_ok(self, other_number, other_color):
        print("{0} send message to {1} color:{2}".format(other_number, self.number_of_node, other_color))

        for item in self.node_neighbours:
            if item[0] == other_number:
                item[1] = other_color
        self.check_local_view()

    def check_local_view(self):
        for item in self.node_neighbours:
            if item[1] is not None and (item[1] is self.color_of_node):
                old_color_of_node = self.color_of_node
                for new_color_of_node in colors:
                    if new_color_of_node != old_color_of_node:
                        consistent = True
                        for e in self.node_neighbours:
                            self.color_of_node = new_color_of_node
                            if e[1] is not None and (e[1] is self.color_of_node):
                                consistent = False
                        if consistent is True:
                            print("agent:{0} change {1} to {2}".format(self.number_of_node, old_color_of_node, self.color_of_node))
                            break

                if consistent is False:
                    print("backTrack")
                else:
                    if self.color_of_node is not old_color_of_node:
                        for a in self.neighbours_address:
                            a.handle_ok(self.number_of_node, self.color_of_node)


all_Agents = list()

for i in range(node):
    neighbours = list()
    for j in range(node):
        if i != j:
            neighbours.append([j, None])
    color = random.choice(colors)
    all_Agents.append(Agent(i, color, neighbours))

for i in all_Agents:
    for j in all_Agents:
        if i != j:
            i.neighbours_address.append(j)

for i in range(node):
    print(all_Agents[i].number_of_node)
    print(all_Agents[i].color_of_node)

for i in range(node):
    for n in all_Agents[i].neighbours_address:
        n.handle_ok(all_Agents[i].number_of_node, all_Agents[i].color_of_node)

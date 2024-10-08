'''Steps:
    1. Find the cheapest node. This is the node
        you can get to in the least amount of 

    2. Check whether there's a cheaper path to
       neighbors of this node. If so, update 
       their costs.

    3. Repeat until you've done this for every 
      node in the graph.

    4. Calculate the final path.'''


'''1. Create 3 hashtables''' 
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')

'''2. Hashtables for costs'''
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

'''3. Hashtables for parents'''
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            paents[n] = node
    processed.append(node)
    node = find_lowest_costnode(costs)

print(graph['start'].keys())
#print(graph['start'].pop('b'))
print(graph['start']['b'])
print(infinity)

#+

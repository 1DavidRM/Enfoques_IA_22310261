from maze_simulator import Maze

mapa = """
##############################
# o         #                #
# ####      ########         #
#    #      #           #    #
#    ###       ##### ####    #
#      #     ###   #         #
#  #           #   #         x
##############################
"""

ent = Maze(mapa)
ent.draw()
class LIFOQueue(object):
    """Clase de una cola FIFO en los problemas de búsqueda"""
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(q) for q in self.queue])
    def isEmpty(self):
        return self.queue == []
    def push(self, element):
        self.queue.append(element)
    def pop(self):
        last_element = self.queue[-1]
        del self.queue[-1]
        return last_element
    
class Node(object):
    """Clase para crear nodos con sus atributos."""
    def __init__(self):
        self.state = (0,0)
        self.parent = None 
        self.action = None
        #Guarda la profundidad del nodo
        self.depth = 0
    def __str__(self):
        if self.parent == None:
            return "State: {}".format(self.state)
        else:
            return "State: {}, Action: {}, Parent: {}".format(self.state,self.action,self.parent.state)   
            
def expand(problem, node):
    """Función para expandir los nodos dado el problema"""
    s = node.state 
    for action in problem.actions(s):
        new_s = problem.result(s, action)        
        new_node,new_node.state,new_node.parent,new_node.action = Node(),new_s,node,action
        new_node.depth = node.depth + 1
        yield new_node
ef DepthLimitedSearch(problem,l):
    """Algoritmo Depth-Limited Search"""
    #Almacenamiento de nodos
    nodes = []
    #Nodo inicial
    node = Node()
    node.state = problem.initial    
    #Frontera con cola de prioridad
    frontier = LIFOQueue()
    frontier.push(node)
    #Nodos alcanzados
    reached = {problem.initial:node}
    #resultado
    result = "failure"

    #Mientras la frontera no esté vacía
    while frontier.isEmpty() == False:
        #Pop en frontera
        node = frontier.pop()
        #Guarda el nodo en la lista
        nodes.append(node)
        
        if problem.is_goal(node.state):
            print("Se encontró solución")
            return nodes
        if node.depth > l:
            result = "cutoff"
        else:
            for child in expand(problem, node):
                state = child.state
                if state not in reached.keys():
                    reached[state] = child
                    frontier.push(child)
    
    return result
    tree_5 = DepthLimitedSearch(ent,l=10)
print(tree_5)
tree = DepthLimitedSearch(ent,l=50)
def get_path(search_tree, root):
    """Recupera la solución."""
    leaf = search_tree[::-1][0]
    parent = leaf.parent
    path = [leaf, parent]
    while parent.state != root:
        parent = parent.parent
        path.append(parent)
        
    return path[::-1]

#Visualiza la solución
prev_s = ent.initial
for n in get_path(tree, ent.initial):
    ent.move(prev_s, n.state)
    prev_s = n.state
    
ent.draw()
# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    This search algorithm returns a list of actions that reaches the
    goal. It is a graph search algorithm.

    To test, try any of the following commands:

    python pacman.py -l tinyMaze -p SearchAgent
    python pacman.py -l mediumMaze -p SearchAgent --frameTime 0
    python pacman.py -l bigMaze -z .5 -p SearchAgent --frameTime 0
    """

    fringe = util.Stack()
    fringe.push( (problem.getStartState(), [], []) )

    while not fringe.isEmpty():
        node, actions, visited = fringe.pop()

        if problem.isGoalState(node):
            return path

        for child, direction, steps in problem.getSuccessors(node):
            if not child in visited:                
                fringe.push((child, actions + [direction] , visited + [node] ))
                path = actions + [direction]
                         
    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    To test, try any of the following commands:

    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0
    python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0
    python eightpuzzle.py
    """

    fringe = util.Queue()
    fringe.push( (problem.getStartState(), [], []) )
    expanded = []

    while not fringe.isEmpty():
        node, actions, curCost = fringe.pop()

        if(not node in expanded):
            expanded.append(node)

            if problem.isGoalState(node):
                return actions

            for child, direction, cost in problem.getSuccessors(node):
                fringe.push((child, actions+[direction], curCost + [cost]))

    return []

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.

    To test, try any of the following commands:

    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs --frameTime 0
    python pacman.py -l mediumDottedMaze -p StayEastSearchAgent --frameTime 0
    python pacman.py -l mediumScaryMaze -p StayWestSearchAgent --frameTime 0
    """

    fringe = util.PriorityQueue()
    fringe.push( (problem.getStartState(), [], 0), 0 )
    expanded = []

    while not fringe.isEmpty():
        node, actions, curCost = fringe.pop()

        if(not node in expanded):
            expanded.append(node)

            if problem.isGoalState(node):
                return actions

            for child, direction, cost in problem.getSuccessors(node):
                fringe.push((child, actions+[direction], curCost + cost), curCost + cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.

    To test, try the following command:

    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    """

    fringe = util.PriorityQueue()
    fringe.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    expanded = []

    while not fringe.isEmpty():
        node, actions, curCost = fringe.pop()

        if(not node in expanded):
            expanded.append(node)

            if problem.isGoalState(node):
                return actions

            for child, direction, cost in problem.getSuccessors(node):
                g = curCost + cost
                fringe.push((child, actions+[direction], curCost + cost), g + heuristic(child, problem))

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

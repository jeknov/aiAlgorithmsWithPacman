Different AI algorithms implemented in a Pacman game.

<b>Folder 01.Search_BFS.DFS.UCS.Astar contains single-agent search algoritms.</b>

a) Depth First Search (DFS). To test, try any of the following at the command line:
    <p><code>python pacman.py -l tinyMaze -p SearchAgent</code>
    <p><code>python pacman.py -l mediumMaze -p SearchAgent --frameTime 0</code>
    <p><code>python pacman.py -l bigMaze -z .5 -p SearchAgent --frameTime 0</code>

b) Breadth First Search (BFS). To test, try:
    <p><code>python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0</code>
    <p><code>python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0</code>
    <p><code>python eightpuzzle.py</code>

c) Uniform Cost Search (UCS). To test, try:
    <p><code>python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs --frameTime 0</code>
    <p><code>python pacman.py -l mediumDottedMaze -p StayEastSearchAgent --frameTime 0</code>
    <p><code>python pacman.py -l mediumScaryMaze -p StayWestSearchAgent --frameTime 0</code>

d) A* search. To test, try:
    <code>python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic</code>

<b>Folder 02.MultiAgentSearch contains multi-agent search algoritms.</b>

a) Reflex agent. To test, try:
    <code>python pacman.py --frameTime 0 -p ReflexAgent -k 1</code>

b) Minimax agent. To test, try:
    <code>python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4</code>

c) Minimax agent with alpha-beta pruning. To test, try:
    <code>python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic</code>

d) Expectimax agent. To test, try:
    <code>python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3</code>

<b>Folder 03.ReinforcementLearning contains MDP and reinforcement learning algoritms. </b>

To test, try:
    <p><code>python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid</code>
    <p><code>python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic</code> (training may take some time, please be patient!)

Prepared for the BerkeleyX course <i>Artificial Intelligence</i>.

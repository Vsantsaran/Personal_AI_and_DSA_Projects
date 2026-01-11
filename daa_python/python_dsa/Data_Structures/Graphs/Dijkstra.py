{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d7fb64c3-f37e-4ebc-9bf0-d28c092d114f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import heapq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "c3f5c645-24d7-453a-baa7-f8c4fba740ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "Priority: 1, Task: eat\n",
      "Priority: 1, Task: drink\n",
      "Priority: 2, Task: code\n"
     ]
    }
   ],
   "source": [
    "import heapq\n",
    "from itertools import count\n",
    "\n",
    "counter = count()\n",
    "print(next(counter))\n",
    "priority_queue = []\n",
    "\n",
    "# Push items with priorities\n",
    "heapq.heappush(priority_queue, (1, next(counter), 'eat'))\n",
    "heapq.heappush(priority_queue, (1, next(counter), 'drink'))\n",
    "heapq.heappush(priority_queue, (2, next(counter), 'code'))\n",
    "\n",
    "# Pop items\n",
    "while priority_queue:\n",
    "    priority, count_num, task = heapq.heappop(priority_queue)\n",
    "    print(f\"Priority: {priority}, Task: {task}\")\n",
    "\n",
    "# Output:\n",
    "# Priority: 1, Task: eat\n",
    "# Priority: 1, Task: drink\n",
    "# Priority: 2, Task: code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "95b2ad67-e9a3-41b1-a578-02928125a3a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Graph:\n",
    "    def __init__(self, n):\n",
    "        self.PQ = []\n",
    "        self.distances = [np.inf for _ in range(n)]\n",
    "        self.adj_mat = [[0 for _ in range(n)] for _ in range(n)]\n",
    "        self.visited = [0 for _ in range(n)]\n",
    "        self.n = n\n",
    "\n",
    "    def add_edge(self, a, b, weight):\n",
    "        self.adj_mat[a][b] = weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "dfdb4e67-4ea8-426a-bdf9-9ed4b498affc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Dijkstra_iterative(G, src, dst):\n",
    "    G.distances[src] = 0\n",
    "    heapq.heappush(G.PQ, (0, src))\n",
    "    \n",
    "    while G.PQ:\n",
    "        current_distance, current_node = heapq.heappop(G.PQ)\n",
    "        if G.visited[current_node]:\n",
    "            continue\n",
    "        G.visited[current_node] = 1\n",
    "        if current_node == dst:\n",
    "            return G.distances[dst]\n",
    "        \n",
    "        for neighbor, weight in enumerate(G.adj_mat[current_node]):\n",
    "            if weight > 0 and not G.visited[neighbor]:\n",
    "                new_distance = current_distance + weight\n",
    "                if new_distance < G.distances[neighbor]:\n",
    "                    G.distances[neighbor] = new_distance\n",
    "                    heapq.heappush(G.PQ, (new_distance, neighbor))\n",
    "    \n",
    "    return G.distances[dst]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b1d485e5-c7da-412d-9463-9250e1ac4175",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shortest path from 4 to 5 is: 8\n"
     ]
    }
   ],
   "source": [
    "N = 6\n",
    "SRC = 4\n",
    "DST = 5\n",
    "\n",
    "G = Graph(N)\n",
    "G.add_edge(4, 0, 2)\n",
    "G.add_edge(0, 1, 1)\n",
    "G.add_edge(4, 2, 3)\n",
    "G.add_edge(2, 0, 4)\n",
    "G.add_edge(2, 3, 2)\n",
    "G.add_edge(3, 5, 3)\n",
    "G.add_edge(1, 3, 5)\n",
    "G.add_edge(5, 1, 4)\n",
    "\n",
    "result = Dijkstra_iterative(G, SRC, DST)\n",
    "print(f\"Shortest path from {SRC} to {DST} is: {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "6e8588a4-61a9-4458-a7f7-36048dae548c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Dijkstra_recursive(G, src, dst, pq=G.PQ):\n",
    "    if src == dst:\n",
    "        return G.distances[dst]\n",
    "    G.visited[src] = 1\n",
    "\n",
    "    for neighbour, dist in enumerate(G.adj_mat[src]):\n",
    "        if dist <= 0 or G.visited[neighbour]:\n",
    "            continue\n",
    "        heapq.heappush(pq, (dist, neighbour))\n",
    "        new_dist = dist + G.distances[src]\n",
    "        if new_dist < G.distances[neighbour]:\n",
    "            G.distances[neighbour] = new_dist\n",
    "    return Dijkstra_recursive(G, heapq.heappop(pq)[1], dst, pq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "ed7967ad-171a-40c2-b76c-a7f43dab0a2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shortest path from 4 to 5 is: 8\n"
     ]
    }
   ],
   "source": [
    "N = 6\n",
    "SRC = 4\n",
    "DST = 5\n",
    "\n",
    "G = Graph(N)\n",
    "G.add_edge(4, 0, 2)\n",
    "G.add_edge(0, 1, 1)\n",
    "G.add_edge(4, 2, 3)\n",
    "G.add_edge(2, 0, 4)\n",
    "G.add_edge(2, 3, 2)\n",
    "G.add_edge(3, 5, 3)\n",
    "G.add_edge(1, 3, 5)\n",
    "G.add_edge(5, 1, 4)\n",
    "\n",
    "G.distances[SRC] = 0\n",
    "result = Dijkstra_recursive(G, SRC, DST, G.PQ)\n",
    "print(f\"Shortest path from {SRC} to {DST} is: {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd8cd360-4c95-4586-829c-9e65f9aacde0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d775d61d-10d0-4395-838a-4ee27ddc9a0b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

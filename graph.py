#!/usr/bin/env python

from random import randint

class Graph():

  DEFAULT_GRAPH = [
    [0,7,6,2,1],
    [7,0,5,3,3],
    [6,5,0,1,2],
    [2,3,1,0,7],
    [1,3,2,7,0],
  ]

  DEFAULT_SIZE = 5

  def __init__(self, mode="default"):
    if mode == "default":
      self._graph = self.DEFAULT_GRAPH
    elif mode == "random":
      self._graph = self._random_graph_()
    else:
      raise Exception("Not implemented yet")

  ############################################################################################################
  ## GET FUNCTIONS

  def get_size(self):
    return len(self._graph)

  def get_graph(self):
    return self._graph

  ############################################################################################################
  ## OTHER FUNCTIONS

  def _random_graph_(self):
    graph = []
    for i in xrange(self.DEFAULT_SIZE):
      graph.append([])
      for j in xrange(self.DEFAULT_SIZE):
        if i == j:
          graph[i].append(0)
        else:
          graph[i].append(randint(0,8))
    return graph

  def print_graph(self):
    print self._graph

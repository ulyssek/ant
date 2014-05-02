#!/usr/bin/env python

from random import randint

class Graph():

  ############################################################################################################
  ## CLASS VARS

  DEFAULT_GRAPH = [
    [0,7,6,2,1],
    [7,0,5,3,3],
    [6,5,0,1,2],
    [2,3,1,0,7],
    [1,3,2,7,0],
  ]

  DEFAULT_SIZE = 5

  ############################################################################################################
  ## INIT FUNCTIONS

  def __init__(self, mode="default"):
    if mode == "default":
      self._graph = self.DEFAULT_GRAPH
    elif mode == "random":
      self._graph = self._random_graph_()
    else:
      raise Exception("Not implemented yet")

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

  ############################################################################################################
  ## GET FUNCTIONS

  def get_size(self):
    return len(self._graph)

  def get_graph(self):
    return self._graph

  ############################################################################################################
  ## GRAPH ALTERATION FUNCTIONS

  def minus(self, minus):
    for i in xrange(self.get_size()):
      for j in xrange(self.get_size()):
        self._graph[i][j] = max(0, self._graph[i][j]-minus)

  def normalize(self):
    for i in xrange(self.get_size()):
      sum_weight = sum(self._graph[i])
      self._graph[i] = map(lambda x : float(x)/sum_weight, self._graph[i])

  ############################################################################################################
  ## PRINTING FUNCTIONS

  def __str__(self):
    return str(self._graph)

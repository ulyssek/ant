#!/usr/bin/env python

from graph import Graph
from random import uniform

class Algo():

  DEFAULT_WEIGTH = 0.5

  def __init__(self):
    self.initial_graph = Graph()
    self.current_graph = self.initial_graph
    self.ant_positions = range(self.initial_graph.get_size())
    self.initial_graph.print_graph()

  def run(self):
    for ant in self.ant_positions:
      self.__next_position__(ant)

  def __next_position__(self, ant):
    graph_line = self.current_graph.get_graph()[ant]
    sum_weight = sum(graph_line)
    probas = map(lambda x : float(x)/sum_weight, graph_line)
    random_number = uniform(0., 1.)
    count = 0
    for i in xrange(len(probas)):
      count += probas[i]
      if count >= random_number:
        print probas
        print random_number
        print i
        return i

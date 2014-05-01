#!/usr/bin/env python

from graph import Graph


class Algo():
  
  def __init__(self):
    self.initial_graph = Graph()
    self.current_graph = self.initial_graph

    self.ant_position = range(self.initial_graph.get_size())

    self.initial_graph.print_graph()
    print self.ant_position
    



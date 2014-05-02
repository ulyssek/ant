#!/usr/bin/env python
# -*- coding:utf-8 -*-

from graph import Graph
from random import uniform

class Algo():

  ############################################################################################################
  ## CLASS VARS
  DEFAULT_WEIGHT  = 0.1
  ITERATIONS      = 10

  ############################################################################################################
  ## INIT FUNCTIONS

  def __init__(self, mode="classic"):
    self.mode = mode
    self.initial_graph = Graph()
    self.current_graph = self.initial_graph
    self.ant_positions = range(self.initial_graph.get_size())

  ############################################################################################################
  ## RUNNING FUNCTIONS

  def launch(self):
    for i in xrange(self.ITERATIONS):
      self._run()
      self.print_current()

  def _run(self):
    """
    lance une itération de l'algorithme
    """
    running_edges = []
    for i in xrange(len(self.ant_positions)):
      next_position = self.__next_position__(self.ant_positions[i])
      running_edges.append((self.ant_positions[i], next_position))
      self.ant_positions[i] = next_position 
    self.__update__(running_edges)

  ############################################################################################################
  ## UPDATE FUNCTIONS
  
  def __update__(self, edges):
    """
    Update des poids du graphe
    """
    for i, j in edges:
      self.current_graph.get_graph()[i][j] += self.DEFAULT_WEIGHT*2
      self.current_graph.get_graph()[j][i] += self.DEFAULT_WEIGHT*2
    self.current_graph.minus(self.DEFAULT_WEIGHT) 
    
  ############################################################################################################
  ## PRINTING FUNCTIONS 

  def print_current(self):
    print "ant's positions :"
    print self.ant_positions
    print "Current graph : "
    print self.current_graph

  ############################################################################################################
  ## OTHER FUNCTIONS
  def __next_position__(self, ant):
    """
    Calcul la prochaine position d'une fourmies données à partir du graphe courant
    """
    graph_line = self.current_graph.get_graph()[ant]
    sum_weight = sum(graph_line)
    if sum_weight == 0:
      #Si toutes les voies sont coupées, la fourmies ne bouge pas
      return ant
    #Calcul du vecteur de probabilité
    probas = map(lambda x : float(x)/sum_weight, graph_line)
    # Détermination de la position suivante
    random_number = uniform(0., 1.)
    count = 0
    for i in xrange(len(probas)):
      count += probas[i]
      if count >= random_number:
        return i
    #sum(probas)==1, donc le script ne peut pas sortir de cette boucle autrement que pas un return.

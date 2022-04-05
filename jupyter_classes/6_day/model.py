#! /usr/bin/env python
# https://docs.python.org/3/library/argparse.html
import argparse
from collections import defaultdict # for income graph
import json
import math

import matplotlib as mil
#mil.use('agg') # add it before launching matplotlib
import matplotlib.pyplot as plt
# static method



class Agent:

    def __init__(self, position, **properties):
        pass


class Position:

    def __init__(self, longitude_degrees, latitude_degrees):
        # We store the degree values, but we will be mostly using radians
        # because they are much more convenient for computation purposes.

        # assert : Lève une exception si renvoie False
        pass


    @property
    def longitude(self):
        """Longitude in radians"""
        pass

    @property
    def latitude(self):
        """Latitude in radians"""
        pass


class Zone:
    """
    A rectangular geographic area bounded by two corners. The corners can
    be top-left and bottom right, or top-right and bottom-left so you should be
    careful when computing the distances between them.
    """


    # The width and height of the zones that will be added to ZONES. Here, we
    # choose square zones but we could just as well use rectangular shapes.

    # Attributs de classe (constante si hors de la classe) car on fait 
    # cls.WIDTH_DEGREES

   # degrees of longitude
     # degrees of latitude

    # S'il y a un attribut d'instance, il va dans __init__



    def __init__(self, corner1, corner2):
        pass

    @property
    def population(self):
        """Number of inhabitants in the zone"""
        pass
    @property
    def width(self):
        """Zone width, in kilometers"""
        # Note that here we access the class attribute via "self" and it
        # doesn't make any difference
        pass
    @property
    def height(self):
        """Zone height, in kilometers"""
        # Note that here we access the class attribute via "self" and it
        # doesn't make any difference
        pass
    def add_inhabitant(self, inhabitant):
        pass
    def population_density(self):
        """Population density of the zone, (people/km²)"""
        # Note that this will crash with a ZeroDivisionError if the zone has 0
        # area, but it should really not happen
        pass
    def area(self):
        """Compute the zone area, in square kilometers"""
        pass
    def average_agreeableness(self):
        pass
    def contains(self, position):
        """Return True if the zone contains this position"""
        pass

    @classmethod
    def find_zone_that_contains(cls, position):
        # Initialize zones automatically if necessary

        # Compute the index in the ZONES array that contains the given position


        # Just checking that the index is correct
       pass
    @classmethod
    def _initialize_zones(cls):
        # Note that this method is "private": we prefix the method name with "_".
        pass

# () ne se fait pas trop.
# Ceci est un mixin ?
class BaseGraph:

    def __init__(self):
       pass

    def show(self, zones):
        pass

    def plot(self, x_values, y_values):
        """Override this method to create different kinds of graphs, such as histograms"""
        # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
        pass
    def xy_values(self, zones):
        """
        Returns:
            x_values
            y_values
        """
        # You should implement this method in your children classes
        raise NotImplementedError


class AgreeablenessGraph(BaseGraph):
    # Inheritance, yay!

    def __init__(self):
        # Call base constructor
        pass

    def xy_values(self, zones):
        pass

class IncomeGraph(BaseGraph):
    # Inheritance, yay!

    def __init__(self):
        # Call base constructor
        pass

    def xy_values(self, zones):
        pass


def main():
    # Si on avait mis tout ça en bas, on aurait eu beaucoup de variables globales.
    parser = argparse.ArgumentParser("Display population stats")
    parser.add_argument("src", help="Path to source json agents file")
    args = parser.parse_args()

    # Load agents
    for agent_properties in json.load(open(args.src)):
        longitude = agent_properties.pop('longitude')
        latitude = agent_properties.pop('latitude')
        # store agent position in radians
        position = Position(longitude, latitude)

        zone = Zone.find_zone_that_contains(position)
        agent = Agent(position, **agent_properties)
        zone.add_inhabitant(agent)

    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)

    income_graph = IncomeGraph()
    income_graph.show(Zone.ZONES)

if __name__ == "__main__":
    main()



from xml.etree.cElementTree import iterparse
import geopy.distance
from shapely import geometry as shgm
import numpy as np
import logging 
from my_util import MyGridBin  
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection 
 
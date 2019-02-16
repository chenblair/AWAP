"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
andrewid1
andrewid2
andrewid3
andrewid4
"""
from awap2019 import Tile, Direction, State

import pdb

import numpy as np

class Team(object):
  def __init__(self, initial_board, team_size, company_info):
    self.board = np.array(initial_board)

    self.team_size = team_size # will always be 4
    self.company_base_value = company_info # company value decreases by half everytime we visit
                                           # helper gets half the advertised value
    self.team_name = "sudoers"

    numrows,numcols = self.board.shape
    self.company_booths = {
      company: 
        [(r,c) for r in range(numrows) for c in range(numcols) if self.board[(r,c)].get_booth()==company]
      for company in company_info
    }
    self.company_line_zones = {
      company: 
        [(r,c) for r in range(numrows) for c in range(numcols) if self.board[(r,c)].get_line()==company]
      for company in company_info
    }

    pdb.set_trace()

  def exp_dist(self,srcpos,dest,visible_board):
    pass

  def closest(self,srcpos,company): pass

  def step(self, visible_board, states, score):
    pdb.set_trace()
    dirs = []
    for p in states:
      pr = p.x
      pc = p.y
      # update the expected distance to each company based on FOV and state
      company_closest_tile = {
        company:
        self.closest((pr,pc),company) 
        for company in self.company_base_value
      }
      
      company_exp_dist = {
        company:
        self.exp_dist((pr,pc),company_closest_tile[company],visible_board)
        for company in self.company_base_value
      }

      bestvalue = 0
      bestcomp = None
      for comp in company_exp_dist:
        v = self.company_base_value[comp]/company_exp_dist[comp] 
        if v>bestvalue:
          bestvalue = v
          bestcomp = comp
        
      # assign p to go toward bestcomp
      self.company_base_value[bestcomp] /= 2
      desttile = company_closest_tile[bestcomp]
      dr = desttile[0] - pr
      dc = desttile[1] - pc
      dir2add = None
      # if dr>0 and dc >0: dir2add = Direction.



    return [Direction.UP,Direction.NONE,Direction.NONE,Direction.NONE]

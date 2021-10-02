#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 00:06:52 2021

@author: erictang
"""

import numpy as np
import random
import time
import concurrent.futures
from math import comb

# 模擬多次次
SIMULATION_ROUNDS = 100000

# +7 => +10 時使用安全精鍊(+4 => +7 用普通精鍊比較便直)
ENABLE_SAFE_REFINE = True

# Multithreading
ENABEL_MULTITHREADED_SIMULATION = False
EXECUTOR = concurrent.futures.ThreadPoolExecutor(max_workers=64)

# map from "source refine level" to (成功機率,失敗機率,紅槌機率,安精成本)
REFINE_PROFILE = {
  0: (1, 0, 0, 0),
  1: (1, 0, 0, 0),
  2: (1, 0, 0, 0),
  3: (1, 0, 0, 0),
  4: (0.5, 0.25, 0.25, 1),
  5: (0.5, 0.25, 0.25, 2),
  6: (0.4, 0.3, 0.3, 3),
  7: (0.4, 0.3, 0.3, 4),
  8: (0.4, 0.3, 0.3, 6),
  9: (0.4, 0.3, 0.3, 8),
  10: (0.4, 0, 0.6, None),
  11: (0.4, 0, 0.6, None),
  12: (0.4, 0, 0.6, None),
  13: (0.4, 0, 0.6, None),
  14: (0.4, 0, 0.6, None),
}


class Item:
  refine_level = 0
  total_cost = 0
  refine_history = [0]
  
  def  __init__(self, refine_level):
    self.refine_level = refine_level
    self.refine_history = [refine_level]
  
  # 精鍊一次(安全/普通,視乎等級)
  def refine(self):
    # It's cheaper to use regular refine in +4 => +7,
    # so only enable safe refine in +7 => +10
    if ENABLE_SAFE_REFINE and (7 <= self.refine_level and self.refine_level <= 9):
      self._safe_refine()
    else:
      self._regular_refine()
    self.refine_history.append(self.refine_level)

  # 安全精鍊一次
  def _safe_refine(self):
    source_level_profile = REFINE_PROFILE[self.refine_level]
    self.refine_level += 1
    self.total_cost += source_level_profile[3]
    
  # 普通精鍊一次
  def _regular_refine(self):
    # This is just so that Variable Explorer can show the content of this object
    debugItemString = "+%d, cost: %d, %s"% (self.refine_level, self.total_cost, self.refine_history)
    
    r = random.random() # 0.0 <= r < 1.0
    source_level_profile = REFINE_PROFILE[self.refine_level]
    if r < source_level_profile[0]: # success
      self.refine_level += 1
    elif r < source_level_profile[0] + source_level_profile[1]: # fail
      self.refine_level -= 1
    else: # broken
      self.refine_level -= 1
      self.total_cost += 1 # cost of repairing it, assume that we always repair
    
  @staticmethod
  def _simulate_once(source_level, target_level):
    item = Item(source_level)
    while item.refine_level < target_level:
      item.refine()
    return item

  @staticmethod
  def simulate(times, source_level, target_level):
    if ENABEL_MULTITHREADED_SIMULATION:
      futures = []
      for i in range(times):
        futures.append(EXECUTOR.submit(lambda p: Item._simulate_once(p[0], p[1]), (source_level, target_level)))
      return [future.result() for future in futures]
    else:
      return [Item._simulate_once(source_level, target_level) for i in range(times)]
    

def run_simulation(times):
  for target_level in range(5,16): # 5-15 inclusive
    source_level = target_level - 1
    t0 = time.time()
    items = Item.simulate(times, source_level, target_level)
    t1 = time.time()
    dt = t1-t0
    costs = np.array([item.total_cost for item in items])
    refine_lengths = np.array([len(item.refine_history)-1 for item in items])
    print("Simulating +%d%s => +%d%s: cost(mean, 75/90/95%%-tile): %s, %s/%s/%s. mean refine length: %s (slmulation elapsed time: %.02fs)" % (
      source_level,
      " " if source_level < 10 else "",
      target_level,
      " " if target_level < 10 else "",
      "{:7.3f}".format(costs.mean()),
      "{:6.2f}".format(np.percentile(costs, 75)),
      "{:6.2f}".format(np.percentile(costs, 90)),
      "{:6.2f}".format(np.percentile(costs, 95)),
      "{:7.3f}".format(refine_lengths.mean()),
      dt
      ))


print("Simulation (%d rounds for each target level):" %SIMULATION_ROUNDS )
run_simulation(SIMULATION_ROUNDS)

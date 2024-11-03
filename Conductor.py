import pandas as pd


def timeStepper():
  #timeStepper?
  timestep = 15
  return timestep

def importSubOut(timestep):
  #get .csv for sub out ready and store as pandas dataframe
  subOut = []
  return subOut

def importSubIn(timestep):
  #get .csv for sub in results
  subIn = []
  return subIn

def subMatcher(subOut, subIn):
  #give results to match ranker
  matches = []
  return matches

def conductor():
  timestep = timeStepper()
  subOut = importSubOut(timestep)
  subIn = importSubIn(timestep)
  matches = subMatcher(subOut, subIn)
  return matches

conductor()


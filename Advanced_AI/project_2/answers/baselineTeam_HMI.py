# baselineTeam.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# baselineTeam.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from captureAgents import CaptureAgent
import distanceCalculator
import random, time, util, sys
from game import Directions
import game
from util import nearestPoint


from agents import ApproximateAdversarialAgent

#################
# Team creation #
#################

def createTeam(firstIndex, secondIndex, isRed,
               first = 'OffensiveReflexAgent', second = 'DefensiveReflexAgent'):
  """
  This function should return a list of two agents that will form the
  team, initialized using firstIndex and secondIndex as their agent
  index numbers.  isRed is True if the red team is being created, and
  will be False if the blue team is being created.

  As a potentially helpful development aid, this function can take
  additional string-valued keyword arguments ("first" and "second" are
  such arguments in the case of this function), which will come from
  the --redOpts and --blueOpts command-line arguments to capture.py.
  For the nightly contest, however, your team will be created without
  any extra arguments, so you should make sure that the default
  behavior is what you want for the nightly contest.
  """
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########

class ReflexCaptureAgent(ApproximateAdversarialAgent):
  """
  A base class for reflex agents that chooses score-maximizing actions
  """
 
  def registerInitialState(self, gameState):
    ApproximateAdversarialAgent.registerInitialState(self, gameState)
    self.start = gameState.getAgentPosition(self.index)

  def chooseAction(self, gameState):
    """
    Picks among the actions with the highest Q(s,a).
    """
    actions = gameState.getLegalActions(self.index)

    # You can profile your evaluation time by uncommenting these lines
    # start = time.time()
    values = [self.evaluate(gameState, a) for a in actions]
    # print 'eval time for agent %d: %.4f' % (self.index, time.time() - start)

    maxValue = max(values)
    bestActions = [a for a, v in zip(actions, values) if v == maxValue]

    foodLeft = len(self.getFood(gameState).asList())

    if foodLeft <= 2:
      bestDist = 9999
      for action in actions:
        successor = self.getSuccessor(gameState, action)
        pos2 = successor.getAgentPosition(self.index)
        dist = self.getMazeDistance(self.start,pos2)
        if dist < bestDist:
          bestAction = action
          bestDist = dist
      return bestAction

    print("DDDDDDDDebug for all actions")
    for  a, v in zip(actions, values):
      print(a,v)
    print("best actions are:")
    print(bestActions)

    return random.choice(bestActions)

  def getSuccessor(self, gameState, action):
    """
    Finds the next successor which is a grid position (location tuple).
    """
    successor = gameState.generateSuccessor(self.index, action)
    pos = successor.getAgentState(self.index).getPosition()
    if pos != nearestPoint(pos):
      # Only half a grid position was covered
      return successor.generateSuccessor(self.index, action)
    else:
      return successor

  def evaluate(self, gameState, action):
    """
    Computes a linear combination of features and feature weights
    """
    features = self.getFeatures(gameState, action)
    weights = self.getWeights(gameState, action)
    return features * weights

  def getFeatures(self, gameState, action):
    """
    Returns a counter of features for the state
    """
    features = util.Counter()
    successor = self.getSuccessor(gameState, action)
    features['successorScore'] = self.getScore(successor)
    return features

  def getWeights(self, gameState, action):
    """
    Normally, weights do not depend on the gamestate.  They can be either
    a counter or a dictionary.
    """
    return {'successorScore': 1.0}

  def debug_pause(self):
    import os
    #os.system("pause")

class DefensiveReflexAgent(ReflexCaptureAgent):
  """
  A reflex agent that keeps its side Pacman-free. Again,
  this is to give you an idea of what a defensive agent
  could be like.  It is not the best or only way to make
  such an agent.
  """

  def getFeatures(self, gameState, action):
    features = util.Counter()
    successor = self.getSuccessor(gameState, action)

    myState = successor.getAgentState(self.index)
    myPos = myState.getPosition()

    # Computes whether we're on defense (1) or offense (0)
    features['onDefense'] = 1
    if myState.isPacman: features['onDefense'] = 0

    # Computes distance to invaders we can see
    enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
    invaders = [a for a in enemies if a.isPacman and a.getPosition() != None]
    features['numInvaders'] = len(invaders)
    if len(invaders) > 0:
      # dists = [self.getMazeDistance(myPos, a.getPosition()) for a in invaders]
      # features['invaderDistance'] = min(dists)
      opponentDistances = self.getOpponentDistances(gameState)
      opponentDistance = min([dist for id, dist in opponentDistances])
      features['invaderDistance'] = opponentDistance

    if action == Directions.STOP: features['stop'] = 1
    rev = Directions.REVERSE[gameState.getAgentState(self.index).configuration.direction]
    if action == rev: features['reverse'] = 1

    return features

  def getWeights(self, gameState, action):
    return {'numInvaders': -1000, 'onDefense': 100, 'invaderDistance': -10, 'stop': -100, 'reverse': -2}


class OffensiveReflexAgent(ReflexCaptureAgent):
  """
  A reflex agent that seeks food. This is an agent
  we give you to get an idea of what an offensive agent might look like,
  but it is by no means the best or only way to build an offensive agent.
  """
  # def getFeatures(self, gameState, action):
  #   features = self.getAllFeatures(gameState, action)
  #   return features


  def print_features(self, state, action, features):
    print("Calc done, we have:")
    print(state.getAgentState(self.index).getPosition())
    print(action)
    print(features)
    #self.debug_pause()
        

  def getFeatures(self, state, action):
    # extract the grid of food and wall locations and get the ghost locations
    
    features = util.Counter()

    successor = self.getSuccessor(state, action)      
    now_state = state.getAgentState(self.index)
    successor_state = successor.getAgentState(self.index)
    now_state_pos = now_state.getPosition()
    x,y = now_state_pos
    successor_pos = successor_state.getPosition()
    next_x, next_y = successor_pos


    # we do not want agent be stop
    if action == Directions.STOP: features['stop'] = 1
    rev = Directions.REVERSE[now_state.configuration.direction]
    if action == rev: features['reverse'] = 1


    # going to enter opponent side, set home point
    if now_state.isPacman == False and successor_state.isPacman == True:
        print("Going to reset the home_point!")            
        home_foodList = self.getFoodYouAreDefending(successor).asList()
        if len(home_foodList) > 0:
          self.home_point = random.choice(home_foodList)
        print(self.home_point)
        self.debug_pause()

    # if we are a pacman, we should care about ghost
    if successor_state.isPacman:
      opponentDistances = self.getOpponentDistances(successor) # we calc the successor's dis to the opponent
      opponentDistance = min([dist for id, dist in opponentDistances])
      features['ghostDistance'] = opponentDistance
    if features['ghostDistance'] > 5 or features['ghostDistance'] == 0: # to far away ghost, we don't care too much
      features['ghostDistance'] = 5 # just a hardcode value


    # if we already eat some points and have not save it (back to our side), say 5, save it first
    opponent_food_left_now = self.getFood(state).asList()
    if now_state.numCarrying >= 5 or len(opponent_food_left_now) <= 2:
      print("Maybe we should go home, our score {}, and eaten but not saved {}, remains {} points \n".format(self.getScore(state), now_state.numCarrying, len(opponent_food_left_now)))
      #self.debug_pause()
      features['homeDistance'] = self.getMazeDistance(successor_pos, self.home_point)

      ## return
      self.print_features(state, action, features)
      return features
    

    food = self.getFood(successor)
    foodList = self.getFood(successor).asList()
    features['successorScore'] = -len(foodList)#self.getScore(successor)

    foodList = self.getFood(successor).asList()
    # Compute distance to the nearest food
    if len(foodList) > 0: # This should always be True,  but better safe than sorry
      minDistance = min([self.getMazeDistance(successor_pos, food) for food in foodList])
      #features["closest-food"] = float(minDistance) / (walls.width * walls.height)
      features['distanceToFood'] = minDistance

    self.print_features(state, action, features)
    return features

  def getWeights(self, gameState, action):
    #return {'successorScore': 100, 'distanceToFood': -1}
    #return {'successorScore': 100, 'distanceToFood': -1, 'invaderDistance': -10}
    #return {'successorScore': 20.0, 'ghostDistance': 3, '#-of-nearby-ghosts':-1.0, "distanceToFood": -2.0, 'stop': -10.0, 'reverse': -2.0, 'homeDistance': -20.0}
    return {'successorScore': 30.0, 'ghostDistance': 3.0, 'distanceToFood': -2.0, 'stop': -50.0, 'reverse': -5.0, 'homeDistance': -20.0}

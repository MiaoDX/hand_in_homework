# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        import os
        
        all_states = self.mdp.getStates()
        for i in range(self.iterations): # do not take the last one?
            Tmp_value = util.Counter() # UPDATE AFTER ALL CALCULATED
            for state in all_states:
                #print(state)
                V_action = self.computeActionFromValues(state)
                if not V_action == None:
                    #print("going to set {} to {}".format(state, self.computeQValueFromValues(state, V_action)))
                    Tmp_value[state] = self.computeQValueFromValues(state, V_action)
            
            self.values = Tmp_value
            #os.system("pause")

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        successors = self.mdp.getTransitionStatesAndProbs(state, action)

        Q_value = 0.0

        for (nextState, prob) in successors:
            tmp_next_state_value = self.values[nextState]
            tmp_reward = self.mdp.getReward(state, action, nextState)
            Q_value += prob*(tmp_reward + tmp_next_state_value*self.discount) # pay attention to the discount and prob
        
        return Q_value

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        if self.mdp.isTerminal(state):
            return None

        possible_actions = self.mdp.getPossibleActions(state)

        Q_values = util.Counter()
        for action in possible_actions:
            tmp_Q_value = self.computeQValueFromValues(state, action)
            Q_values[action] = tmp_Q_value
        
        V_action = Q_values.sortedKeys()[0]

        return V_action

        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

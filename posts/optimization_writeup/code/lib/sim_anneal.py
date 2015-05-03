import numpy as np


################################################################################
# holds configuration information
class AnnealConfig(object):
    """the state of a simulated annealing run"""

    def __init__(self, minDomain, maxDomain, maxIterations):
        self.minDomain = minDomain
        self.maxDomain = maxDomain
        self.maxIterations = maxIterations


################################################################################
# function that returns a probability that a new state will be accepted
def Acceptance(currentStateEnergy, newStateEnergy, temperature):

    if(newStateEnergy < currentStateEnergy):
        return 1.0

    return np.exp( ( - ( newStateEnergy - currentStateEnergy ) ) / temperature )


################################################################################
# function to generate neighbors
def GetNeighbor(lbound, ubound, currentTemp, currentState):

    std = np.minimum(np.sqrt(currentTemp) * np.ones(len(currentState)),
                  (ubound - lbound) / 1.5)

    x0 = np.asarray(currentState)

    xc = np.random.normal(0, 1.0, size=len(currentState))

    xnew = x0 + xc*std*0.5

    return xnew


################################################################################
# temperature function, aka 'cooling schedule'
def GetNewTemp(initialTemp, iterNumber):

    return initialTemp / np.log(iterNumber + 2)


################################################################################
# pick an appropriate initial temperature and state
def InitTempAndState(config, f):

        # note: maxValueAtPoint is set to 64bit double min
        #       minValueAtPoint is set to 64bit double max
        maxValueAtPoint = np.finfo(float).min
        minValueAtPoint = np.finfo(float).max

        bestValueAtPoint = None
        bestPoint = None

        for _ in range(50):

            point = np.random.uniform(size=2) * ( config.maxDomain - config.minDomain ) + config.minDomain
            valueAtPoint = f(point)

            if valueAtPoint > maxValueAtPoint:
                maxValueAtPoint = valueAtPoint

            if valueAtPoint < minValueAtPoint:
                minValueAtPoint = valueAtPoint
                bestValueAtPoint = valueAtPoint
                bestPoint = np.array(point)

        return ((maxValueAtPoint-minValueAtPoint)*1.5, bestPoint)


################################################################################
# takes configuration information and a function to minimize as arguments
def SimAnneal(config, f):

    initialTemp, initialGuess = InitTempAndState(config, f)

    # current state of the simulation
    currentState = initialGuess;
    currentStateEnergy = f(initialGuess)

    # keeps track of the best (most minimum) state
    bestState = initialGuess;
    bestStateEnergy = f(initialGuess)

    temp = initialTemp

    iterations = 0
    localSearchStep = 200

    while iterations < config.maxIterations:

        for n in xrange(localSearchStep):
            newStateProspect = GetNeighbor(config.minDomain, config.maxDomain, temp, currentState)
            newStateProspectEnergy = f(newStateProspect)

            if(Acceptance(currentStateEnergy, newStateProspectEnergy, temp) > np.random.uniform(0.0, 1.0)):

                currentState = newStateProspect
                currentStateEnergy = newStateProspectEnergy

                if currentStateEnergy < bestStateEnergy:
                    bestState = currentState.copy()
                    bestStateEnergy = currentStateEnergy

        temp = GetNewTemp(initialTemp, iterations)

        iterations = iterations + 1


    return (bestState, bestStateEnergy)





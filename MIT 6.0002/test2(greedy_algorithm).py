# provided data: food name, food value, food calories, max value, max calories
# output: list of the results

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value)\
              + ', ' + str(self.calories) + '>'

    def buildMenu(names, values, calories):
        # init object
        menu = []
        for i in range(len(values)):
            menu.append(Food(names[i], values[i], calories[i]))

        return menu
    def greedy(items, maxCost, keyFunction):
        itemsCopy = sorted(items, key = keyFunction, reverse = True)
        result = []
        totalValue, totalCost = 0.0, 0.0

        for i in range(len(itemsCopy)):
            if (totalCost + Food.getCost(itemsCopy[i])) <= maxCost:
                result.append(itemsCopy[i])
                totalCost += (Food.getCost(itemsCopy[i]))
                totalValue += (Food.getValue(itemsCopy[i]))

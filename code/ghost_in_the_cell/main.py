import sys

class Factory():
    """
    class for factory data
    ------
    owner : factory owner
    bot : number of bot in the factory
    prod : production of the factory
    cooldown : cooldown before the factory restart
    link : (destination of link ; distance from destination)
    """

    def __init__(self):
        self.link = []

    def linkTo(self, des, dis):
        self.link.append((des, dis))

    def update(self, arg0, arg1, arg2, arg3, arg4):
        self.owner = int(arg0)
        self.bot = int(arg1)
        self.prod = int(arg2)
        self.cooldown = int(arg3)
        self.id = int(arg4)


factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
factorys = [Factory() for i in range(factory_count)]

# make link
for i in range(link_count):
    l = [int(j) for j in input().split()]
    factorys[l[0]].linkTo(l[1], l[2])
    factorys[l[1]].linkTo(l[0], l[2])

# * main loop
while True:

    # collect data
    troop_data = []
    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]

        # factory entity
        if entity_type == "FACTORY":
            factorys[entity_id].update(*inputs[2:6], entity_id)

        # troop entity
        elif entity_type == "TROOP":
            if int(inputs[2]) == 1:
                troop_data.append(int(inputs[4]))
            else:
                factorys[int(inputs[2])].bot += int(inputs[5])

    # get all possible action
    move = [-1, 0, 0, -10]
    for f in factorys:
        if f.owner == 1:
            for link in f.link:
                if factorys[link[0]].owner != 1:
                    # get minimun bot to get the factory
                    requiredBot = factorys[link[0]].bot + \
                        (factorys[link[0]].prod * link[1]) + 1
                    if requiredBot <= f.bot and not link[0] in troop_data:

                        # set priority
                        priority = (factorys[link[0]].prod / 3 * 10) + (abs(factorys[link[0]].owner) * 5) - (
                            (requiredBot * 0.1)) + (link[1] / 5)
                        if move[3] < priority:
                            move = [f.id, link[0], requiredBot, priority]

    # output
    print("WAIT", end="")
    if move[0] != -1:
        print(";MOVE {} {} {}".format(move[0], move[1], move[2]), end="")
    print("")

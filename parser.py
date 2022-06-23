class Parser:
    def __init__(self):
        self.arguments = []

    def add_argument(self, arglist, returnFunc):
        self.arguments.append((arglist, returnFunc))

    def argument(self, arglist):
        def in_argument(func):
            self.arguments.append((arglist, func))
        return in_argument

    def parse(self, toks):
        tree = []
        while len(toks) > 0:
            for argNames, argFunc in self.arguments:
                arglen = len(argNames)
                argstreak = 0
                for tokName, tokVal in toks:
                    if tokName == argNames[argstreak]:
                        argstreak += 1

                    if argstreak == arglen:
                        tree.append(argFunc(*toks[:arglen]))
                        toks = toks[arglen:]
                        break

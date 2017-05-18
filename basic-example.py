class arguments:
    def __init__(self, ArgsDict):
        self.autoversion = ArgsDict["autoversion"]
        self.value  = ArgsDict["value"]
        
        
ArgsDict = dict(
    value = "value1",
    autoversion = True
)

args = arguments(ArgsDict)

if args.autoversion:
    print("I am set to true")
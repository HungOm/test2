class Robot:
    population = 0
    def __init__(self,name):
        self.name =name
        Robot.population += 1
    def say_hi(self):
        print("Hi,my name is:,", self.name)
    def die(self):
        Robot.population -= 1
        if Robot.population == 0:
            print("That was the last one.")
        else:
            print("There are more robots.")
    @classmethod
    def how_many(cls):
        print("We have",cls.population)


droid1 = Robot('Android')
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C3P0")
droid2.say_hi()
Robot.how_many()
droid2.die()
Robot.how_many()

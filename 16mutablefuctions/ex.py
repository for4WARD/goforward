class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost=3
    

    def nearest_bee(self, beehive, min_range=Ant.min_range  , max_range =Ant.max_range):
        """Return the nearest Bee in a Place that is not the HIVE (beehive), connected to
        the ThrowerAnt's Place by following entrances.
        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        target = self.place
        for _ in range(min_range): # Move the first targeting pllace to the min range.
            target = target.entrance
            if target is beehive:
                return None

        distance = min_range
        while target is not beehive and distance <= max_range:
            if target.bees:
                return rANTdom_else_none(target.bees)
            else:
                distance += 1
                target = target.entrance
        return None
        # END Problem 3 and 4


    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, gamestate):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(gamestate.beehive))

def rANTdom_else_none(s):
    """Return a random element of sequence S, or return None if S is empty."""
    assert isinstance(s, list), "rANTdom_else_none's argument should be a list but was a %s" % type(s).__name__
    if s:
        return random.choice(s)

##############
# Extensions #
##############

class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = 'Short'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    min_range=0
    max_range=3
    implemented = True
    
    
    
     
    
    # END Problem 4

class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = 'Long'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
     
    min_range=5
    max_range=float('inf')
    implemented = True
    
    # END Problem 4
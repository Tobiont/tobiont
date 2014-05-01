import random
from tobiont import resource


class AbstractWeather(object):
  region = ""
  biome = ""

  def __init__(self, region, biome):
    self.region = region
    self.biome = biome

  def run(self):
    """Accepts reference to weather's owning gridsquare and runs rules.

    This method should be overridden by subclasses.
    """
    pass

class RaineyWeather(AbstractWeather):
  """Impliments Rain weather conditions.

  Rain is a weather condition where the game square has a random chance
  of generating a resource every turn and a random chance that the square
  will 'dry up' each turn, removing resources.
  """

  def __init__(self, region, biome):
    super(RaineyWeather, self).__init__(region, biome)

  def run(self, game_square):
    """Impliments weather rules.

    @override

    """
    rain_chance = random.randint(1,4)

    if rain_chance <= 1:
      #rain
      game_square.addResource(resource.Resource('basic', 1))
    elif rain_chance >= 4:
      #dry up
      game_square.withdrawResource(resource.Resource('basic', 1))
    #else do nothing

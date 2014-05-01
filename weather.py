import random
from tobiont import resource


class AbstractWeather(object):
  _region = ""
  _biome = ""

  def __init__(self, region, biome):
    self._region = region
    self._biome = _biome

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
    super(raineyWeather, self).__init__(region, biome)

  def run(self):
    """Impliments weather rules.

    @override

    """
    rain_chance = random.randint(1,4)

    if rain_chance <= 1:
      #rain
      self.addResource(resource('basic', 1))
    elif rain_chance >= 4:
      #dry up
      self.removeResource(resource('basic', 1))


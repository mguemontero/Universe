"""
	Defining classes for modeling Solar System.
"""
class Galaxy:
	"""A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas, 
	   dust, and dark matter.
	"""
	def __init__(self, name, shape):
		self.name = name
		self.shape = shape
		
class Planet:
	"""A planet is an astronomical body orbiting a star or stellar remnant that is massive enough 
	   to be rounded by its own gravity, is not massive enough to cause thermonuclear fusion, and 
	   has cleared its neighbouring region of planetesimals.
	"""
	def __init__(self, name, orbit=None, axial_tilt=None, rotation=None, color=None):
		self.name = name
		self.orbit = orbit
		self.axial_tilt = axial_tilt
		self.rotation = rotation
		self.color = color


class Star:
	"""A star is type of astronomical object consisting of a luminous spheroid of plasma
	   held together by its own gravity.
	"""
	def __init__(self, name, age=None, mass=None, temperature=None):
		self.name = name
		self.age = age
		self.mass = mass
		self.temperature = temperature

Planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune']
solar_system = []

for planeta in Planets:
	solar_system.append(Planet(planeta))
# [Planet(planeta) for planeta in Planets]

# Planets as dictionaries

Earth = { 'name': 'Earth',  'color': 'blue', 'orbit' = None }
Mars = { 'name': 'Mars',  'color': 'red', 'orbit' = None }

# Planets = [Earth, Mars, ...]

Earth['orbit']

# TODO: Planets as namedtuple

sun = Star('Sun')
Milky_way = Galaxy('Milky Way', 'spiral')
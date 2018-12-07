"""
	Defining classes for modeling Solar System.
"""
class Galaxy(object):
	"""A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas, 
	   dust, and dark matter.
	"""
	def __init__(self, arg):
		pass
		
class Planet(object):
	"""A planet is an astronomical body orbiting a star or stellar remnant that is massive enough 
	   to be rounded by its own gravity, is not massive enough to cause thermonuclear fusion, and 
	   has cleared its neighbouring region of planetesimals.
	"""
	def __init__(self, name, orbit, axial_tilt, rotation, color):
		self.name = name
		self.orbit = orbit
		self.axial_tilt = axial_tilt
		self.rotation = rotation
		self.color = color


class Star(object):
	"""A star is type of astronomical object consisting of a luminous spheroid of plasma
	   held together by its own gravity.
	"""
	def __init__(self, name, age=None, mass=None, temperature=None):
		self.name = name
		self.age = age
		self.mass = mass
		self.temperature = temperature

Planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune']
sun = Star('Sun')
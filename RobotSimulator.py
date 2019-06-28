from enum import Enum

class Direction(Enum):
	EAST = 0
	WEST = 1
	NORTH = 2
	SOUTH = 3


class RobotSimulator:
	def __init__(self, table_width = 5, table_length = 5):
		assert table_width > 0, "Table width should be a positive integer"
		assert table_length > 0, "Table length should be a positive integer"

		self.table_width = table_width
		self.table_length = table_length

		self.robot_x = None
		self.robot_y = None
		self.robot_direction = None


	def place(self, x, y, direction):
		self.robot_x = x
		self.robot_y = y
		self.robot_direction = direction


	def move(self):
		new_x, new_y = self.robot_x, self.robot_y
		if (self.robot_direction == Direction.EAST):
			new_x += 1
		elif (self.robot_direction == Direction.WEST):
			new_x -= 1
		elif (self.robot_direction == Direction.NORTH):
			new _y += 1
		else:
			new_y -= 1

		self.robot_x, self.robot_y = new_x, new_y


	def report(self):
		return '{},{},{}'.format(self.robot_x, self.robot_y, self.robot_direction.name)

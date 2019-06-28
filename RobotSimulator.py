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


	def is_valid(self, new_x, new_y):
		return 0 <= new_x < self.table_width and 0 <= new_y < self.table_length

	def place(self, x, y, direction):
		if self.is_valid(x, y):
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
			new_y += 1
		else:
			new_y -= 1

		if self.is_valid(new_x, new_y):
			self.robot_x, self.robot_y = new_x, new_y


	def report(self):
		print('{},{},{}'.format(self.robot_x, self.robot_y, self.robot_direction.name))


	def parse_command(self, line):
		params = line.strip().split()
		command = params[0]

		if command == 'PLACE':
			x, y, dir = params[1].split(',')
			self.place(int(x), int(y), Direction[dir.upper()])
		elif command == 'MOVE':
			self.move()
		elif command == 'REPORT':
			self.report()
		else:
			raise TypeError('Invalid command type.')


if __name__ == '__main__':
	r_sim = RobotSimulator()
	r_sim.place(0, 0, Direction.NORTH)
	r_sim.report()

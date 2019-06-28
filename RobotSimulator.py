from enum import Enum


class Direction(Enum):
	"""Enum to representation robot direction."""
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3


class RobotSimulator:
	def __init__(self, table_width=5, table_length=5):
		assert table_width > 0, "Table width should be a positive integer"
		assert table_length > 0, "Table length should be a positive integer"

		self.table_width = table_width
		self.table_length = table_length

		self.robot_x = None
		self.robot_y = None
		self.robot_direction = None

		self._is_valid_command = False

	def __eq__(self, other):
		# assuming we only have one robot.
		return isinstance(other, RobotSimulator) and \
		       all([getattr(self, attr) == getattr(other, attr) for attr in vars(self)])

	def is_valid_position(self, new_x, new_y):
		"""To validate if the new robot position is on the tabletop"""
		return 0 <= new_x < self.table_width and 0 <= new_y < self.table_length

	def place(self, x, y, direction):
		"""Function to validate the new position and place the robot"""
		if self.is_valid_position(x, y):
			self.robot_x = x
			self.robot_y = y
			self.robot_direction = direction
			self._is_valid_command = True

	def move(self, step=1):
		"""Function to validate the move the robot"""
		if not self._is_valid_command:
			return

		new_x, new_y = self.robot_x, self.robot_y
		if self.robot_direction == Direction.EAST:
			new_x += step
		elif self.robot_direction == Direction.WEST:
			new_x -= step
		elif self.robot_direction == Direction.NORTH:
			new_y += step
		else:
			new_y -= step

		if self.is_valid_position(new_x, new_y):
			self.robot_x, self.robot_y = new_x, new_y

	def report(self):
		"""Function to report the robot's position and direction"""
		if self._is_valid_command:
			return '{},{},{}'.format(self.robot_x, self.robot_y, self.robot_direction.name)

	def parse_command(self, line):
		"""Function to parse each line of command."""
		params = line.strip().split()
		command = params[0]

		if command == 'PLACE':
			try:
				x, y, dir = params[1].split(',')
				self.place(int(x), int(y), Direction[dir.upper()])
			except:
				pass
		elif command == 'MOVE':
			self.move()
		elif command == 'REPORT':
			output = self.report()
			if output:
				print(output)
		elif command == 'LEFT':
			if self._is_valid_command:
				self.robot_direction = Direction((self.robot_direction.value - 1) % 4)
		elif command == 'RIGHT':
			if self._is_valid_command:
				self.robot_direction = Direction((self.robot_direction.value + 1) % 4)
		else:
			pass

	def process_input(self, input):
		"""Function to process multi-line commands"""
		for command in input.strip().split('\n'):
			self.parse_command(command)

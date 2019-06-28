from enum import Enum


class Direction(Enum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3


class RobotSimulator:
	def __init__(self, table_width = 5, table_length = 5):
		assert table_width > 0, "Table width should be a positive integer"
		assert table_length > 0, "Table length should be a positive integer"

		self.table_width = table_width
		self.table_length = table_length

		self.robot_x = None
		self.robot_y = None
		self.robot_direction = None

		self._is_valid_command = False

	def __eq__(self, other):
		if isinstance(other, RobotSimulator):
			return self.table_width == other.table_length and \
			       self.table_length == other.table_length and \
			       self.robot_x == other.robot_x and \
			       self.robot_y == other.robot_y and \
			       self.robot_direction == other.robot_direction and \
			       self._is_valid_command == other._is_valid_command

		return False


	def is_valid_position(self, new_x, new_y):
		return 0 <= new_x < self.table_width and 0 <= new_y < self.table_length

	def place(self, x, y, direction):
		if self.is_valid_position(x, y):
			self.robot_x = x
			self.robot_y = y
			self.robot_direction = direction
			self._is_valid_command = True


	def move(self):
		if not self._is_valid_command:
			return

		new_x, new_y = self.robot_x, self.robot_y
		if (self.robot_direction == Direction.EAST):
			new_x += 1
		elif (self.robot_direction == Direction.WEST):
			new_x -= 1
		elif (self.robot_direction == Direction.NORTH):
			new_y += 1
		else:
			new_y -= 1

		if self.is_valid_position(new_x, new_y):
			self.robot_x, self.robot_y = new_x, new_y


	def report(self):
		if self._is_valid_command:
			return '{},{},{}'.format(self.robot_x, self.robot_y, self.robot_direction.name)


	def parse_command(self, line):
		params = line.strip().split()
		command = params[0]

		if command == 'PLACE':
			try:
				x, y, dir = params[1].split(',')
				self.place(int(x), int(y), Direction[dir.upper()])
			except Exception as e:
				pass
				# raise Exception('Error while parsing\n{}'.format(e))
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
			# raise TypeError('Invalid command {}'.format(line))


	def process_input(self, input):
		for command in input.strip().split('\n'):
			self.parse_command(command)




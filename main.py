#!/usr/bin/env python3

import sys
from RobotSimulator import Direction, RobotSimulator

if __name__ == '__main__':
	robo_sim = RobotSimulator()
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as in_file:
			input = in_file.read()
		robo_sim.process_input(input)
	else:
		while (True):
			command = input()
			if command == '':
				exit(0)
			robo_sim.parse_command(command)

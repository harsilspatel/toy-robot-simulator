#!/usr/bin/env python3

import sys
from RobotSimulator import Direction, RobotSimulator


def main():
	robo_sim = RobotSimulator()
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as in_file:
			input = in_file.read()
		robo_sim.process_input(input)
	else:
		command = input()
		robo_sim.parse_command(command)


if __name__ == '__main__':
	main()

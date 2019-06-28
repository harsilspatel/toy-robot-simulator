import pytest

from RobotSimulator import RobotSimulator


test1 = '''PLACE 0,0,NORTH
MOVE
REPORT'''

test2 = '''PLACE 0,0,NORTH
LEFT
REPORT'''

test3 = '''PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT'''
@pytest.mark.parametrize("input, expected", [(test1, '0,1,NORTH'), (test2, '0,0,WEST'), (test3, '3,3,NORTH')])
def test_given(input, expected, capfd):
	robot_simulator = RobotSimulator()
	robot_simulator.process_input(input)
	captured = capfd.readouterr()
	assert captured.out.strip() == expected



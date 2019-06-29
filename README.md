# toy-robot-simulator

[![Build Status](https://travis-ci.com/harsilspatel/toy-robot-simulator.svg?token=yLgWGY7CNm621frWpHzZ&branch=master)](https://travis-ci.com/harsilspatel/toy-robot-simulator)

> A library allows for a simulation of a toy robot moving on a 5 x 5 square tabletop.

#### Please visit the GitHub [repo](https://github.com/harsilspatel/toy-robot-simulator/) for the best experience.


## Development
### Testing
This project uses pytest for testing. 
Visit https://docs.pytest.org/en/latest/ to know more.

### Continuous Integration
Travis CI is employed to test the software updates. Please visit https://about.travis-ci.com/ for more information.

## Usage
1. Clone the repo.
2. Run `pip3 install requirements.txt` to install dependencies.
3. `chmod +x main.py` for execution permissions. (Or can be called using python3).
4. `./main.py {arguments}`

### CLI Arguments
`filename`</br> the file contatining robot commands. This argument can be omitted should the user wishes to enter commands from the CLI.

### Executing the tests
`pytest test.py --capture=fd` </br>
We run the pytest with the capture flag so as to capture and test the REPORT commands' outputs.

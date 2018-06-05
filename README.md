# Hell-Triangle-Challenge

- Introduction
	- This project is a solution to "Hell Triangle - Challenge" problem explained in .\doc\HellsTriangle.pdf
	- This project was designed using the python program language, their benefits to this project include:
		- Ease to create classes
		- The slice functionality turn on easy the manipulation of arrays
		- Ease to manipulate test cases using PyUnit framework

- Using the code
	- To use this solution is necessary import the content of it using the file "HellsTriangle.py" 
	- Create an object instance using "HellsTriangle" constructor 
	- To set up the inputs, using the constructor or calling the function "setTriangle", use the list of lists structure representing a triangle (more explainations in .\doc\HellsTriangle.pdf)
	- To get the max total result call the "getMaxTotal" function

- Test cases
	- The test cases were done using the PyUnit framework because of the facilities to generate simple case tests

	- Add
		- To add more test cases is necessary define:
			- Name of the test case, always beginning with "test" string
			- The input of the test case
			- The right answer of that test case
			- Add a new test case using the previous definitions as exemplified in the file .\src\HellsTriangleTests.py
	- Run
		- To run the defined test cases just run the command line:
			"python3 HellTriangleTests.py"
		- To another versions of python with the library "unittest" available (python version > 2.1)
			"python HellTriangleTests.py"

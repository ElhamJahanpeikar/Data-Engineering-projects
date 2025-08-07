# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'add' function from the 'mymodulepractice' module.
from mymodulepractice import add

# Define a test case class for testing the 'add' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestAdd(unittest.TestCase): 

    # Define the first test method for the 'add' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'add(2,4)' returns 6.
        # This tests if the function correctly computes the addition of 2 and 4.
        self.assertEqual(add(2, 4),6) # test when 2 and 4 are given as input the output is 6.

        # Check that calling 'add(2.3,3.6)' returns 5.9.
        # This tests if the function correctly computes the addition of 2.3 and 3.6, verifying that it handles float inputs.
        self.assertEqual(add(2.3,3.6), 5.9)  # test when 2.3 and 3.6 are given as input the output is 5.9.

        # Check that calling 'add(2.3000,4.300)' returns 6.6.
        # This tests if the function correctly computes the addition of 2.3000 and 4.300, verifying that it handles float inputs.
        self.assertEqual(add(2.3000,4.300), 6.6)  # test when 2.3 and 3.6 are given as input the output is 5.9.
       
        # Check that calling 'add(-2,-2)' does not return 0.
        # This tests that the function's output is not 0, verifying that the addition of -2 and -2 should be -4.
        self.assertNotEqual(add(-2,-2), 0)  # test when -2 and -2 are given as input the output is not 0.


        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()

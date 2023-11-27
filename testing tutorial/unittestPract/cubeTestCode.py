#this is the test file     and run this file as (( py -m unittest cubeTestCode.py )) at terminal
# -m is for telling thet it should run as a module script at terminal
# OK -> all test case passes
# FAIL -> test did not pass and AssertionError is raised
# ERROR -> test raises an Exception 
# unittest.main(argv=[''],verbosity=0,exit=False) # for running our test code on jupiter



from volume_cub import *    #importing the volume function
import unittest             #importing the testing module of python

class TestCub(unittest.TestCase): # this class inherits from unittest.TestCase
    def test_volume(self):
        self.assertAlmostEqual(cub_vol(2),8)  #test cases  # OK
        self.assertAlmostEqual(cub_vol(1),1)  #test cases  # OK
        self.assertAlmostEqual(cub_vol(0),0)  #test cases  # OK
        self.assertAlmostEqual(cub_vol(5.5),166.375)  #test cases  # OK

       # self.assertAlmostEqual(cub_vol(0),1)  # FAIL test cases  # FAIL
       # self.assertAlmostEqual(cub_vol(5.5),166)  # FAIL test cases  # FAIL

       # self.assertAlmostEqual(cub_vol('hello'),1)  # FAIL test cases  # FAIL cause we have done the type checking at our code and gives the type error 

    def test_input_val(self):   #This function checks that the main function is not raising any type of type error |||  if any type checking not there in my code it will give TypeError not Raised error. else everything gonna be OK
        self.assertRaises(TypeError,cub_vol,True)
# need to create 2 file 1 for the main code and 2nd for creating unit test

#this is importable fole for testing the unite test to test file

def cub_vol(l):
    if type(l) not in [int,float]:
        raise TypeError("the length should be a valid int or float ")     # for raising the type error at the main function 
    return(l**3)

#writing a function to calculate cuboid volume-


def cub_vol(lenth):
    return (lenth*lenth*lenth)

length=[2,3,4.4,2j,'two']

for i in range(len(length)):
    print("volume of the cuboide are :- ",cub_vol(i))
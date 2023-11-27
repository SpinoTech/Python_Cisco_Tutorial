#optional static typing using mypy module
#-> catch potential bugs , improve maintainability

#mypy -> is a third party library brings optional static typing allows #to annonate the code 

#--type hints , provide info about type module

#-> if no error in code mypy will give successfully massege but if error then give some errors 
# run  (( python -m mypy area.py  )) to run at terminal




def calc_area(length:float,width:float) -> float :
    return length*width

length=5.5
width=3.8

area=calc_area(length,width)
print(area)
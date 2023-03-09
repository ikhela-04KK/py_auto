from contextlib import contextmanager

# un gc permet d'allouer des ressiurces lors de l'execution d'un programme python 
@contextmanager
def this_func(fname, method):
    print("This is the implicit ENTRER block")
    with open(fname, method) as my_file:
        yield my_file
        print("This is the implicit EXIT block")
    
with this_func("this_file.txt", 'w')  as example:
    print("I'm in With block ") 









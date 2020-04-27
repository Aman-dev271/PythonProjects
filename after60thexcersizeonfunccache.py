import time
from functools import lru_cache
no_of_input_for_maxsize_of_chache_function = int(input("Enter the number for cache function"))
@lru_cache(maxsize= no_of_input_for_maxsize_of_chache_function)
def make_string_to_split(string):
    n1 = string.split(",")[0]
    n2 = string.split(",")[1]
    n3 = " "
    print(f"your F_name is: {n1}")
    print(f"your L_name is :{n2}")
    print(f"Plese wait for {no_of_input_for_maxsize_of_chache_function} seconds server works backend...........")
    time.sleep(no_of_input_for_maxsize_of_chache_function)
    print(f"your full name is {n1+n3+n2}")
make_string_to_split("Amandeep,Singh")
intput_your_fname_and_lname = input("Enter the name like:-F_name,L_name plese diffrentiate your f ans lastname with the comma")
time.sleep(no_of_input_for_maxsize_of_chache_function)
print(f"now does not take{no_of_input_for_maxsize_of_chache_function}  seconds to output.............. ")
make_string_to_split(intput_your_fname_and_lname)

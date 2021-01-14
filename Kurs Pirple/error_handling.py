# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 07:05:22 2021

@author: schomej
"""
keyWord = "Hello"
try:
    print(int(keyWord))
    
except Exception as error:
     print(error)
    
print("Past exception")


#another case
keyWord = "Hello"
try:
    print(int(keyWord))
    
except ValueError:
     print("got a ValueError")
    
except:
    print("Other type of exception")
    
finally:
    print("Finally") #it will alwlays be executed
    
    
#another case - raise your own error
keyWord = "Hello"
try:
    raise NameError("My own error")
    
except ValueError:
    print("got a ValueError")
except Exception as myError:
    print("Other kind of error")
    print(str(myError))


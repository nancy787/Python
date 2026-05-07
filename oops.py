class Student :
    def __init__(self, name) :
     self.name = name
    
st = Student('nan')
print(st.name)

# init_function or constructor it called when object initated
# def __init__(self) self poins to current obejct in class 
# Del Key used to delete object or properties itself

class User :
    def __init__(self, name) :
     self.name = name
    
st = User('nan')
print(st.name)
del st.name
# print(st.name)



# Access specirifer

class Account :
   def  __init__(self, acc_no, acc_key):
     self.acc_no = acc_no
     self. __acc_key = acc_key

ac = Account('233', 3343)
print(ac.__acc_key)
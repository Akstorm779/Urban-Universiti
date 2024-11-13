immutable_var= 1,2,'a','b'
print( immutable_var) # в кортеже можно изменять только списки (если содержится)
mutable_list= [1,2,'a','b']
mutable_list.append ('Modified')
print(mutable_list)
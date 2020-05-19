# challenge is to transform the string "Don’t panic!" into the string "on tap" using only the list methods

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
print("\n##################Operation begins ########################\n")

for i in range(4):
    plist.pop()
    print(plist)
print("######Sliced the Unnecessary object of the list ##########\n")

plist.pop(0)
print(plist)
print("######Removed the 0th index value (i.e, D) from the plist ###########\n")

plist.remove("'")
print(plist)
print("####### Removed object value \"\'\"  using remove method  ############\n")


plist.extend([plist.pop(),plist.pop()])
print(plist)
print("####### used extend method to switch the object value for last two indices ########")
print("####### we used extend method because insert can't be used for inserting at the end  ########\n")

plist.insert(2,plist.pop(3))
print(plist)
print("########### Swicthed the object value of indices that contained t and \' \' ##############")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)



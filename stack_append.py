# declaring a stack and appending
stack = [1, 2]
stack.append(5)
stack.append(4)
stack.append(3)
print(stack)

# stack of objects and fininding the size of stack
print(len(stack))

# appending the data to stack
stack_4 = []
stack_4.append(5)
stack_4.append(4)
stack_4.append(3)
print(stack_4)

# is not a stack
stack_not = []
print(not stack_not)

# appending vegetables to stack
stack_veg = []
stack_veg.append("Carrot")
stack_veg.append("Tomato")
stack_veg.append("Cabbage")
stack_veg.append("Spinach")
stack_veg.append("Potato")
stack_veg.append("Onion")
stack_veg.append("Pepper")
stack_veg.append("Broccoli")

print(stack_veg)
# removing an item from stack at index 1
print(stack_veg.pop(1))


# stack of fuitchat and appending the elements
fruit_chat = []
fruit_chat.append("Apple")
fruit_chat.append("Banana")
fruit_chat.append("Grapes")
fruit_chat.append("Mango")
fruit_chat.append("Orange")
fruit_chat.append("Pineapple")
fruit_chat.append("Strawberry")

print(fruit_chat)

# pop the 5th element
print("Popped Element:")
print(fruit_chat.pop(4))

print("After Popping:")
print(fruit_chat)

#sort the stack
fruit_chat.sort()
print("After Sorting:")
print(fruit_chat)

#reverse the stack
fruit_chat.reverse()
print("After Reversing:")
print(fruit_chat)



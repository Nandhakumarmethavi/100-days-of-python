#data types
#string integer float boolean

#string indexing (subscript)
print("hello"[0])

#integer
print(123+456)

#float
print(3+0.45)

#type conversion

num=len(input("whats ur name"))
new_num=str(num)
print("your name has "+new_num+"characters")

#all the data adding together should be of same data type

#data type checker
a=123
print(type(a))

#adding of number as string
print(str(80)+str(70))

#
two_digit_number=input("type any two digit number")
print(type(two_digit_number))
first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
result=int(first_digit)+int(second_digit)
print(result)

#
score=0
score+=1
print(score)
height=1

#f string
print(f"your score is {score},your height is{height}")
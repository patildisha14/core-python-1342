#check whether the number is even or odd
# a=int(input("Enter a number: "))
# if a%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")


#positive negative or zero
# a=int(input("Enter a number: "))
# if a>0:
#     print("the number is positive")
# elif a<0:
#     print("the number is negative")
# else:
#     print("the number is zero")

#for loop and while loop
# for i in range(5,0,-1):
#     print(i)


# fact=1
# n=4
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial of",n,"is",fact)

#prime number
# a=19
# while a>1:
#     for i in range(2,100):
#         if a%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
#     break


# for a in range(2, 101):
#     for i in range(2, a):
#         if a % i == 0:
#             break
#     else:
#         print(a)

# a=4
# square=a**2
# print(square)
# a=5 
# cube=a**3
# print(cube)


# a=123
# if str(a)==str(a)[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# a="disha"
# rev =""
# for i in a:
#     rev = i + rev
# print("Reverse =", rev)

# a=[12,23,42,5,56,7]
# for i in a:
#     if i%2==0:
#         print(i,"number is even")
#     else:
#         print(i,"number is odd")

# a=[13,24,22,3,23,2,13]
# print(a.count(13))

# a=[12,45,63,36]
# rev = []
# for i in a:
#     rev = [i] + rev
#     print(rev)

# a = [12, 31,37, 45, 36, 77, 88]
# for i in a:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

#print string
# a=[12,"disha","ram",34,45]
# for i in a:
#     if isinstance(i,str):
#         print(i)


#print int
# a=[12,32,"ab",243]
# for i in a:
#     if isinstance(i,int):
#         print(i)
    
#find min
# a=(12,3,43,443,56,)
# print(max(a))

#find sum
# a=(12,2,43,544,67)
# print(min(a))

#sum of tuple element
# a=(12,2,43,544,67)
# print(sum(a))

#length of tuple
# a=(1,54,676,88,23)
# count=0
# for i in a:
#     count=count+1
#     print("length:",count)
# print (sum(a))

#only even num
# a=(1,54,676,88,23)
# for i in a:
#     if i%2==0:
#         print(i)

#display values 
# a={
#     "name":"disha",
#     "age":20,
#     "city":"pune",
#     "marks":65
# }
# for i in a.values():
#     print(i)

#total of marks
# a={
#    1:{
#    "name":"disha",
#    "age":20,
#    "city":"pune",
#    "marks":65},
# 2:{
#    "name":"ram",
#    "age":20,
#    "city":"pune",
#    "marks":67},

# 3:{
#   "name":"sweta",
#    "age":21,
#    "city":"pune",
#    "marks":68
# }
# }
# total = 0
# for i in a:
#     total = total + a[i]["marks"]
# print("Total marks:", total)


#highest marks
a={
   1:{
   "name":"disha",
   "age":20,
   "city":"pune",
   "marks":65},
2:{
   "name":"ram",
   "age":20,
   "city":"pune",
   "marks":59},

3:{
  "name":"sweta",
   "age":21,
   "city":"pune",
   "marks":68
}
}
#student who scored above 60
for i in a:
    if a[i]["marks"]>60:
        print(i,a[i]["marks"])

#count nuber who passed
count=0
for i in a:
    if a[i]["marks"]>60:
        count=count+1
        print(count)

#highest marks
m=0
name=""
for i in a:
    if a[i]["marks"]>m:
     m=a[i]["marks"]
     name=a[i]["name"]
print(name,m)
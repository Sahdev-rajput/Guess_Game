import random
list1=[]
list2=[]
def number_of_digits(n,list):
    count=0
    while(n!=0):
        list.append(n%10)
        n=n//10
        count=count+1
    return count

def trywithMe(a,list):
 list.clear()
 result=0
 result=number_of_digits(a,list)
 while(result!=3):
    list.clear()
    print("You haven't entered a 3-digit number.Enter Again!")
    a=int(input("Enter the number Again: "))
    result=number_of_digits(a,list)


random_number=random.randint(100,999)
print("Let's play a Guess Game . You Have to think of a Number . I will tell u three possibility : Match , Close or Correct: ")
a=int(input("Enter the number: "))


number_of_digits(random_number,list2)

while(a!=random_number):
   trywithMe(a,list1)
   same=0
   if list1[0] in list2:
      same=same+1
   if list1[1] in list2:
      same=same+1
   if list1[2] in list2:
      same=same+1
   if(same==1):
      print("Match")
      a=int(input("Enter the number Again: "))
   elif(same==2):
      print("Close")
      a=int(input("Enter the number Again: "))
   elif(same==0):
      print("Try Again")
      a=int(input("Enter the number Again: "))
   else:
      print("Perfect Match")
      a=int(input("Enter the number Again: "))


print("Oh! Yes You Win Finally")





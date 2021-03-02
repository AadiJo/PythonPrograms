def base_2(num):
   i = 0
   while 2**i <= num:
       answer = 2**i
       i += 1
   answer_lst = [0] * (i-1)
   answer_lst[0] = 1
   remainder = num - answer
   while remainder != 0:
       remainder, answer_lst = base_2_loop(remainder, answer_lst)
   print(answer_lst)


def base_2_loop(num, answer_lst):
   i = 0
   if num == 1:
       answer = 1
       i += 2

   while 2 ** i <= num:
       answer = 2 ** i
       i += 1

   answer_lst[-(i-1)] = 1
   baseNumber = str(answer_lst)
   return (num - answer), answer_lst
   #return baseNumber


print("This is the BASE TWO CALCULATOR")
print("Enter the the number that's 'bout to be base two!")
number = int(input("ENTER YOUR NUMBER: "))
base_2(number)

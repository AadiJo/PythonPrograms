print('Celcius to Fahrenheit!')
num = float(input('Type a number: '))
def cal(num):
  ans = (1.8 * num) + 32
  print(ans)

cal(num)

print('Fahrenheit to Celcius')
num1 = float(input('Type a number: '))

def cal2(num):
  ans = (num - 32) / 1.8
  print(ans)

cal2(num1)
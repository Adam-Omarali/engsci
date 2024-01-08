def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  return a + b if a != b else 2 * (a + b)

def diff21(n):
  return abs(21 - n) if n <= 21 else 2 * abs(21 - n)

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  
  return a < 0  and b > 0 or b < 0 and a > 0

def not_string(str):
  if len(str) >= 3:
    return "not " + str if str[0:3] != 'not' else str
  
  return "not " + str

def missing_char(str, n):
  if n < len(str) - 1:
    return str[:n] + str[n+1:]
  
  return str[:n]

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    temp = str[0]
    return str[-1] + str[1:-1] + temp
  

def front3(str):
  if len(str) < 3:
    return str * 3
  
  return str[0:3] * 3

def string_times(str, n):
  return str * n

def front_times(str, n):
  if len(str) < 3:
    return str * n
  
  return str[0:3] * n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  ret = ''
  for i in range(1, len(str) + 1):
    ret += str[0:i]
    
  return ret

def last2(str):
  if len(str) <= 2:
    return 0
    
  count = 0  
  sub = str[-2:]
  for i in range(0, len(str) - 2):
    if str[i:i+2] == sub:
      count += 1
      
  return count

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  for i in range(min(4, len(nums))):
    if nums[i] == 9:
      return True
      
  return False

def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i: i + 3] == [1, 2, 3]:
      return True
      
  return False

def string_match(a, b):
  count = 0
  
  for i in range(min(len(a), len(b) - 1)):
    if a[i: i+2] == b[i: i + 2]:
      count += 1
      
  return count

def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  ret = 0
  for i in nums:
    ret += i

  return ret
    
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  return [max(nums[0], nums[2])] * 3

def sum2(nums):
  if len(nums) > 0:
    if len(nums) > 1:
      return nums[0] + nums[1]
    return nums[0]
      
  return 0

def middle_way(a, b):
  return [a[len(a) // 2], b[len(b) // 2]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  return 2 in nums or 3 in nums

def cigar_party(cigars, is_weekend):
  return 40 <= cigars if is_weekend else 40 <= cigars <= 60

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8  or date >= 8:
    return 2
    
  return 1

def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  
  return 60 <= temp <= 90

def caught_speeding(speed, is_birthday):
  if(speed <= 60):
    return 0
    
  if is_birthday:
    if 66 >= speed:
      return 0
    if 86 >= speed:
      return 1
    
  if 61 <= speed <= 80:
    return 0 if is_birthday and speed <= 85 else 1

  return 2

def sorta_sum(a, b):
  if 10 <= a+b <= 19:
    return 20
    
  return a + b

def alarm_clock(day, vacation):
  if vacation:
    if 1 <= day <= 5:
      return "10:00"
    else:
      return "off"
      
  if 1 <= day <= 5:
    return "7:00"
    
  return "10:00"

def love6(a, b):
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
    
  return 1 <= n <= 10

def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
      
  return count

def big_diff(nums):
  low = 1000000
  high = 0
  for num in nums:
    if num > high:
      high = num
    
    if num < low:
      low = num
      
  return high - low
  
def centered_average(nums):
  low = min(nums)
  high = max(nums)
  
  avg = 0
  
  for num in nums:
    if num == low:
      low = None
    elif num == high:
      high = None
    else:
      avg += num
    
  return avg / (len(nums)-2)

def sum13(nums):
  no_add = False
  ret = 0
  for num in nums:
    if not no_add and num != 13:
      ret += num
    no_add = num == 13
      
  return ret

def sum67(nums):
  no_add = False
  count = 0
  for num in nums:
    if num == 6:
      no_add = True
      
    if not no_add:
      count += num
      
    if num == 7:
      no_add = False
      
  return count

def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1] == 2:
      return True
      
  return False

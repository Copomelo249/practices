def falling(n, k):
    a=1
    for i in range(n-k+1,n+1):
        a=a*i
    return a
print(falling(6,3))

def divisible_by_k(n, k):
    count=0
    for i in range(1,n+1):
        if i % k == 0:
            print(i)
            count+=1
    return count
a = divisible_by_k(6, 7)
print(a)
    
def sum_digits(y):
    digits = [int(a) for a in y]
    total = sum(digits)
    return total

y = "545"
result = sum_digits(y)
print(result)
    
def double_eights(n):
    # 将整数转换为字符串
    str_n = str(n)
# 检查是否包含连续的两个 '8'
    return '88' in str_n
print(double_eights(8))
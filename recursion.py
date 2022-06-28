def factorial(num):
    if num == 1:
        return 1
    else:
        ans = num * factorial(num - 1)
        print(ans)
        return ans

input = input("enter number: ")
factorial(int(input))
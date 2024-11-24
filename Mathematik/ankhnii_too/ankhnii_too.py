def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** (1/2))+1):
            if n % i == 0:
                return False
        return True

def main():
    n = int(input())
    print(prime(n))
if __name__=="__main__":
    main()





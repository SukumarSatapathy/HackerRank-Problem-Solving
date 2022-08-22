def separateNumbers(s):
    
    mid = len(s)//2
    res = 'NO'
    for i in range(mid):
        start_int = int(s[:i+1])
        start_str = s[:i+1]
        start_num = start_int
        while(len(start_str) < len(s)):
            start_int += 1
            start_str += str(start_int)
        if s == start_str:
            res = f'''YES {start_num}'''
            break
    print(res)
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

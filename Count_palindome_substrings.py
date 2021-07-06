def countPalindromes(s):
    dp = [[True for i in range(5001)]
          for j in range(5001)]
    
    n = len(s)
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                dp[i][i+k] = True
            if k == 1:
                if s[i] == s[i+1]:
                    dp[i][i+k] = True
                else:
                    dp[i][i+k] = False
            else:
                if s[i] == s[i+k] and dp[i+1][i+k-1] == True:
                    dp[i][i+k] = True
                else:
                    dp[i][i+k] = False
                    
    for i in range(n):
        for j in range(n):
            print(dp[i][j],end= ' ')
        print()   
                 
    count = 0
    for i in range(n):
        for j in range(i , n):
            if dp[i][j]:
                count += 1                
    return count        
    
  
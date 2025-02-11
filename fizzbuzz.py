from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1): 
            ans = ""  

            if i % 3 == 0: 
                ans += "Fizz"
            if i % 5 == 0:  
                ans += "Buzz"
            
            if ans == "":  
                ans = str(i)

            output.append(ans)  
        
        return output

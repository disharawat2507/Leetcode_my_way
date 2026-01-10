# LeetCode #992: Subarrays with K Different Integers
# Approach : we will find count of subarrays less than k and less than k -1 . then subsctracting the count of these 2 , will give us the actual count
# Time Complexity : O(2n)

def main(nums,k):
    def diffsubarray(k):
        l =0
        cmap ={}
        count = 0
        for r in range(len(nums)):
            cmap[nums[r]] = cmap.get(nums[r], 0) +1
            while len(cmap.keys()) > k:
                cmap[nums[l]] -=1
                if cmap[nums[l]] == 0:
                    del cmap[nums[l]]
                l +=1
            count += r-l +1  
        return count   
    return  diffsubarray(k) -diffsubarray(k-1)        

nums =[2,1,1,1,3,4,3,2]
k = 3
print(main(nums,k)) 

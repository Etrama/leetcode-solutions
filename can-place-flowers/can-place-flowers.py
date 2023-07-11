class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count_added = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0) or flowerbed[i-1] == 0:
                    left_empty = True
                else:
                    left_empty = False
                if (i == len(flowerbed)-1) or flowerbed[i+1] == 0:
                    right_empty = True
                else:
                    right_empty = False
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count_added +=1
        return count_added>=n
            
        
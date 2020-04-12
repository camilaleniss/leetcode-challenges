def lastStoneWeight(stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for index in range(0, len(stones)):
            if len(stones)<=1:
                break

            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()

            if (stone2!=stone1):
                stone2 = stone1 - stone2
                stones.append(stone2)
        
        if len(stones)==1:
            return stones[0]
        else:
            return 0

stones = [1000,999,987]
print(lastStoneWeight(stones))
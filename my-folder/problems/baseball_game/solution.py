class Solution:
    def calPoints(self, operations: List[str]) -> int:
        dummy_array = []
        for i in operations:
            if i == 'C':
                dummy_array.pop()
            elif i == "D":
               dou = int(dummy_array[-1])
               dummy_array.append(2*dou)
            elif i == "+":
                score1 = int(dummy_array[-1])
                score2 = int(dummy_array[-2])
                dummy_array.append(score1+score2)
            else:
                dummy_array.append(int(i))
        return sum(dummy_array)
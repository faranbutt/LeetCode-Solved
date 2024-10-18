class Solution(object):
    def mySqrt(self,x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x

        while left <= right:
            M = left + (right - left) // 2
            print(M)
            m_squared = M * M
            if m_squared == x:
                return M
            elif m_squared < x:
                left = M + 1
            else:
                right = M - 1
        return right
        
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        answer = [0] * ( n + 2)
        for first,last, seats in bookings:
         answer[first]+= seats
         answer[last +1]-= seats
        for i in range(1,n+1):
         answer[i] += answer[i - 1]

        return  answer[1:n+1]

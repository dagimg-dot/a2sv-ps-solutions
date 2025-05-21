class MyCalendar:

    def __init__(self):
        self.calendar = []        

    def book(self, startTime: int, endTime: int) -> bool:
        right = len(self.calendar)
        if right == 0:
            self.calendar.append((startTime, endTime))
            return True

        left = 0
        while left < right:
            mid = int(left + (right - left)/2)
            if self.calendar[mid][1] <= startTime:
                left = mid + 1
            else:
                right = mid

        if left == len(self.calendar):
            self.calendar.append((startTime, endTime))
            return True
                
        if self.calendar[left][0] >= endTime:
            self.calendar.insert(left, (startTime, endTime))
            return True
            
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
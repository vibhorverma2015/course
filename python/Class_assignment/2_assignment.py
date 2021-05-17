class Time:
    def __init__(self, time):
        self.time = 0
        self.total_time = 0

    def addtime(self):

        total_hours = (hour1+hour2*60)
        total_minutes = (minutes1+minutes2*6)
        total_time = (total_hours+total_minutes/60)
        return(total_time)


print("entre first time")
hour1 = int(input())
minutes1 = int(input())
print("entre second time")
hour2 = int(input())
minutes2 = int(input())

class Soldier:
    def __init__(self, name , id , qualification, isAssigned):
        self.name = name
        self.id = id
        self.qualification = qualification
        self.isAssigned = isAssigned

class Tasks:
    def __init__(self, name , amountQualification, soldiers,duration):
        self.name = name 
        self.amountQualification = amountQualification
        self.soldiers = soldiers
        self.duration = duration

class Shift:
    def __init__(self, nameTask , startTime, endTime,soldiers,assignments):
        self.nameTask = nameTask
        self.startTime = startTime
        self.endTime = endTime
        self.soldiers = soldiers
        self.assignments = assignments


class Assignments:
    def __init__(self, assignments):
        self.assignments = assignments

    def assign(self, soldiers, tasks):
        AllShifts = []
        for task in tasks:
            shifts = []
            # TODO - if task.duration%24 != 0 or task.duration>24 --> error
            for i in range(0,23,task.duration):
                shifts.append(Shift(task.name,i,i+task.duration,[],False))

            for shift in shifts:
                if not shift.assignments:
                    qualification = task.amountQualification.copy()
                    for soldier in soldiers:
                        if soldier.qualification in task.amountQualification and qualification[soldier.qualification] > 0 and not soldier.isAssigned:
                            qualification[soldier.qualification] -= 1
                            shift.soldiers.append("name "+soldier.name + " id:" + str(soldier.id))
                            soldier.isAssigned = True
                            self.assignments[task.name] = True
                    shift.assignments = True       
            AllShifts.append(shifts)            
                
        return AllShifts
            # for in range(task.duration)



# main
if __name__ == "__main__":
    soldiers = [Soldier("A", 1, "hovesh", False),Soldier("k", 9, "normal", False) ,Soldier("B", 2, "normal", False), Soldier("C", 3, "mc", False), Soldier("D", 4, "hovesh", False), Soldier("E", 5, "normal", False), Soldier("F", 6, "normal", False)]
    tasks = [Tasks("shinG", {"normal": 1}, [],12), Tasks("siyur", {"hovesh": 2, "normal": 2, "mc": 1}, [],8)]
    assignments = Assignments({"shinG": False, "siyur": False})
    shifts = assignments.assign(soldiers, tasks)
    for shift in shifts:
        for i in shift:
            print("task name: ",i.nameTask,", soldiers in this shift = ",i.soldiers,", start time: ",i.startTime, "end time of shift: " ,i.endTime)
    print(assignments.assignments)






    


        




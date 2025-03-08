#req: last canceled var (for rescedule)
#			stack to store events
# 		pop() to get top element to store in last canceled
# 		reschedule: add last canceled element to stack
#     cancel:to cancel the most recently added (top) event

def manage_stage_changes(changes):
    schedule_stack = []
    canceled_stack = []

    for change in changes:
        if (change == "Cancel"):
            canceled = schedule_stack.pop()
            canceled_stack.append(canceled)
        elif (change == "Reschedule"):
            cancel = canceled_stack.pop()
            schedule_stack.append(cancel)
        else:
            event = change.split(" ", 1)[1]
            schedule_stack.append(event)
    
    return schedule_stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))
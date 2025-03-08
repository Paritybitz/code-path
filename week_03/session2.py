#req: last canceled var (for rescedule)
#			stack to store events
# 		pop() to get top element to store in last canceled
# 		reschedule: add last canceled element to stack
#     cancel:to cancel the most recently added (top) event

def manage_stage_changes(changes):
    schedule_stack = []
    canceled_stack = []

    for change in changes:
        if (changes[change] == "Cancel"):
            canceled = schedule_stack.pop()
            canceled_stack.add(canceled)
        elif (changes[change] == "Reschedule"):
            cancel = canceled_stack.pop()
            schedule_stack.add(cancel)
        else:
            event=changes[change][9]
            schedule_stack.add(event)
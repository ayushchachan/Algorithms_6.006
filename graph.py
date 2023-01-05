# class Node:
#     def __init__(self, val):
#         self.val  = val
#         self.next = None



class Solution:
    
    def findAllPeople(self, n, meetings, firstPerson) :
        tasks = self.get_sorted_tasks(meetings)
        
        
    
    def get_sorted_tasks(self, meetings):
        tasks = {}

        for u, v, t in meetings:
            if t in meetings:
                tasks[t].append((u, v))
            else:
                tasks[t] = [(u, v)]
        
        return tasks
    
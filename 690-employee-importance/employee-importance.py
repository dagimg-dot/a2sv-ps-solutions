"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        employee_dict = dict()
        queue = [id]
        importance_sum = 0

        for employee in employees:
            employee_dict[employee.id] = employee

        while queue:
            employee_index = queue.pop(0)
            employee = employee_dict[employee_index]
            importance_sum += employee.importance
            queue.extend(employee.subordinates)

        return importance_sum

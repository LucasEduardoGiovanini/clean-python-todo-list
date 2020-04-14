import unittest
from domain import use_cases
from domain.entities.todolist import TodoList
from domain.entities.task import Task


class Tests(unittest.TestCase):

    def test_create_list(self):
        testlist = TodoList("works of day")

    def test_add_task_to_list(self):
        testlist1 = TodoList("market")
        task1 = Task("banana", "test banana", True, 1)

        response = use_cases.add_task(testlist1, task1)
        self.assertEqual(response, task1)

    def test_remove_task_to_list(self):
        testlist2 = TodoList("market")
        task4 = Task("banana", " test banana", True, 1)
        task5 = Task("apple", "test apple", False, 2)
        task6 = Task("rice", "test rice", False, 3)

        testlist2.addTask(task4)
        testlist2.addTask(task5)
        testlist2.addTask(task6)
        response = use_cases.add_task(testlist2, task5)
        self.assertEqual(response, task5)

    def test_complete_task(self):
        testlist3 = TodoList("market")
        task7 = Task("banana", " test banana", True, 1)
        task8 = Task("apple", "test apple", False, 2)
        task9 = Task("rice", "test rice", False, 3)

        testlist3.addTask(task7)
        testlist3.addTask(task8)
        testlist3.addTask(task9)

        response = use_cases.complete_task(testlist3, task8)
        self.assertEqual(response, task8)

    def test_undo_task(self):
        testlist4 = TodoList("market")
        task10 = Task("banana", " test banana", True, 1)
        task11 = Task("apple", "test apple", False, 2)
        task12 = Task("rice", "test rice", False, 3)

        testlist4.addTask(task10)
        testlist4.addTask(task11)
        testlist4.addTask(task12)

        response = use_cases.undo_task(testlist4, task10)
        self.assertEqual(response, task10)

    def test_order_task(self):
        testlist5 = TodoList("market")
        task13 = Task("banana", " test banana", True, 1)
        task14 = Task("apple", "test apple", False, 2)
        task15 = Task("rice", "test rice", False, 3)

        testlist5.addTask(task13)
        testlist5.addTask(task14)
        testlist5.addTask(task15)

        response = use_cases.order_task(testlist5, task15, task13)
        self.assertEqual(response, True)

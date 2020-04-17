import unittest

from domain.entities.todolist import TodoList
from domain.entities.task import Task
from domain.exception.custom_exception import todoListError


class Tests(unittest.TestCase):

    def test_create_list(self):
        response = TodoList("works of day")
        self.assertEqual(response.name, ("works of day"))

    def test_add_task_to_list(self):
        testlist1 = TodoList("market")
        task1 = Task("banana", "test banana", True, 1)

        response = testlist1.addTask(task1)
        index = response.index(task1)
        self.assertEqual(response[index], task1)

    def test_remove_task_to_list(self):
        testlist2 = TodoList("market")
        task4 = Task("apple", "test apple", False, 2)

        testlist2.addTask(task4)

        response = testlist2.removeTask(task4)
        self.assertEqual(response, True)

    def test_remove_task_to_not_exist_in_list(self):
        testlist2false = TodoList("market")
        task5 = Task("apple", "test apple", False, 2)
        task6 = Task("krab", "test krab", False, 2)
        testlist2false.addTask(task6)

        with self.assertRaises(todoListError):
            testlist2false.removeTask(task5)

    def test_complete_task_not_completed(self):
        task8 = Task("apple", "test apple", False, 2)
        task8.complete()
        self.assertEqual(task8.completed, True)

    def test_complete_task_already_completed(self):
        task8 = Task("apple", "test apple", True, 2)
        task8.complete()
        self.assertEqual(task8.completed, True)

    def test_undo_task_already_completed(self):
        task11 = Task("apple", "test apple", True, 2)

        response = task11.undo()
        self.assertEqual(response, False)

    def test_undo_task_not_completed(self):
        task11 = Task("apple", "test apple", False, 2)

        response = task11.undo()
        self.assertEqual(response, False)

    def test_order_task(self):
        testlist5 = TodoList("market")
        task13 = Task("banana", " test banana", True, 1)
        task14 = Task("apple", "test apple", False, 2)
        task15 = Task("rice", "test rice", False, 3)

        testlist5.addTask(task13)
        testlist5.addTask(task14)
        testlist5.addTask(task15)

        response = testlist5.orderTasks(task15, 0)
        self.assertEqual(response[0], task15)

    def test_order_task_with_task_not_existent_in_list(self):
        testlist6 = TodoList("market")
        task16 = Task("banana", " test banana", True, 1)
        task17 = Task("apple", "test apple", False, 2)
        task18 = Task("rice", "test rice", False, 3)

        task19 = Task("test", "big test", True, 1)

        testlist6.addTask(task16)
        testlist6.addTask(task17)
        testlist6.addTask(task18)

        with self.assertRaises(todoListError):
            testlist6.orderTasks(task19, 0)

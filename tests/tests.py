import unittest

from domain.entities.todolist import TodoList
from domain.entities.task import Task
from domain.exception.custom_exception import todoListError


class Tests(unittest.TestCase):

    def test_create_list(self):
        response = TodoList("works of day")
        self.assertEqual(response.name, "works of day")

    def test_edit_list_name(self):
        testlist0 = TodoList("market")
        testlist0.edit_list_name("testing")
        self.assertEqual(testlist0.name, "testing")

    def test_add_task_to_list(self):
        testlist1 = TodoList("market")
        response = testlist1.create_task("banana", "test banana", True, 1)
        self.assertEqual(response, testlist1.tasks[0])

    def test_remove_task_to_list(self):
        testlist2 = TodoList("market")
        created_task = testlist2.create_task("apple", "test apple", False, 2)

        response = testlist2.remove_task(created_task)
        self.assertEqual(response, True)

    def test_remove_task_to_not_exist_in_list(self):
        testlist2false = TodoList("market")
        testlist3false = TodoList("gym")
        response = testlist3false.create_task("apple", "test apple", False, 2)

        with self.assertRaises(todoListError):
            testlist2false.remove_task(response)

    def test_complete_task_not_completed(self):
        testlist3 = TodoList("market")
        task = testlist3.create_task("apple", "test apple", False, 2)

        response = testlist3.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_complete_task_already_completed(self):
        testlist4 = TodoList("market")
        task = testlist4.create_task("apple", "test apple", True, 2)

        response = testlist4.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_undo_task_already_completed(self):
        testlist5 = TodoList("market")
        task = testlist5.create_task("apple", "test apple", True, 2)

        response = testlist5.undo_task(task)
        self.assertEqual(response.completed, False)

    def test_undo_task_not_completed(self):
        testlist6 = TodoList("market")
        task11 = Task("apple", "test apple", False, 2)
        testlist6.add_task(task11)
        response = testlist6.undo_task(task11)
        self.assertEqual(response.completed, False)

    def test_order_task(self):
        testlist7 = TodoList("market")
        task13 = Task("banana", " test banana", True, 1)
        task14 = Task("apple", "test apple", False, 2)
        task15 = Task("rice", "test rice", False, 3)

        testlist7.add_task(task13)
        testlist7.add_task(task14)
        testlist7.add_task(task15)

        response = testlist7.order_task(task15, 0)
        self.assertEqual(response[0], task15)

    def test_order_task_with_task_not_existent_in_list(self):
        testlist6 = TodoList("market")
        task16 = Task("banana", " test banana", True, 1)
        task17 = Task("apple", "test apple", False, 2)
        task18 = Task("rice", "test rice", False, 3)
        task19 = Task("test", "big test", True, 1)

        testlist6.add_task(task16)
        testlist6.add_task(task17)
        testlist6.add_task(task18)

        with self.assertRaises(todoListError):
            testlist6.order_task(task19, 0)

    def test_edit_task(self):
        testlist7 = TodoList("market")
        task19 = Task("banana", " test banana", True, 1)
        testlist7.add_task(task19)
        testlist7.edit_task(task19, name="avocado")
        self.assertEqual(task19.name, "avocado")

    def test_edit_task_not_existent_in_List(self):
        testlist8 = TodoList("market")
        task20 = Task("banana", " test banana", True, 1)

        with self.assertRaises(todoListError):
            testlist8.edit_task(task20, name="avocado")

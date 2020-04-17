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
        task1 = testlist7.create_task("banana", " test banana", True, 1)
        task2 = testlist7.create_task("apple", "test apple", False, 2)
        task3 = testlist7.create_task("rice", "test rice", False, 3)

        response = testlist7.order_task(task3, 0)
        self.assertEqual(response[0], task3)

    def test_order_task_with_task_not_existent_in_list(self):
        testlist8 = TodoList("market")
        testlist9 = TodoList("gym")
        task1 = testlist8.create_task("banana", " test banana", True, 1)
        task2 = testlist8.create_task("apple", "test apple", False, 2)
        task3 = testlist8.create_task("rice", "test rice", False, 3)
        task4 = testlist9.create_task("run", "run 50 minutes", True, 1)

        with self.assertRaises(todoListError):
            testlist8.order_task(task4, 0)

    def test_edit_task(self):
        testlist10 = TodoList("market")
        task1 = testlist10.create_task("banana", " test banana", True, 1)
        testlist10.edit_task(task1, name="avocado")
        self.assertEqual(task1.name, "avocado")

    def test_edit_task_not_existent_in_List(self):
        testlist11 = TodoList("market")
        testlist12 = TodoList("Gym")
        task = testlist11.create_task("banana", " test banana", True, 1)

        with self.assertRaises(todoListError):
            testlist12.edit_task(task, name="avocado")

    def test_order_tasks_by_priority(self):
        testlist13 = TodoList("market")
        task1 = testlist13.create_task("banana", " test banana", True, 3)
        task2 = testlist13.create_task("apple", "test apple", False, 1)
        task3 = testlist13.create_task("rice", "test rice", False, 2)
        expected_result = [task2, task3, task1]

        response = testlist13.order_task_priority()

        self.assertEqual(response,expected_result)

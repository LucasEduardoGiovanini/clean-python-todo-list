import unittest
import uuid
from domain.entities.todolist import TodoList
from domain.entities.task import Task
from domain.exception.custom_exception import TodoListError
from repositories import TodoListRepository,UserRepository

class Tests(unittest.TestCase):

    def test_create_list(self):
        response = TodoList(str(uuid.uuid4()), "works of day")
        self.assertEqual(response.todo_name, "works of day")

    def test_edit_list_name(self):
        testlist0 = TodoList(str(uuid.uuid4()), "market")
        testlist0.edit_list_name("testing")
        self.assertEqual(testlist0.todo_name, "testing")

    def test_add_task_to_list(self):
        testlist1 = TodoList(str(uuid.uuid4()), "market")
        response = testlist1.create_task(str(uuid.uuid4()), "banana", "test banana", True, 1)
        self.assertEqual(response, testlist1.tasks[0])

    def test_remove_task_to_list(self):
        testlist2 = TodoList(str(uuid.uuid4()), "market")
        created_task = testlist2.create_task(str(uuid.uuid4()), "apple", "test apple", False, 2)

        response = testlist2.remove_task(created_task)
        self.assertEqual(response, True)

    def test_remove_task_to_not_exist_in_list(self):
        testlist2false = TodoList(str(uuid.uuid4()), "market")
        testlist3false = TodoList(str(uuid.uuid4()), "gym")
        response = testlist3false.create_task(str(uuid.uuid4()), "apple", "test apple", False, 2)

        with self.assertRaises(TodoListError):
            testlist2false.remove_task(response)

    def test_complete_task_not_completed(self):
        testlist3 = TodoList(str(uuid.uuid4()), "market")
        task = testlist3.create_task(str(uuid.uuid4()), "apple", "test apple", False, 2)

        response = testlist3.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_complete_task_already_completed(self):
        testlist4 = TodoList(str(uuid.uuid4()), "market")
        task = testlist4.create_task(str(uuid.uuid4()), "apple", "test apple", True, 2)

        response = testlist4.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_undo_task_already_completed(self):
        testlist5 = TodoList(str(uuid.uuid4()), "market")
        task = testlist5.create_task(str(uuid.uuid4()), "apple", "test apple", True, 2)

        response = testlist5.undo_task(task)
        self.assertEqual(response.completed, False)

    def test_undo_task_not_completed(self):
        testlist6 = TodoList(str(uuid.uuid4()), "market")
        task11 = Task(str(uuid.uuid4()), "apple", "test apple", False, 2)
        testlist6.add_task(task11)
        response = testlist6.undo_task(task11)
        self.assertEqual(response.completed, False)

    def test_order_task(self):
        testlist7 = TodoList(str(uuid.uuid4()), "market")
        task1 = testlist7.create_task(str(uuid.uuid4()), "banana", " test banana", True, 1)
        task2 = testlist7.create_task(str(uuid.uuid4()), "apple", "test apple", False, 2)
        task3 = testlist7.create_task(str(uuid.uuid4()), "rice", "test rice", False, 3)

        response = testlist7.order_task(task3, 0)
        self.assertEqual(response[0], task3)

    def test_order_task_with_task_not_existent_in_list(self):
        testlist8 = TodoList(str(uuid.uuid4()), "market")
        testlist9 = TodoList(str(uuid.uuid4()), "gym")
        task2 = testlist8.create_task(str(uuid.uuid4()), "apple", "test apple", False, 2)
        task3 = testlist8.create_task(str(uuid.uuid4()), "rice", "test rice", False, 3)
        task4 = testlist9.create_task(str(uuid.uuid4()), "run", "run 50 minutes", True, 1)

        with self.assertRaises(TodoListError):
            testlist8.order_task(task4, 0)

    def test_edit_task(self):
        testlist10 = TodoList(str(uuid.uuid4()), "market")
        task1 = testlist10.create_task(str(uuid.uuid4()), "banana", " test banana", True, 1)
        testlist10.edit_task(task1, name="avocado")
        self.assertEqual(task1.task_name, "avocado")

    def test_edit_task_not_existent_in_List(self):
        testlist11 = TodoList(str(uuid.uuid4()), "market")
        testlist12 = TodoList(str(uuid.uuid4()), "Gym")
        task = testlist11.create_task(str(uuid.uuid4()), "banana", " test banana", True, 1)

        with self.assertRaises(TodoListError):
            testlist12.edit_task(task, name="avocado")

    def test_order_tasks_by_priority(self):
        testlist13 = TodoList(str(uuid.uuid4()), "market")
        task1 = testlist13.create_task(str(uuid.uuid4()), "banana", " test banana", True, 3)
        task2 = testlist13.create_task(str(uuid.uuid4()), "apple", "test apple", False, 1)
        task3 = testlist13.create_task(str(uuid.uuid4()), "rice", "test rice", False, 2)
        expected_result = [task2, task3, task1]

        response = testlist13.sort_tasks_by_priority()

        self.assertEqual(response, expected_result)

    def test_create_not_bool_completed(self):
        testlist14 = TodoList(str(uuid.uuid4()), "market")
        with self.assertRaises(TodoListError):
            testlist14.create_task(str(uuid.uuid4()), "banana", " test banana", 5, 3)

    def test_create_not_int_priority(self):
        testlist15 = TodoList(str(uuid.uuid4()), "market")
        with self.assertRaises(TodoListError):
            testlist15.create_task(str(uuid.uuid4()), "banana", " test banana", True, "3")

    def test_create_list_database(self):
        email_user_test = "lucas_giovanini"
        identifier = str(uuid.uuid4())
        repository = TodoListRepository()
        response = repository.create_todo_list(email_user_test, identifier, "market")
        self.assertEqual(response.todolist_id, identifier)

    def test_create_task_database(self):
        repository = UserRepository()
        email_user = "lucas_giovanini"
        identifier = str(uuid.uuid4())
        lists = repository.get_code_from_user_list(email_user)
        selected_code = lists[1]['todolist_id']
        repository = TodoListRepository()
        position_in_list = repository.get_the_next_free_position(selected_code)
        response = repository.create_task(identifier, selected_code, "work", "i need finish my code", True, 1, position_in_list )
        print(response)
        self.assertEqual(response.task_id, identifier)

    def test_all_user_list(self):
        repository = UserRepository()
        email_user = "lucas_giovanini"
        lists = repository.get_code_from_user_list(email_user)
        recovered_lists = []
        for list_user in lists:
            recovered_lists.append(repository.recover_user_list(list_user['todolist_id']))
        assert len(lists) > 0





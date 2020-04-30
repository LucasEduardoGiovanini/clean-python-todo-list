import unittest
from domain.entities.todolist import TodoList
from domain.entities.task import Task
from domain.exception.custom_exception import TodoListError
from repositories import TodoListRepository


class Tests(unittest.TestCase):

    def test_create_list(self):
        response = TodoList("works of day", "test_email")
        self.assertEqual(response.todo_name, "works of day")

    def test_edit_list_name(self):
        testlist0 = TodoList("market", "test_email")
        testlist0.edit_list_name("testing")
        self.assertEqual(testlist0.todo_name, "testing")

    def test_add_task_to_list(self):
        testlist1 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist1.todo_name,
                                                                                 testlist1.email_creator)
        response = testlist1.create_task(todolist_id, "banana", "test banana", True, 1)
        self.assertEqual(response, testlist1.tasks[0])

    def test_remove_task_to_list(self):
        testlist2 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist2.todo_name,
                                                                                 testlist2.email_creator)

        created_task = testlist2.create_task(todolist_id, "apple", "test apple", False, 2)

        response = testlist2.remove_task(created_task)
        self.assertEqual(response, True)

    def test_remove_task_to_not_exist_in_list(self):
        testlist2false = TodoList("market", "test_email")
        testlist3false = TodoList("gym", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist3false.todo_name,
                                                                                 testlist3false.email_creator)
        response = testlist3false.create_task(todolist_id, "apple", "test apple", False, 2)

        with self.assertRaises(TodoListError):
            testlist2false.remove_task(response)

    def test_complete_task_not_completed(self):
        testlist3 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist3.todo_name,
                                                                                 testlist3.email_creator)
        task = testlist3.create_task(todolist_id, "apple", "test apple", False, 2)
        response = testlist3.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_complete_task_already_completed(self):
        testlist4 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist4.todo_name,
                                                                                 testlist4.email_creator)
        task = testlist4.create_task(todolist_id['todolist_id'], "apple", "test apple", True, 2)

        response = testlist4.complete_task(task)
        self.assertEqual(response.completed, True)

    def test_undo_task_already_completed(self):
        testlist5 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist5.todo_name,
                                                                                 testlist5.email_creator)
        task = testlist5.create_task(todolist_id, "apple", "test apple", True, 2)

        response = testlist5.undo_task(task)
        self.assertEqual(response.completed, False)

    def test_undo_task_not_completed(self):
        testlist6 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist6.todo_name,
                                                                                 testlist6.email_creator)
        task11 = Task(todolist_id, "apple", "test apple", False, 2)
        testlist6.add_task(task11)
        response = testlist6.undo_task(task11)
        self.assertEqual(response.completed, False)

    def test_order_task(self):
        testlist7 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist7.todo_name,
                                                                                 testlist7.email_creator)
        task1 = testlist7.create_task(todolist_id, "banana", " test banana", True, 1)
        task2 = testlist7.create_task(todolist_id, "apple", "test apple", False, 2)
        task3 = testlist7.create_task(todolist_id, "rice", "test rice", False, 3)

        response = testlist7.order_task(task3, 0)
        self.assertEqual(response[0], task3)

    def test_order_task_with_task_not_existent_in_list(self):
        testlist8 = TodoList("market", "test_email")
        testlist9 = TodoList("gym", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist8.todo_name,
                                                                                 testlist8.email_creator)
        task2 = testlist8.create_task(todolist_id, "apple", "test apple", False, 2)
        task3 = testlist8.create_task(todolist_id, "rice", "test rice", False, 3)

        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist9.todo_name,
                                                                                 testlist9.email_creator)
        task4 = testlist9.create_task(todolist_id, "run", "run 50 minutes", True, 1)

        with self.assertRaises(TodoListError):
            testlist8.order_task(task4, 0)

    def test_edit_task(self):
        testlist10 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist10.todo_name,
                                                                                 testlist10.email_creator)
        task1 = testlist10.create_task(todolist_id, "banana", " test banana", True, 1)
        testlist10.edit_task(task1, name="avocado")
        self.assertEqual(task1.task_name, "avocado")

    def test_edit_task_not_existent_in_List(self):
        testlist11 = TodoList("market", "test_email")
        testlist12 = TodoList("Gym", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist11.todo_name,
                                                                                 testlist11.email_creator)
        task = testlist11.create_task(todolist_id, "banana", " test banana", True, 1)

        with self.assertRaises(TodoListError):
            testlist12.edit_task(task, name="avocado")

    def test_order_tasks_by_priority(self):
        testlist13 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist13.todo_name,
                                                                                 testlist13.email_creator)
        task1 = testlist13.create_task(todolist_id, "banana", " test banana", True, 3)
        task2 = testlist13.create_task(todolist_id, "apple", "test apple", False, 1)
        task3 = testlist13.create_task(todolist_id, "rice", "test rice", False, 2)
        expected_result = [task2, task3, task1]

        response = testlist13.sort_tasks_by_priority()

        self.assertEqual(response, expected_result)

    def test_create_not_bool_completed(self):
        testlist14 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist14.todo_name,
                                                                                 testlist14.email_creator)
        with self.assertRaises(TodoListError):
            testlist14.create_task(todolist_id, "banana", " test banana", 5, 3)

    def test_create_not_int_priority(self):
        testlist15 = TodoList("market", "test_email")
        todolist_id = TodoListRepository().recover_list_id_by_namelist_and_email(testlist15.todo_name,
                                                                                 testlist15.email_creator)
        with self.assertRaises(TodoListError):
            testlist15.create_task(todolist_id, "banana", " test banana", True, "3")

    def test_create_list_database(self):
        email_user_test = "test_email"
        repository = TodoListRepository()
        response = repository.create_todo_list(email_user_test, "market")
        self.assertEqual(response.todo_name, "market")

    def test_create_task_database(self):
        repository = TodoListRepository()
        selected_code = repository.recover_list_id_by_namelist_and_email("market", "test_email")
        response = repository.create_task(selected_code['todolist_id'], "work", "i need finish my code", True, 1)  #crio a task na posição

        self.assertEqual(response.task_name, "work")

    def test_all_user_list(self):
        repository = TodoListRepository()
        email_user = "test_email"
        lists = repository.get_all_a_user_list_with_tasks(email_user)
        assert len(lists) > 0

drop database dbtodolist;
create database dbTodoList;
use dbTodoList;

create table tbUsuario(
email varchar(100) primary key,
senha varchar(200)
);

create table tbTodoList(
todolist_id varchar(36) not null default (uuid()),
email varchar(100),
todo_name varchar(40),
primary key (todolist_id),
foreign key (email) references tbUsuario(email)
);



create table tbTask(
task_id varchar(36) not null default (uuid()),
todolist_id varchar(36),
task_name varchar(40),
descripton varchar(100),
completed bool,
priority int,
queue_position int,
primary key (task_id),
foreign key (todolist_id) references tbTodoList(todolist_id)
);

insert into tbUsuario(email,senha) VALUES("test_email","testemail");
insert into tbTodoList(email,todo_name) VALUES("test_email","works of day");
insert into tbTodoList(email,todo_name) VALUES("test_email","cooking");
insert into tbTask(todolist_id,task_name,descripton,completed,priority,queue_position) VALUES ("f578b004-8df6-11ea-bc9c-0250cc5339c3","gym","monday i do leg training and Wednesday i do weightlifting",False,2,1);
insert into tbTask(todolist_id,task_name,descripton,completed,priority,queue_position) VALUES ("f578b004-8df6-11ea-bc9c-0250cc5339c3","cook","cooking spaghetti for the lunch",False,1,0);
insert into tbTask(todolist_id,task_name,descripton,completed,priority,queue_position) VALUES ("f578b004-8df6-11ea-bc9c-0250cc5339c3","cook","cooking spaghetti for the lunch",False,1,0);
select * from tbUsuario;
select * from tbTodoList;
select * from tbTask;
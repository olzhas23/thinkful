drop table if exists person;

create table person (
	id int primary_key not null,
	name text not null,
	age int);
	
insert into person values
(1, 'bob',22)
(2, 'sue', 34)
(3, 'timmy', 19)
(4, 'ellen', 23)

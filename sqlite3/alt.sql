alter  table person RENAME TO peoples;
alter table peoples add column hatred integer ;
alter table peoples rename to person;
alter table person add column height integer;
alter table person add column weight integer ;
alter table pet add column dob date;
alter table pet add column breed text;

select*from pet;
select*from peoples;
select*from person;
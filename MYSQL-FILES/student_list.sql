select count(tamil), name from std_mark_list group by name having count (tamil)>50;
select * from std_info;
select * from std_mark_list;
select name from std_info order by dob desc;
select * from std_mark_list left join std_info on std_mark_list . reg_no = std_info . reg_no;
select * from std_info;
select * from std_mark_list;
alter table std_mark_list add grat char(2);
describe std_mark_list;
use student_list;
show tables;
delimiter //
create procedure s4()
begin
select * from salary_info;
end //
call s2();
select name from std_info;
select name from std_info where name like 'a%';
select * from std_info order by father_name asc;
select * from std_info order by name desc;
select * from salary_info order by salary desc;
show tables;
select * from teachers_info right join salary_info on teachers_info ._id= salary_info. _id;












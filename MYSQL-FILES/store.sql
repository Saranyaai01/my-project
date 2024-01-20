use sample1_db;
create table sample_table (
user_id int not null primary key auto_increment,
name varchar(50),
qualification varchar(50)
);
delimiter &&
create procedure insert_table (
in nameparameter varchar(50),
in qualificationparameter varchar(50)
)
begin
insert into sample_table(name,qualification) values (nameparameter, qualificationparameter);
end &&
delimiter;
call insert_table('hazeera','BA');
select * from sample_table;

delimiter ##
use sample1_db;##
drop procedure if exists mycode;##
create procedure mycode(
in tablename varchar(255),
in columnname varchar(255),
in valuechange varchar(255),
in idname varchar(255),
in idparam int 
)
begin
set @statement=concat("update ",tablename," set ",columnname, "=\'",valuechange,'\'',' where ',idname,'=',idparam);

prepare stmt from @statement;
execute stmt;
end ##
 delimiter ;   
 
select * from sample_table;
describe sample_table;
call mycode('sample_table','name','jaya','user_id',3);
alter database sample1.db modify name = ai_saranya;

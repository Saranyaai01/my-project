use ai_saranya;
show tables;
select * from sample_table;
select * from batch01_details;
select * from system_info;
select * from student_details;
delimiter &&
drop procedure if  exists renam;&&
create procedure renam (
in tablename varchar(50),
in old_name varchar(50),
in new_name varchar(50)
)
begin
set @statement = concat('alter table ',tablename,' rename ', 'column ' , old_name ,' to ', new_name );
prepare stmt from  @statement ;
execute stmt;
end &&
delimiter ;
call renam('sample_table','user_id','ID');

delimiter &&
drop procedure if exists al_integer;&&
create procedure al_integer(
in tablename varchar(50),
in columnname int
)
begin

set @statement = concat(' alter table ',tablename, ' add column ',columnname ,' int ');
prepare stmt from @statement;
execute stmt;
end &&
delimiter ;
call al_varchar('student_details','SNO');

alter table student_details modify column SNO int primary key auto_increment;

delimiter ##
drop procedure if exists mycode1;##
create procedure mycode1(
in tablename varchar(255),
in columnname varchar(255),
in valuechange int,
in idname varchar(255),
in idparam varchar(255) 
)
begin
set @statement=concat("update ",tablename," set ",columnname, "=\'",valuechange,'\'',' where ',idname,'=',idparam);

prepare stmt from @statement;
execute stmt;
end ##
 delimiter ;   
 call mycode1('system_info','SNO',31,'name','Yogarajank');
 update system_info set SNO = 31 where name = 'yogarajan k';



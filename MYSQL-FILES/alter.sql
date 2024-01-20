SELECT * FROM ai_saranya.system_info;
delimiter &&
create procedure insert_table (
in nameparameter varchar(50),
in qualificationparameter varchar(50)
)
begin
insert into sample_table(name,qualification) values (nameparameter, qualificationparameter);
end &&
delimiter ;
delimiter ##
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
 
 delimiter &&
drop procedure if exists de;&&
create procedure de (
in tablename varchar(50),
in idname varchar(50),
in idparam int
)
begin
set @statement = concat("delete ", 'from ',tablename,' where ',idname,'=',idparam );
prepare stmt from @statement;
execute stmt;
end &&
 delimiter ;
 call de('sample_table','user_id',1);
 select * from batch01_details;
 select * from sample_table;

alter table batch01_details drop column middle_Name;
delimiter ##
drop procedure if exists dr;##
create procedure dr(
in tablename varchar(50),
in columnname varchar(50)
)
begin
set  @statement = concat('alter table ',tablename,' drop column ',columnname);
prepare stmt from @statement;
execute stmt;
end ##
delimiter ;

call dr('batch01_details','last_name');
select * from batch01_details;
select * from sample_table;
call insert_table('jaya','Msc');
alter table sample_table add column location varchar(70) not null;
delimiter &&
drop procedure if exists al_varchar;&&
create procedure al_varchar(
in tablename varchar(50),
in columnname varchar(50)
)
begin

set @statement = concat(' alter table ',tablename, ' add column ',columnname ,' varchar\(70\)');
prepare stmt from @statement;
execute stmt;
end &&
delimiter ;
call al_varchar('sample_table','location');
show tables;
use ai_saranya;
select * from sample_table;
call mycode('sample_table','location','trichy','user_id',12);
call de('sample_table','user_id',13);
alter table batch01_details rename column first_name to name;
select * from batch01_details;
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
call renam ('sample_table','name ','first_name ');

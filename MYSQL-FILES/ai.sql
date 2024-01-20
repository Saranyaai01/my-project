create database sample1_db;
use sample1_db;
show tables;
create table ai_batch01 
(
SNO int not null primary key,
first_Name varchar(50) not null, 
middle_Name varchar(50) not null,
last_Name varchar(50) not null,
DOB date not null,
Aadhar_Number long ,
Biometric_ID long ,
Primary_Contact_No long ,
Secondary_Contact_No long ,
WhatsApp_No long ,
User_name varchar(50) not null,
Password varchar(50) not null,
UG varchar(50),
Subject_Group varchar(50),
PG varchar(50),
Subject varchar(50),
Year_of_Passing int,
AI_Batch_Email varchar(70),
Email varchar(70),
Address varchar(250),
District varchar(50),
Father_Name varchar(60),
 Husband_Name varchar(60),
 Mother_Name varchar(60));
 show  tables;
 describe ai_batch01;
 insert into ai_batch01 values(1,'Abdul Rahman  B',' ', ' ','2001-01-15',669092087983,92087983,9952630126,6369696359,9952630126,'TI2023M-C01E438
','Password@123','BSC','Computer science',' ',' ',2022,'','abdulrahman001007@gmail.com','No 3/1-76 Indra street Keela ambikaburam Trichy-04','Trichy','Badhusha',' ','Noorjahan');
insert into ai_batch01 values(2,'Arun T',' ',' ','2001-01-16',341246643302,46643302,8525880306,6382506148,8525880306,'PU2023M-C01E488
','Password@123','BSC','Computer science',' ',' ',2023,' arunaathi41@gmail.com','arunaathi41@gmail.com','3/4 Thirupur Thirupur (po) Kulathur(tk)Senaiyakuti Pudukkottai (Dt) 622502
', 'pudukkottai',' ','Tamil selvam
','Suppu laxmi
');
insert into ai_batch01 values(3,'Aysha sithika L',' ',' ' ,'1988-01-11',784654756225,54756225,8124823036,8610353074,8124823036,'TI2023F-C01E78D Navalpattu Trichy -26','Trichy',' ','Nazrul Islam','Amthul jabeen');
insert into ai_batch01 values(4,'Bhavani R',' ',' ','2002-10-13',935775705642,75705642,6380185097,9659871377,6380185097,'Pu2023F-C01E44D','Password@123','BSC','Computer science',' ',' ',2023,'bhavanirai01@gmail.com','bb464490@gmail.com','Melakkottai Kovilur (p)Alangudi Tk Pudukkottai (dt)','Pudukkottai','C.Ramachandran
',' ','R.Thenmozhi
');



insert into ai_batch01 values(5,'Fathima M',' ',' ', '2002-12-17',622631324614,31324614,6374041818,9791676433,6374041818,'TI2023F-C01E43B','Password@123','B.Com','Commerce',' ',' ',2024,'Ray0488faths@gmail.com','Ray0488faths@gmail.com','5/249 20th cross vasancity vayalur road trichy-620102','Trichy','Mohamed Ibrahi',' ','Saira banu');

insert into ai_batch01 values(6,'Ghouse bi S',' ',' ','1989-08-14',818393990050,93990050,9994286043,7708475065,9994286043,'TI2023F-C01E46D','Password@123','B.A.
','English',' ',' ',2010,'happydhillu@gmail.com','happydhillu@gmail.com','MIG 49 Phase 1 Anna nagarTNUDP trichy-620026','Trichy',' ','Juber khan B','Zarina Begum
');


insert into ai_batch01 values(7,'Gnanagowsalya K',' ',' ','2003-04-29',418718821662,18821662,7094373123,9965452410,7094373123,'TI2023F-C01E474','Password@123','Bsc ','Computer science',' ',' ',2023,'kkowsalyaai01@gmail.com','kowsalyakannan29@gmail.com','26/1 College roadSri Ram theatre near MusiriTrichy(Dt)','Trichy','Kannan A',' ','Sundhari K');


insert into ai_batch01 values(8,'Hajeera Sithika L',' ',' ','1992-06-11',430341868981,41868981,8056447098,9751471799,8056447098,'TI2023F-C01E796
','Password@123','BA','English',' ',' ',2013,'hajeerasithka2021@gmail.com','hajeerasithka2021@gmail.com','3 murugesan street M K kottai trichy
','Trichy',' ','Syed Azarudeen','Amthul jabeen');

insert into ai_batch01 values(9,'HARIHARAN A',' ',' ','2001-10-11',304765424440,65424440,9363649175,9363649175,9363649175,'PE2023M-C01E437','Password@123','BE','EEE',' ',' ',2023,'hariharananbu2001@gmail.com','hariharananbu2001@gmail.com','2/225 North st keelapuliyur po Kunnam tk Perambalur dt 621115','Perambalur','ANBALAGAN D',' ','Anjalai A');

insert into ai_batch01 values(10,'Jayalakshmi R',' ',' ','1997-02-06',432445616668,45616668,9500628375,6385632493,6385632493,'TI2023F-C01E444','Password@123','BCA','Computer application','MCA','Computer Application',2019,'jayalakshmiai01@gmail.com','jasperjeevi@gmail.com','28-A bharathiyar Street west ambigapuram trichy-4','Trichy','Ravikumar',' ','Geetha');

insert into ai_batch01 values(11,'Jothika J',' ',' ','2003-01-08',693941180387,41180387,9585607631,9843412199,9585607631,'TI2023F-C01E555','Password@123','BSC','Mathematics',' ',' ',2023,'jothikajai01@gmail.com','jothikajagan8@gmail.com','H/5 Housing Unit Parvathipuram,Musiri Trichy DT','Trichy','Jegatharatchagan K',' ','Manjula J');

insert into ai_batch01 values(12,'Kalaiarasan A',' ',' ','1987-07-29',447595386464,95386464,9600330846,9994057344,9600330846,'TI2023M-C01E78B','Password@123','B.com','Commerce',' ',' ',2009,'Kalaiarasanayyavooai0@gmail.com','Kalai29.7@gmail.com','2/337 navalpattu burma colony oft po trichy 16','Trichy','K Ayyavoo',' ','A Vasanthi');
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]

update salary SET sex = 'w' where sex = 'm';
update salary SET sex = 'm' where sex = 'f';
update salary SET sex = 'f' where sex = 'w';


# 正解
UPDATE salary
SET sex = IF(sex = 'm', 'f', 'm')
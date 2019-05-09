/* 创建数据库 */
CREATE DATABASE IF NOT EXISTS testdb;

use testdb;

/* 用户表 */
CREATE TABLE IF NOT EXISTS user(
    name varchar(20),
    userid int,
    PRIMARY KEY (userid));

/* 插入初始数据 */
INSERT INTO user VALUES('Tom',1);
INSERT INTO user VALUES('Ben',2);



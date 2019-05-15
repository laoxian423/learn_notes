/*=====================================*/
/*股票信息数据库DDL脚本*/
/* Client does not support authentication protocol requested by server */
/* 容器mysql 8.0 */
/* ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '你的密码'; */
/* ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';*/
/* SELECT plugin FROM mysql.user WHERE User = 'root';*/
/*=====================================*/

/* 创建数据库 */
create database if not exists NASDAQ;

use NASDAQ;

drop table if exists HistoricalQuote;

drop table if exists Stocks;

/*=====================================*/
/*Table :HistroicalQuote  历史数据表    */
/*=====================================*/
create table HistoricalQuote
(
    HDate       varchar(12),
    Open        decimal(8,4),
    High        decimal(8,4),
    Low         decimal(8,4),
    Close       decimal(8,4),
    Volume      bigint,
    Symbol      varchar(10),
    primary key (HDate)
);

/*=====================================*/
/*Table :Stocks  历史数据表             */ 
/*=====================================*/
create table Stocks
(
    Symbol      varchar(10) not null,
    Company     varchar(50) not null,
    Industry    varchar(10) not null,
    primary key (Symbol)
);

/*
ALTER table HistoricalQuote add CONSTRAINT FK_Reference_1 foreign key (Symbol)
        references Stocks (Symbol) on delete restrict on update restrict;
*/
INSERT INTO Stocks (Symbol, Company, Industry) values ('AAPL', 'Apple Inc.', 'Technology');
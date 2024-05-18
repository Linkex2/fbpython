create database musicstore;

use musicstore;

create table usuario (
id int primary key auto_increment,
email varchar(345),
senha varchar(255)
);

create table produtomusica (

id_produtomusica int  NOT NULL primary key auto_increment,
descricao varchar(255),
marca varchar(50),
valor float,
estoque int

);
DROP TABLE IF EXISTS agents;
CREATE TABLE agents (
	id SERIAL PRIMARY KEY,
	email varchar(255) DEFAULT NULL,
	password varchar(255) DEFAULT NULL,
	fio varchar(255) DEFAULT NULL,
	obrazovanie text,
	samozan varchar(255) DEFAULT NULL,
  	city varchar(255) DEFAULT NULL,
  	opit varchar(255) DEFAULT NULL,
  	phone varchar(255) DEFAULT NULL,
  	date date DEFAULT NULL,
  	resume varchar(255) DEFAULT NULL,
  	photo bytea NOT NULL,
  	telegramid int DEFAULT NULL,
  	activation int DEFAULT NULL
);

DROP TABLE IF EXISTS clients;
CREATE TABLE clients (
	id SERIAL PRIMARY KEY,
	name text NOT NULL,
  	inn varchar(222) NOT NULL,
  	contacts text NOT NULL,
  	comments text NOT NULL,
  	objects text NOT NULL,
  	contact_name text NOT NULL,
  	agent_id int NOT NULL
);

DROP TABLE IF EXISTS deals;
CREATE TABLE deals (
  	id SERIAL PRIMARY KEY,
 	deals_id int NOT NULL,
  	company_name varchar(255) NOT NULL,
	etap varchar(255) NOT NULL,
 	budget varchar(255) NOT NULL,
 	agent_id int NOT NULL
);

DROP TABLE IF EXISTS deals_history;
CREATE TABLE deals_history (
  	id SERIAL PRIMARY KEY,
  	date varchar(100) NOT NULL,
  	message text NOT NULL
);
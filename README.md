# SBBSurprise

## Backend

### Requirements
- Python & pip
- (optional for DB manipulation) [SQLite](https://www.sqlite.org/)

### Dependencies
`pip install flask flask-restful flask-cors pandas requests`


### Run
`flask run`
Serving at [localhost:5000](http://localhost:5000)


## Frontend 

### Requirements
- [Node.js](https://nodejs.org)

### Dependencies
1. cd to `/frontend`
2. `npm install`

### Run
1. cd to `/frontend`
2. `npm run dev`
3. Serving at [localhost:8080](http://localhost:8080)


# Stack preparation
## Flask RESTful
https://flask-restful.readthedocs.io/en/latest/quickstart.html

## Postman
https://www.getpostman.com/downloads/

## Sqlite3
https://www.sqlite.org/cli.html
sudo apt install sqlite3

create table todos1(id varchar(10), task varchar(200));

insert into todos1 values('todo1','get up');

select * from todos1;

.save db1.db

create table users
(
	id INTEGER not null
		constraint users_pk
			primary key autoincrement,
	email NVARCHAR not null,
	name NVARCHAR not null
);

INSERT INTO users (email, name) VALUES ('alexbutol@yandex.ru','butol');
INSERT INTO users (email, name) VALUES ('leha@yandex.ru','leha');
INSERT INTO users (email, name) VALUES ('vasyl@yandex.ru','vasy');

SELECT * FROM users;

INSERT INTO places (name, description, owner_id)
VALUES ('kilfish', 'полная херня, палена алкашка, некит ушел блевать и мы его проебали', 1);
INSERT INTO places (name, description, owner_id)
VALUES ('we cideria', 'охуенное место, всемм советую. Попробуйте сидр пьяный русский', 1);
INSERT INTO places (name, description, owner_id)
VALUES ('acha-chacha', 'Ходил с бабушкой, оч вкусно поели. Хинкали топ!', 2);

SELECT * FROM places;


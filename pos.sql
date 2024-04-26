CREATE TABLE productos(
    Codigo int not null Unique,
    Nombre VARCHAR(255) not null,
    Precio Float(9,2) not null
);

INSERT INTO productos VALUES 
("1", "Cafe","20.00"),
("2", "Cheve","15.00"),
("3", "Powerade","30.00"),
("4", "Cocacola","12.00"),
("5", "Mouse","200.00"),
("6", "Pantalla","4500.00"),
("7", "Carro","800000.00"),
("8", "Azucar","10.00"),
("9", "Queso","40.00"),
("10", "Pizza","220.00");
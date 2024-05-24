-- Criar o banco de dados
CREATE DATABASE Speccialle;

-- Selecionar o banco de dados
USE Speccialle;

-- Criar a tabela
CREATE TABLE Contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Mensagem TEXT NOT NULL
);
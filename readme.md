# Projeto SA

Este projeto consiste na criação de um site para uma empresa de cerimonialista chamada "Specialle Assessoria". O site tem como objetivo apresentar os serviços oferecidos pela empresa, informações de contato e permitir que os visitantes entrem em contato para solicitar mais informações ou agendar serviços.

## Informações do Projeto

- **Empresa:** Specialle Assessoria
- **Desenvolvedor:** Renan Tomasi

## Descrição

Este projeto é um site estático desenvolvido utilizando o microframework Flask, com HTML e CSS. O site inclui várias páginas, como a página inicial, página "Sobre", página de "Contato" e uma página de formulário para os visitantes entrarem em contato com a empresa. A interface é responsiva e foi desenvolvida com o framework Bootstrap, garantindo uma excelente experiência do usuário em diferentes dispositivos. Além disso, o site integra um banco de dados MySQL para gerenciar os dados dos formulários de contato.

## Requisitos

O que foi exigido para a criacão desse site:

- Criar dentro do Flask
- utilizar pelo menos 5 componentes do framework Bootstrap
- Aplicar o recurso @media para aplicar responsividade
- Utilizar o Flexbox para organizar os elementos
- Integração com MySQL

## Componentes do Bootstrap Utilizados

Durante o desenvolvimento do site, os seguintes componentes do Bootstrap foram utilizados:

- Navbar
- Carousel
- Cards
- Forms
- Alerts
- Buttons
- Grid System

## Como Executar o Projeto

1. Clone este repositório para o seu ambiente local.
  ```git
  git clone https://github.com/renan21-tg/Projeto-SA
  ```
2. Crie e inicie seu ambiente virtual:
  ```shell
  python -m venv venv
  ```
  ```shell
  .\venv\Scripts\activate
  ```
3. Instale o flask através do arquivo requirements.txt
  ```shell
  pip install -r requirements.txt
  ```
4. Crie o banco de dados no seu MySQL através do script.sql
  ```sql
  CREATE DATABASE Speccialle;
  
  USE Speccialle;
  
  CREATE TABLE Contatos (
      id INT AUTO_INCREMENT PRIMARY KEY,
      Nome VARCHAR(100) NOT NULL,
      Email VARCHAR(100) NOT NULL,
      Mensagem TEXT NOT NULL
  );
  ```
5. Inicie o flask
  ```shell
  flask run
  ```
## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, por favor, abra uma issue ou envie um pull request.

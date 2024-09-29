package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexão {
    public static void main(String[] args) {


        try {
            String url = "jdbc:postgresql://localhost:5432/Curso";
            String usuario = "postgres";
            String senha = "lolseek005";
            Connection connection = DriverManager.getConnection(url,usuario,senha);
            System.out.println("Conexao realizada com sucesso!");
            connection.close();
        } catch (SQLException erro) {
            System.out.println("Problemas na conexao com a fonte de dados"	+ erro.toString());
        }
    }
}

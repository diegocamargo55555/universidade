package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Insere {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/Curso";
        String usuario = "postgres";
        String senha = "lolseek005";

        try {
            Connection connection = DriverManager.getConnection(url,usuario,senha);
            System.out.println("Conexao realizada com sucesso!");

            String sql = "INSERT INTO estudante (estudante_id, nome, idade) VALUES(?,?,? )";
            PreparedStatement stmt = connection.prepareStatement(sql);
            stmt.setInt(1, 1);
            stmt.setString(2, "Vitor");
            stmt.setInt(3, 20);
            stmt.executeUpdate();


        } catch (SQLException erro) {
            System.out.println("Problemas na conexao com o banco de dados"	+ erro.toString());
        }
    }
}

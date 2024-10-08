package org.example.dao;

import org.example.model.Estudante;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class EstudanteDBDAO implements EstudanteDAO, IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    private void open() throws SQLException {
        connection = Conexao.getConexao(Conexao.stringDeConexao, Conexao.usuario, Conexao.senha);
    }

    private void close() throws SQLException {
        connection.close();
    }

    public void insere(Estudante estudante) throws SQLException {
        open();
        sql = "INSERT INTO estudante(estudante_Id, nome, idade) VALUES(?,?,?)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudante.getEstudanteId());
        statement.setString(2, estudante.getNome());
        statement.setInt(3, estudante.getIdade());
        statement.executeUpdate();
        close();
    }

    public void atualiza(Estudante estudante) throws SQLException {
        open();
        sql = "UPDATE estudante SET nome = ?, idade = ? WHERE estudante_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setString(1, estudante.getNome());
        statement.setInt(2, estudante.getIdade());
        statement.setInt(3, estudante.getEstudanteId());
        statement.executeUpdate();
        close();
    }

    public void remove(Estudante estudante) throws SQLException {
        open();
        sql = "DELETE FROM estudante WHERE estudante_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudante.getEstudanteId());
        statement.executeUpdate();
        close();
    }

    public Estudante buscaPorCodigo(int estudanteId) throws SQLException {
        open();
        sql = "SELECT * FROM estudante WHERE estudante_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudanteId);
        result = statement.executeQuery();
        if (result.next()) {
            Estudante estudante = new Estudante();
            estudante.setEstudanteId(result.getInt("estudante_id"));
            estudante.setNome(result.getString("nome"));
            estudante.setIdade(result.getInt("idade"));
            close();
            return estudante;
        } else{
            close();
            return null;
        }
    }
    public List<Estudante> listaTodos() throws SQLException {
        open();
        sql = "SELECT * FROM estudante";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        ArrayList<Estudante> estudantes = new ArrayList<>();
        while (result.next()) {
            Estudante estudante = new Estudante();
            estudante.setEstudanteId(result.getInt("estudante_id"));
            estudante.setNome(result.getString("nome"));
            estudante.setIdade(result.getInt("idade"));
            estudantes.add(estudante);
        }
        close();
        return estudantes;
    }
}
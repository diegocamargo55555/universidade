package org.example.dao;

import org.example.model.Estudante;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
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
        sql = "INSERT INTO estudante(estudante_ID, nome, idade) VALUES(???)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudante.getEstudanteID());
        statement.setString(2, estudante.getNome());
        statement.setInt(3, estudante.getIdade());
        statement.executeUpdate();
        close();
    }

    @Override
    public void atualiza(Estudante estudante) throws SQLException {
        open();
        sql = "UPDATE estudante set nome=?, idade=? WHERE estudante_ID=?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudante.getEstudanteID());
        statement.setString(2, estudante.getNome());
        statement.setInt(3, estudante.getIdade());
        statement.executeUpdate();
        close();
    }

    @Override
    public void remove(Estudante estudante) throws SQLException {
        open();
        sql = "Delete From estudante WHERE estudante_id=?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudante.getEstudanteID());
        statement.setString(2, estudante.getNome());
        statement.setInt(3, estudante.getIdade());
        statement.executeUpdate();
        close();

    }

    @Override
    public Estudante buscaPorCodigo(int estudanteID) throws SQLException {
        open();
        sql = "SELECT * FROM estudante WHERE estudanteid=?";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        statement.setInt(1, estudanteID);
        if (result.next()) {
            Estudante estudante = new Estudante();
            estudante.setEstudanteID(result.getInt("estudante_ID"));
            estudante.setNome(result.getString("nome"));
            estudante.setIdade(result.getInt("idade"));
            close();
            return estudante;
        } else {
            close();
            return null;
        }
    }

    public List<Estudante> listaTodos() throws SQLException {
        open();
        sql = "SELECT * GROM estudante";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        ArrayList<Estudante> estudantes = new ArrayList<>();
        while (result.next()) {
            Estudante estudante = new Estudante();
            estudante.setEstudanteID(result.getInt("estudante_id"));
            estudante.setNome(result.getString("nome"));
            estudante.setIdade(result.getInt("idade"));
            estudantes.add(estudante);
        }
        close();
        return estudantes;

    }
}
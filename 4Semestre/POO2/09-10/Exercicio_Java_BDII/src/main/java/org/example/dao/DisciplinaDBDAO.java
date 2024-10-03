package org.example.dao;

import org.example.model.Disciplina;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DisciplinaDBDAO extends Disciplina implements IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    public void open() throws SQLException{
        connection = Conexao.getConexao(Conexao.stringDeConexao, Conexao.usuario, Conexao.usuario);
    }

    public void close() throws SQLException{
        connection.close();
    }
}

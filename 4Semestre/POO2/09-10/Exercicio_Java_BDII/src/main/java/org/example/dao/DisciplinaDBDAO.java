package org.example.dao;

import org.example.model.Disciplina;
import org.example.model.Estudante;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

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
    public void insere(Disciplina disciplina) throws SQLException {
        open();
        sql = "INSERT INTO estudante(estudante_ID, nome, idade) VALUES(?,?)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplina.getDisciplinaID());
        statement.setString(2, disciplina.getNome());
        statement.executeUpdate();
        close();
    }

    public void atualiza(Disciplina disciplina) throws SQLException {
        open();
        sql = "UPDATE estudante set nome=?, idade=? WHERE estudante_ID=?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplina.getDisciplinaID());
        statement.setString(2, disciplina.getNome());
        statement.executeUpdate();
        close();
    }

    public void remove(Disciplina disciplina) throws SQLException {
        open();
        sql = "Delete From estudante WHERE estudante_id=?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplina.getDisciplinaID());
        statement.setString(2, disciplina.getNome());
        statement.executeUpdate();
        close();

    }

    public Estudante buscaPorCodigo(int disciplinaID) throws SQLException {
        open();
        sql = "SELECT * FROM estudante WHERE estudanteid=?";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        statement.setInt(1, disciplinaID);
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

    public List<Disciplina> listaTodos() throws SQLException {
        open();
        sql = "SELECT * fROM disciplina";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        ArrayList<Disciplina> disciplinas = new ArrayList<>();
        while (result.next()) {
            Disciplina disciplina = new Disciplina();
            disciplina.setDisciplinaID(result.getInt("estudante_id"));
            disciplina.setNome(result.getString("nome"));
            disciplinas.add(disciplina);
        }
        close();
        return disciplinas;

    }
}

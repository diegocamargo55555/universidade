package org.example.dao;

import org.example.model.Disciplina;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DisciplinaDBDAO implements DisciplinaDAO, IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;
    public void open() throws SQLException {
        connection = Conexao.getConexao(Conexao.stringDeConexao, Conexao.usuario, Conexao.senha);
    }
    public void close() throws SQLException{
        connection.close();
    }

    public void insere(Disciplina disciplina) throws SQLException {
        open();
        sql = "INSERT INTO Disciplina(disciplinaId, nome) VALUES(?,?)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplina.getDisciplinaId());
        statement.setString(2, disciplina.getNome());
        statement.executeUpdate();
        close();
    }
    public void atualiza(Disciplina disciplina) throws SQLException {
        open();
        sql = "UPDATE disciplina SET nome = ? WHERE disciplinaId = ?";
        statement = connection.prepareStatement(sql);
        statement.setString(1, disciplina.getNome());
        statement.setInt(2, disciplina.getDisciplinaId());
        statement.executeUpdate();
        close();
    }
    public void remove(Disciplina disciplina) throws SQLException {
        open();
        sql = "DELETE FROM disciplina WHERE disciplinaID = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplina.getDisciplinaId());
        statement.executeUpdate();
        close();
    }
    public Disciplina buscaPorCodigo(int disciplinaId) throws SQLException {
        open();
        sql = "SELECT * FROM disciplina WHERE disciplinaId = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, disciplinaId);
        result = statement.executeQuery();
        if(result.next()){
            Disciplina disciplina = new Disciplina();
            disciplina.setDisciplinaId(disciplinaId);
            disciplina.setNome(result.getString("nome"));
            close();
            return disciplina;
        } else{
            close();
            return null;
        }
    }


    public List<Disciplina> listaTodos() throws SQLException {
       open();

       sql = "SELECT * FROM disciplina";
       statement = connection.prepareStatement(sql);
       result = statement.executeQuery();
       ArrayList<Disciplina> disciplinas = new ArrayList<>();
       while(result.next()){
           Disciplina disciplina = new Disciplina();
           disciplina.setDisciplinaId(result.getInt("disciplinaId"));
           disciplina.setNome(result.getString("nome"));
           disciplinas.add(disciplina);
       }
       close();
       return disciplinas;
    }
}

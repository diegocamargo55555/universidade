package org.example.dao;


import org.example.model.EstudanteDisciplina;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class EstudanteDisciplinaDBDAO implements EstudanteDisciplinaDAO, IConst{
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
    public void insere(EstudanteDisciplina estudanteDisciplina) throws SQLException{
        open();
        sql = "INSERT INTO estudante_disciplina(estudante_id, disciplinaid) VALUES(?,?)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudanteDisciplina.getEstudante().getEstudanteId());
        statement.setInt(2, estudanteDisciplina.getDisciplina().getDisciplinaId());
        statement.executeUpdate();
       close();
    }

    public void atualiza(EstudanteDisciplina estudanteDisciplina) throws SQLException {
        open();
        sql = "UPDATE estudante_disciplina SET disciplinaid = ? WHERE estudante_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudanteDisciplina.getDisciplina().getDisciplinaId());
        statement.setInt(2, estudanteDisciplina.getEstudante().getEstudanteId());
        statement.executeUpdate();
        close();
    }

    public void remove(EstudanteDisciplina estudanteDisciplina) throws SQLException {
       open();
       sql = "DELETE FROM estudante_disciplina WHERE estudante_id = ?";
       statement = connection.prepareStatement(sql);
       statement.setInt(1, estudanteDisciplina.getEstudante().getEstudanteId());
       statement.executeUpdate();
       close();
    }

    public EstudanteDisciplina buscaIndividual(int estudanteId, int disciplinaID) throws SQLException{
        open();
        sql = "SELECT * FROM estudante_disciplina WHERE estudante_id=? AND disciplinaid=?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudanteId);
        statement.setInt(2, disciplinaID);
        result = statement.executeQuery();
        EstudanteDBDAO estudanteDB = new EstudanteDBDAO();
        DisciplinaDBDAO disciplinaDB = new DisciplinaDBDAO();
        if(result.next()){
            EstudanteDisciplina estudanteDisciplina = new EstudanteDisciplina();
            estudanteDisciplina.setEstudante(estudanteDB.buscaPorCodigo(result.getInt("estudante_id")));
            estudanteDisciplina.setDisciplina(disciplinaDB.buscaPorCodigo(result.getInt("disciplinaid")));
            close();
            return estudanteDisciplina;
        } else{
            close();
            return null;
        }
    }

    public List<EstudanteDisciplina> listaTodos() throws SQLException{
        open();
        sql = "SELECT * FROM estudante_disciplina";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        ArrayList<EstudanteDisciplina> estudantesDisciplinas = new ArrayList<>();
        EstudanteDBDAO estudanteDB = new EstudanteDBDAO();
        DisciplinaDBDAO disciplinaDB = new DisciplinaDBDAO();
        while(result.next()){
            EstudanteDisciplina estudanteDisciplina  = new EstudanteDisciplina();
            estudanteDisciplina.setEstudante(estudanteDB.buscaPorCodigo(result.getInt("estudante_id")));
            estudanteDisciplina.setDisciplina(disciplinaDB.buscaPorCodigo(result.getInt("disciplinaid")));
            estudantesDisciplinas.add(estudanteDisciplina);
        }
        close();
        return estudantesDisciplinas;
    }
}

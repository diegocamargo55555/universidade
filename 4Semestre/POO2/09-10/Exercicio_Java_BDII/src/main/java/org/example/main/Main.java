package org.example.main;

import java.sql.SQLException;

import org.example.dao.DisciplinaDBDAO;
import org.example.dao.EstudanteDBDAO;
import org.example.dao.EstudanteDisciplinaDBDAO;
import org.example.model.Disciplina;
import org.example.model.Estudante;
import org.example.model.EstudanteDisciplina;

public class Main {

    public static void main(String[] args) throws SQLException {
        Estudante estudante = new Estudante(1, "Andre", 22);
        EstudanteDBDAO estudanteDAO = new EstudanteDBDAO();

        System.out.println("######### Opera��es sobre a tabela Estudante ###########");

        System.out.println("Insere o estudante Andr�:");
        estudanteDAO.insere(estudante);

        System.out.println("Lista os estudantes no banco:");
        //Chamadas a println com apenas um objeto fazem com que toString seja chamado
        //automaticamente.
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Muda o nome de Andr� para Andr� Galv�o e idade de 22 para 17:");
        Estudante estudante01 = new Estudante(1, "Andr� Galv�o", 17);
        estudanteDAO.atualiza(estudante01);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Insere o estudante Mario:");
        Estudante estudante02 = new Estudante(2, "Mario", 23);
        estudanteDAO.insere(estudante02);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Insere a estudante Mariane:");
        Estudante estudante03 = new Estudante(3, "Mariane", 19);
        estudanteDAO.insere(estudante03);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Retorna o estudante Mario:");
        System.out.println(estudanteDAO.buscaPorCodigo(2));

        System.out.println("Remove o estudante Mario:");
        estudanteDAO.remove(estudanteDAO.buscaPorCodigo(2));

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("\n######### Opera��es sobre a tabela Disciplina ###########");

        Disciplina disciplina = new Disciplina(1, "Matem�tica");
        DisciplinaDBDAO disciplinaDAO = new DisciplinaDBDAO();

        System.out.println("Insere a disciplina Matem�tica:");
        disciplinaDAO.insere(disciplina);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Muda o nome de Matem�tica para C�lculo I:");
        Disciplina disciplina01 = new Disciplina("C�lculo I", 1);
        disciplinaDAO.atualiza(disciplina01);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Insere a disciplina Portugu�s:");
        Disciplina disciplina02 = new Disciplina(2, "Portugu�s");
        disciplinaDAO.insere(disciplina02);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Insere a disciplina Ingl�s:");
        Disciplina disciplina03 = new Disciplina(3, "Ingl�s");
        disciplinaDAO.insere(disciplina03);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Retorna a disciplina Portugu�s:");
        System.out.println(disciplinaDAO.buscaPorCodigo(2));

        System.out.println("Remove a disciplina Portugu�s:");
        disciplinaDAO.remove(disciplinaDAO.buscaPorCodigo(2));

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("\n######### Opera��es sobre a tabela EstudanteDisciplina ###########");

        EstudanteDisciplina estudanteDisciplina = new EstudanteDisciplina();
        estudanteDisciplina.setEstudante(estudanteDAO.buscaPorCodigo(1));
        estudanteDisciplina.setDisciplina(disciplinaDAO.buscaPorCodigo(1));

        System.out.println("Cria rela��o entre estudante e disciplina:");
        EstudanteDisciplinaDBDAO estudanteDisciplinaDAO = new EstudanteDisciplinaDBDAO();
        estudanteDisciplinaDAO.insere(estudanteDisciplina);

        System.out.println("Lista todas as rela��es entre estudante e disciplina:");
        System.out.println(estudanteDisciplinaDAO.listaTodos());
    }
}
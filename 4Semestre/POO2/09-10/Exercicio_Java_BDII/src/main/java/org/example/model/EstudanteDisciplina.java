package org.example.model;

public class EstudanteDisciplina {
    private Estudante estudante;
    private Disciplina disciplina;

    public EstudanteDisciplina(){
        estudante = new Estudante();
        disciplina = new Disciplina();
    }

    public EstudanteDisciplina(Estudante academico, Disciplina materia){
        estudante = academico;
        disciplina = materia;
    }


    public Disciplina getDisciplina() {
        return disciplina;
    }

    public Estudante getEstudante() {
        return estudante;
    }

    public void setDisciplina(Disciplina disciplina) {
        this.disciplina = disciplina;
    }

    public void setEstudante(Estudante estudante) {
        this.estudante = estudante;
    }

    @Override
    public String toString() {
        return "EstudanteDisciplina{" +
                "estudante=" + estudante +
                ", disciplina=" + disciplina +
                '}';
    }
}

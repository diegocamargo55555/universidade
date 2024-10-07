package org.example.model;

public class Disciplina {
    private int disciplinaID;
    private String nome;

    public Disciplina(){

    }
    public Disciplina(int id , String name){
        disciplinaID = id;
        nome = name;
    }

    public int getDisciplinaID() {
        return disciplinaID;
    }

    public void setDisciplinaID(int disciplinaID) {
        this.disciplinaID = disciplinaID;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Disciplina{" +
                "disciplina=" + disciplinaID +
                ", nome='" + nome + '\'' +
                '}';
    }
}

package org.example.model;

public class Disciplina {
    private int disciplina;
    private String nome;

    public Disciplina(){
        disciplina = 0;
        nome = "default";
    }

    public Disciplina(int id, String name){
        disciplina = id;
        nome = name;
    }

    public String getNome() {
        return nome;
    }

    public int getDisciplina() {
        return disciplina;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setDisciplina(int disciplina) {
        this.disciplina = disciplina;
    }

    @Override
    public String toString() {
        return "Disciplina{" +
                "disciplina=" + disciplina +
                ", nome='" + nome + '\'' +
                '}';
    }
}

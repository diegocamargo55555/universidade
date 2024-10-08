package org.example.model;

public class Disciplina {
    private int disciplinaId;
    private String nome;
    public Disciplina() {

    }
    public Disciplina(int disciplinaId, String nome) {
        this.disciplinaId = disciplinaId;
        this.nome = nome;
    }
    public int getDisciplinaId() {
        return disciplinaId;
    }
    public void setDisciplinaId(int disciplinaId) {
        this.disciplinaId = disciplinaId;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    @Override
    public String toString() {
        return "Id: " + disciplinaId + ", Nome: " + nome;
    }
}

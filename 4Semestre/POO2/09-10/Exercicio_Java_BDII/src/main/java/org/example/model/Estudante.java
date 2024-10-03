package org.example.model;

public class Estudante {
    private int estudanteID;
    private String nome;
    private int idade;

    public Estudante(int age, int id, String name){
        estudanteID = id;
        nome = name;
        idade = age;
    }

    public Estudante(){
        estudanteID = 0;
        nome = "default";
        idade = 0;
    }


    public int getEstudanteID() {
        return estudanteID;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setEstudanteID(int estudanteID) {
        this.estudanteID = estudanteID;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Estudante{" +
                "estudanteID=" + estudanteID +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}


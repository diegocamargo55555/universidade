import Endereco from "./Endereco";
import Telefone from "./Telefone";

export default class Cliente{
    private _nome: string;
    private _cpf: number
    private _data_nascimento: number
    private _sexo: string
    private _endereco: Endereco
    private _telefones: Telefone[]
    
    constructor(nome : string, cpf : number, data_nascimento : number, sexo : string, endereco : Endereco, telefones : Telefone[]){
        this._nome = nome
        this._cpf = cpf
        this._data_nascimento = data_nascimento
        this._sexo = sexo
        this._endereco = endereco
        this._telefones = telefones
    }
    public get nome() : string {
        return this._nome
    }
    public get cpf() : number {
        return this._cpf
    }
    public get data_nascimento() : number {
        return this._data_nascimento
    }
    public get sexo() : string {
        return  this._sexo
    }
    public get endereco() : Endereco {
        return this._endereco
    }
    public get telefone() : Telefone[] {
        return this._telefones
    }
    
    public set nome(nome : string) {
        this._nome = nome;
    }
    
    public set cpf(cpf : number) {
        this._cpf = cpf;
    }
    
    public set data_nascimento(data_nascimento : number) {
        this._data_nascimento = data_nascimento;
    }
    
    public set sexo(sexo : string) {
        this._sexo = sexo;
    }
    
    
    public set endereco(endereco : Endereco) {
        this._endereco = endereco;
    }
    
    public set telefone(telefone : Telefone[]) {
        this._telefones = telefone;
    }
    
}
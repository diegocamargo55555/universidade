import Cliente from "./Client";
import Produtos from "./Produto";


export default class Venda{
    private _codigo: number
    private _data: number
    private _cliente: Cliente
    private _produtos: Produtos[]
    
    constructor(codigo: number, data: number, cliente: Cliente, produto:Produtos[]){
        this._cliente = cliente
        this._codigo = codigo
        this._data = data
        this._produtos = produto
    }
    public get codigo() : number {
        return this._codigo
    }
    
    public get data() : number {
        return this._data
    }
    
    public get cliente() : Cliente {
        return this._cliente
    }
    
    public get produtos() : Produtos[] {
        return this.produtos
    }
    
    public set cliente(cliente : Cliente) {
        this._cliente = cliente;
    }
    
    public set produtos(produtos : Produtos[]) {
        this._produtos = produtos;
    }
    
    public set data(data : number) {
        this._data = data;
    }
    
    public set codigo(codigo : number) {
        this._codigo = codigo;
    }
    

    public calcularTotal() : number {
        var total = 0
        for (let i = 0; i < this._produtos.length; i++) {
            total = this._produtos[i].valor
        }
        return total
    }
    
    
    
    
    
    
}
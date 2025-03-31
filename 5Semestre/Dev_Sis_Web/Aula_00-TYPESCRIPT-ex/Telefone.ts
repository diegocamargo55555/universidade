export default class Telefone{
    private _ddd: string
    private _numero: number
    private _tipo:string
    
    constructor(ddd : string, number : number, tipo : string){
        this._ddd = ddd
        this._numero = number
        this._tipo = tipo
    }
    
}

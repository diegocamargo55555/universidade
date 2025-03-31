export default class Endereco{
    private _rua: string
    private _numero: number
    private _cidade: string
    private _estado: string
    
    constructor(rua : string, numero : number, cidade : string, estado : string){
        this._cidade = cidade
        this._estado = estado
        this._numero = numero
        this._rua = rua
    }
}


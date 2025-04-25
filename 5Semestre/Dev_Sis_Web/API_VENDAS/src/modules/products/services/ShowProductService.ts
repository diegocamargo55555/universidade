import { getCustomRepository } from "typeorm";
import Product  from "../typeorm/entities/Product";
import ProductsRepository from "../typeorm/repositories/ProductsRepository";
import AppError from "@shared/errors/AppError";

interface Irequest{
    id: string
}

export default class ShowProductService{
    public async execute({id} : Irequest) : Promise<Product>{
        const productsRepository = getCustomRepository(ProductsRepository);
        const product = await productsRepository.findOne({id});
        if(!product){
            throw new AppError('product not found')
        }
        return product
    }

}
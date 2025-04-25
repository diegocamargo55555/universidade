import { getCustomRepository } from "typeorm";
import Product  from "../typeorm/entities/Product";
import ProductsRepository from "../typeorm/repositories/ProductsRepository";
import AppError from "@shared/errors/AppError";

interface Irequest{
    name: string
    price: number
    quantity: number
}

export default class CreateProductService{
    public async execute({name, price, quantity} : Irequest) : Promise<Product>{
        const productsRepository = getCustomRepository(ProductsRepository);
        const productExists = await productsRepository.findByName(name);
        if (productExists){
            throw new AppError('there is already one product with this name')
        }
        const product = productsRepository.create({name, price, quantity});
        await productsRepository.save(product)
        return product
    }

}
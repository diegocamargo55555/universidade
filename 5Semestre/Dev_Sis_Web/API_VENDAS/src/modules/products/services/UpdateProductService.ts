import { getCustomRepository } from "typeorm";
import Product  from "../typeorm/entities/Product";
import ProductsRepository from "../typeorm/repositories/ProductsRepository";
import AppError from "@shared/errors/AppError";

interface Irequest{
    id: string
    name: string
    price: number
    quantity: number
}

export default class UpdateProductService{
    public async execute({id, name, price, quantity} : Irequest) : Promise<Product>{
        const productsRepository = getCustomRepository(ProductsRepository);
        const product = await productsRepository.findOne({id});
        if(!product){
            throw new AppError('product not found')
        }

        const productExists = await productsRepository.findByName(name);
        if (productExists && name != product.name){
            throw new AppError('there is already one product with this name')
        }
        product.name = name
        product.price = price
        product.quantity = quantity
        await productsRepository.save(product)
        return product
    }
}
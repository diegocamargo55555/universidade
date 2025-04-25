import { getCustomRepository } from "typeorm";
import Product  from "../typeorm/entities/Product";
import ProductsRepository from "../typeorm/repositories/ProductsRepository";

export default class ListProductService{
    public async execute() : Promise<Product[]>{
        const productsRepository = getCustomRepository(ProductsRepository);
        const product = await productsRepository.find()
        await productsRepository.save(product)
        return product
    }

}
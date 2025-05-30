import { Entity, EntityRepository, In, Repository } from "typeorm";
import Product from "../entities/Product";

interface IfindProducts {
    id: string
}

@EntityRepository(Product)
export default class ProductsRepository extends Repository<Product> {
    public async findByName(name: string): Promise<Product | undefined> {
        const Product = this.findOne({ where: { name } });
        return Product;
    }

    public async findAllByIds(products: IfindProducts[]): Promise<Product[]> {
        const productsIds = products.map(product => product.id)
        const existProducts = await this.find({ where: { id: In(productsIds) } })
        return existProducts
    }
}
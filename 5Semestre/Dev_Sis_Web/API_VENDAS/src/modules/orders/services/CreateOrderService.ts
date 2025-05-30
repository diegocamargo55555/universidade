import { getCustomRepository } from "typeorm"
import OrdersRepository from "../typeorm/repositories/OrdersRepository"
import Order from "../typeorm/entities/Order"
import CustomersRepository from "@modules/customers/typeorm/repositories/CustomersRepository"
import ProductsRepository from "@modules/products/typeorm/repositories/ProductsRepository"
import AppError from "@shared/errors/AppError"

interface IProduct {
    id: string
    quantity: number
}


interface IRequest {
    customer_id: string
    products: IProduct[]
}

export default class CreateOrderService {
    public async execute({ customer_id, products }: IRequest): Promise<Order> {
        const orderRepository = getCustomRepository(OrdersRepository)
        const customerRepository = getCustomRepository(CustomersRepository)
        const productRepository = getCustomRepository(ProductsRepository)

        const customerExist = await customerRepository.findById(customer_id)
        if (!customerExist) {
            throw new AppError("Could not find any customer with the given id.")
        }

        const productsExist = await productRepository.findAllByIds(products)
        if (!productsExist.length) {
            throw new AppError("Could not find any products with the given ids.")
        }

        const existProductsIds = productsExist.map((product) => product.id)
        const checkInexistentsProducts = products.filter(
            product => !existProductsIds.includes(product.id))
        if (!checkInexistentsProducts.length) {
            throw new AppError(`Could not find ${checkInexistentsProducts[0].id}`)
        }

        const quantityAvaliable = products.filter(
            product => productsExist.filter(
                prod => prod.id === product.id)[0].quantity < product.quantity)
        if (quantityAvaliable.length) {
            throw new AppError(`the quantity ${quantityAvaliable[0].quantity} 
                di not avaliable for ${quantityAvaliable[0].id} `)

        }

        const serializarProducts = products.map(product => ({
            product_id: product.id,
            quantity: product.quantity,
            price: productsExist.filter(prod => prod.id === product.id)[0].price
        }))

        const order = await orderRepository.createOrder({
            customer: customerExist,
            products: serializarProducts
        })

        const { orders_products } = order
        const updateProductQuantity = orders_products.map(product => ({
            id: product.product_id,
            quantity: productsExist
                .filter(p => p.id === product.product_id)[0].quantity - product.quantity
        }))
        await productRepository.save(updateProductQuantity)
        return order
    }
}
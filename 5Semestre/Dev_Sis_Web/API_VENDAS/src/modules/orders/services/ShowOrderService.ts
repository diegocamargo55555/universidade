import { getCustomRepository } from "typeorm";
import AppError from "@shared/errors/AppError";
import Order from "../typeorm/entities/Order";
import OrdersRepository from "../typeorm/repositories/OrdersRepository";

interface Irequest {
    id: string
}

export default class ShowOrdertService {
    public async execute({ id }: Irequest): Promise<Order> {
        const ordersRepository = getCustomRepository(OrdersRepository);
        const order = await ordersRepository.findOne({ id });
        if (!order) {
            throw new AppError('order not found')
        }
        return order
    }

}
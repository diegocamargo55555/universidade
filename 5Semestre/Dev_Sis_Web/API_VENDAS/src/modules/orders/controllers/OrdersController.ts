import { NextFunction, Request, response, Response } from "express";
import CreateOrderService from "../services/CreateOrderService";
import ShowOrdertService from "../services/ShowOrderService";
import ListCustomerService from "@modules/customers/service/ListCustomerService";

export default class OrdersController {
    public async index(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const listOrder = new ListCustomerService();
            const products = await listOrder.execute();
            return response.json(products);
        } catch (err) {
            next(err);
        }
    }


    public async show(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { id } = request.params;
            const showOrder = new ShowOrdertService();
            const order = await showOrder.execute({ id });
            return response.json(order);
        } catch (err) {
            next(err);
        }
    }

    public async create(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { customer_id, products } = request.body;
            const createOrder = new CreateOrderService();
            const order = await createOrder.execute({ customer_id, products });
            return response.json(order);
        } catch (err) {
            next(err);
        }
    }

}
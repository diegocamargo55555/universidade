import { getCustomRepository } from "typeorm";
import Customer from "../typeorm/entities/Customer";
import CustomersRepository from "../typeorm/repositories/CustomersRepository";
import AppError from "src/shared/errors/AppError";


export default class ListCustomerService{
    public async execute(): Promise<Customer[]>{
        const customerRepository = getCustomRepository(CustomersRepository);
        const customers = await customerRepository.find();
        return customers;
    }
}


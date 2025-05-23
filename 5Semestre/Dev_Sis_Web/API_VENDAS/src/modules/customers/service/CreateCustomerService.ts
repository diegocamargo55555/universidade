import { getCustomRepository } from "typeorm";
import Customer from "../typeorm/entities/Customer";
import CustomerRepository from "../typeorm/repositories/CustomersRepository";
import AppError from "src/shared/errors/AppError";
import { hash } from "bcryptjs";

interface IRequest {
    name: string;
    email: string;
}
export default class CreateCustomerService {
    public async execute({ name, email, }: IRequest): Promise<Customer> {
        const customerRepository = getCustomRepository(CustomerRepository);
        const emailsExists = await customerRepository.findByEmail(email);
        if (emailsExists) {
            throw new AppError('Email adress already used');
        }
        //const hashedpassPassword = await hash(password, 8)
        const customer = customerRepository.create({ name, email });
        await customerRepository.save(customer);
        return customer;
    }
}
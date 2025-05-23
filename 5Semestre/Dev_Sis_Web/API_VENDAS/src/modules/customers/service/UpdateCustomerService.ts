import { getCustomRepository } from "typeorm";
import Customer from "../typeorm/entities/Customer";
import CustomerRepository from "../typeorm/repositories/CustomersRepository";
import AppError from "src/shared/errors/AppError";
import { hash } from "bcryptjs";

interface IRequest {
    id: string;
    name: string;
    email: string;
}
export default class UpdateCustomerService {
    public async execute({id, name, email }: IRequest): Promise<Customer> {
        const customerRepository = getCustomRepository(CustomerRepository);
        const customer = await customerRepository.findById(id);
        if (!customer) {
            throw new AppError('Email adress already used');
        }
        const customerExists = await customerRepository.findByEmail(email)
        if (customerExists && email !== customer.email) {
                throw new AppError(" email alredy used")
        }
        customer.name = name
        customer.email = email
        //const hashedpassPassword = await hash(password, 8)
        await customerRepository.save(customer);
        return customer;
    }
}


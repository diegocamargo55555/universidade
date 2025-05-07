import { getCustomRepository } from "typeorm";
import User from "../typeorm/entities/User";
import UsersRepository from "../typeorm/repositories/UsersRepository";
import AppError from "src/shared/errors/AppError";
import { hash } from "bcryptjs";

interface IRequest{
    name: string;
    email: string;
    password: string;
}
export default class CreateUserService{
    public async execute({name, email, password}: IRequest): Promise<User>{
        const userRepository = getCustomRepository(UsersRepository);
        const emailsExists = await userRepository.findByEmail(email);
        if(emailsExists){
            throw new AppError('Email adress already used');
        }
        const hashedpassPassword = await hash(password, 8)
        const user = userRepository.create({name,email,password:hashedpassPassword});
        await userRepository.save(user);
        return user;
    }
}
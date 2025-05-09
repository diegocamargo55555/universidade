import { getCustomRepository } from "typeorm";
import User from "../typeorm/entities/User";
import UsersRepository from "../typeorm/repositories/UsersRepository";
import AppError from "src/shared/errors/AppError";


export default class ListUserService{
    public async execute(): Promise<User[]>{
        const userRepository = getCustomRepository(UsersRepository);
        const users = await userRepository.find();
        return users;
    }
}


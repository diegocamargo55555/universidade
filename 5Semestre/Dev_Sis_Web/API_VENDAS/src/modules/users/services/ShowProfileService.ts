import { getCustomRepository } from "typeorm";
import User from "../typeorm/entities/User";
import UsersRepository from "../typeorm/repositories/UsersRepository";
import AppError from "src/shared/errors/AppError";

interface Irequest{
    user_id: string
}

export default class ShowProfileService{
    public async execute({user_id} : Irequest): Promise<User>{
        const userRepository = getCustomRepository(UsersRepository);
        const user = await userRepository.findById(user_id);
        if(!user){
            throw new AppError('User not found')
        }
        return user;
    }
}


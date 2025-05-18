import { getCustomRepository } from "typeorm"
import UserRepository from "../typeorm/repositories/UsersRepository"
import UsersTokensRepository from "../typeorm/repositories/UsersTokensRepository"
import AppError from "@shared/errors/AppError"
import { addHours, isAfter } from "date-fns"
import { hash } from "bcryptjs"

interface IRequest {
    token: string
    password: string
}


export default class ResetPasswordService {
    public async execute({token, password }: IRequest): Promise<void> {
        const userRepository = getCustomRepository(UserRepository)
        const UserTokensRepository = getCustomRepository(UsersTokensRepository)
        const userToken = await UserTokensRepository.findByToken(token)

        if (!userToken) {
            throw new AppError('User Token does not exist')
        }


        const user = await userRepository.findById(userToken.user_id)
        if (!user) {
            throw new AppError('User does not exist')
        }


        const tokenCreatedAt = userToken.created_at
        const compareDate = addHours(tokenCreatedAt, 2)
        if (isAfter(Date.now(), compareDate)) {
            throw new AppError('Token expired')           
        }

        user.password = await hash(password, 8)
        await userRepository.save(user)

        console.log(token)
    }
}
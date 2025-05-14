import upload from "@config/upload"
import AppError from "@shared/errors/AppError"
import { getCustomRepository } from "typeorm"
import User from "../typeorm/entities/User"
import UsersRepository from "../typeorm/repositories/UsersRepository"
import path from 'path'
import uploadConfig from '@config/upload'
import fs from 'fs'

interface Irequest {
    user_id: string
    avatarFileName: string
}

export default class UpdateUserAvatarService {
    public async execute({ user_id, avatarFileName, }: Irequest): Promise<User> {
        const usersRepository = getCustomRepository(UsersRepository)
        const user = await usersRepository.findById(user_id)
        if (!user) {
            throw new AppError("User not found ")
        }
        if (user.avatar) {
            const userAVatarFilePath = path.join(uploadConfig.directory, user.avatar);
            const userAVatarFileExists = await fs.promises.stat(userAVatarFilePath);
            if (userAVatarFileExists) {
                await fs.promises.unlink(userAVatarFilePath);
            }
        }
        user.avatar = avatarFileName;
        await usersRepository.save(user);
        return user;
    }
}    
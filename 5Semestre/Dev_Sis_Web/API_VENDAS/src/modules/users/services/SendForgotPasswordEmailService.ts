import { getCustomRepository } from "typeorm";
import UserRepository from "../typeorm/repositories/UsersRepository";
import UsersTokensRepository from "../typeorm/repositories/UsersTokensRepository";
import AppError from "src/shared/errors/AppError";
import EtherealMail from "@config/mail/EtherealMail";

interface IRequest{
    email: string;
}

export default class SendForgotPasswordEmailServise{
    public async execute({email} : IRequest) : Promise<void>{
        const userRepository = getCustomRepository(UserRepository);
        const userTokenRepository = getCustomRepository(UsersTokensRepository);
        const user = await userRepository.findByEmail(email);
        if(!user){
            throw new AppError('User does not exist.');
        }
        const {token} = await userTokenRepository.createToken(user.id);
        //implementação do envio do token
        console.log(token);
        await EtherealMail.sendMail({
            to: email,
            body: `Solicitação de recuperação de senha recebida: ${token}`,
        });
    }
}
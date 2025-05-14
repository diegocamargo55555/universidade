import { EntityRepository, Repository } from "typeorm";
import UserTokens from "../entities/UserTokens";

@EntityRepository(UserTokens)
export default class UsersTokensRepository extends Repository<UserTokens> {
    public async findByToken(token: string): Promise<UserTokens | undefined> {
        const userToken = await this.findOne({ where: token })
        return userToken
    }

    public async createToken(user_id: string): Promise<UserTokens | undefined> {
        const userToken = await this.create({ user_id })
        return userToken
    }

}
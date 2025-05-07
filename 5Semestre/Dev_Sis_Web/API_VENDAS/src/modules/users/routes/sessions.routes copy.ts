import { Router } from "express";
import SessionRouter from "../Controllers/SessionsController"
import { celebrate, Joi, Segments } from "celebrate";

const sessionRouter = Router()
const sessionController = new SessionRouter();

sessionRouter.post('/', celebrate({
    [Segments.BODY] : {
        email: Joi.string().email().required(),
        password: Joi.string().required()
    }
}),
async(req, res, next) =>{
    try{
        await sessionController.create(req, res, next)
    }catch(err){
        next(err)
    }
} )

export default sessionRouter
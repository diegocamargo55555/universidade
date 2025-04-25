import { Router } from "express";
import ProductsController from "../Controllers/ProductesControllers";
import { celebrate, Joi, Segments } from 'celebrate';

const productsRouter = Router();
const productsController = new ProductsController();

productsRouter.get('/', async (req, res, next) => {
    try {
        console.log("1")
        await productsController.index(req, res, next)
    } catch (err) {
        next(err)
    }
})

productsRouter.get('/:id', async (req, res, next) => {
    console.log("2")
    try {
        await productsController.show(req, res, next)
    } catch (err) {
        next(err)
    }
})

productsRouter.post('/', async (req, res, next) => {
    console.log("3")
    try {
        await productsController.create(req, res, next)
    } catch (err) {
        next(err)
    }
})

productsRouter.put('/:id', async (req, res, next) => {
    console.log("4")

    try {
        await productsController.update(req, res, next)
    } catch (err) {
        next(err)
    }
})


productsRouter.delete('/:id', async (req, res, next) => {
    console.log("5")

    try {
        await productsController.delete(req, res, next)
    } catch (err) {
        next(err)
    }
})

productsRouter.get('/:id', celebrate({
    [Segments.PARAMS] : {id: Joi.string().uuid().required()}
  }),
  async (req, res, next) => {
    try {
      await productsController.show(req, res, next);
    } catch (err) {
      next(err);
    }
  });
  

export default productsRouter
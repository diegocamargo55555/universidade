import productsRouter from "@modules/products/routes/products.routes";
import { Router } from "express";
const routes = Router();
console.log("65")

routes.use('/products', productsRouter);

export default routes;
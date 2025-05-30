import { Column, CreateDateColumn, Entity, JoinColumn, ManyToMany, ManyToOne, OneToMany, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";
import Order from "./Order"
import Product from "@modules/products/typeorm/entities/Product";
@Entity('orders_products')
export default class OrdersProducts {
    @PrimaryGeneratedColumn('uuid')
    id: string

    @ManyToOne(() => Order, order => order.orders_products)
    @JoinColumn({ name: "customer_id" })
    order: Order

    @ManyToOne(() => Product, product => product.orders_products)
    @JoinColumn({ name: "product_id" })
    product: Product

    @Column()
    order_id: string

    @Column()
    product_id: string

    @Column('decimal')
    price: number

    @Column('int')
    quantity: number

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;

}
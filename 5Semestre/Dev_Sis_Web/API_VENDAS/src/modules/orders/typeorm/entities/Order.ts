import Customer from "@modules/customers/typeorm/entities/Customer";
import { CreateDateColumn, Entity, JoinColumn, ManyToMany, ManyToOne, OneToMany, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";
import OrderProducts from "./OrdersProducts";

@Entity('orders')
export default class Order {
    @PrimaryGeneratedColumn('uuid')
    id: string

    @ManyToOne(() => Customer)
    @JoinColumn({ name: "customer_id" })
    customer: Customer

//    @OneToMany(() => OrdersProducts, orders_products => orders_products.order, { cascade: true })
//    orders_products: OrdersProducts[]

    @OneToMany(() => OrderProducts, orders_products => orders_products.order, {
        cascade: true,
    })
    orders_products: OrderProducts[];

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;
    order_products: any;

}
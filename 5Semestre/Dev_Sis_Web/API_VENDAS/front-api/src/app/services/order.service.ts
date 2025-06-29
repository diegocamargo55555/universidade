import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Variables } from '../config/variables';
import Customer from '../model/customer';
import { AuthService } from './auth.service';
import Order from '../model/order';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  private apiURL: string = Variables.apiURL

  constructor(private http: HttpClient,
    private authService: AuthService) { }

  private getAuthHeaders(): HttpHeaders {
    const token = this.authService.getToken()
    return new HttpHeaders().set('Authorization', `Bearer ${token}`)
  }

  getAllOrder(): Observable<Order[]> {
    return this.http.get<Order[]>(`${this.apiURL}/order`,
      { headers: this.getAuthHeaders() })
  }

  getOrderById(id: string): Observable<Order> {
    return this.http.get<Order>(`${this.apiURL}/order/${id}`,
      { headers: this.getAuthHeaders() })
  }

  createOrder(order: Order): Observable<Order> {
    return this.http.post<Order>(`${this.apiURL}/order/`, order,
      { headers: this.getAuthHeaders() })
  }
}

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Variables } from '../config/variables';
import { AuthService } from './auth.service';
import Customer from '../model/customer';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {
  private apiURL: string = Variables.apiURL

  constructor(private http: HttpClient,
    private authService: AuthService) { }

  private getAuthHeaders(): HttpHeaders {
    const token = this.authService.getToken()
    return new HttpHeaders().set('Authorization', `Bearer ${token}`)
  }

  getAllCustomers(): Observable<Customer[]> {
    return this.http.get<Customer[]>(`${this.apiURL}/customer`,
      { headers: this.getAuthHeaders() })
  }

  getCustomerById(id: string): Observable<Customer> {
    return this.http.get<Customer>(`${this.apiURL}/customer/${id}`,
      { headers: this.getAuthHeaders() })
  }

  addCustomer(customer: Customer): Observable<Customer> {
    return this.http.post<Customer>(`${this.apiURL}/customer/`, customer,
      { headers: this.getAuthHeaders() })
  }

  updateCustomer(id: string, customer: Customer): Observable<Customer> {
    return this.http.put<Customer>(`${this.apiURL}/customer/${id}`, customer,
      { headers: this.getAuthHeaders() })
  }

  deleteCustomer(id: string): Observable<void> {
    return this.http.delete<void>(`${this.apiURL}/customer/${id}`,
      { headers: this.getAuthHeaders() })
  }
}

import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { PaymentMethods } from "../domain/payment-methods";
import { environment } from "../../environment";

@Injectable({
  providedIn: 'root'
})
export class PaymentMethodsService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getPaymentMethods(): Observable<PaymentMethods> {
    return this.http.get<PaymentMethods>(`${this.baseUrl}/payment-methods`);
  }
}

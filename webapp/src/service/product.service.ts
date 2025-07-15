import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Product } from "../domain/product";
import { environment } from "../../environment";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getProductById(productId: string): Observable<Product> {
    return this.http.get<Product>(`${this.baseUrl}/items/${productId}`);
  }
}

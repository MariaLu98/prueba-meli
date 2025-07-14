import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { RecommendedProduct } from "../domain/related-product";
import { environment } from "../../environment";

@Injectable({
  providedIn: 'root'
})
export class RelatedProductsService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getRelatedProducts(): Observable<RecommendedProduct[]> {
    return this.http.get<RecommendedProduct[]>(`${this.baseUrl}/related-products`);
  }
}

import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RecommendedProduct } from '../../../../domain/related-product';
import { RecommendedProductsService } from '../../../../service/recommended-products.service';

@Component({
  selector: 'app-products-list',
  imports: [CommonModule],
  templateUrl: './products-list.component.html',
  styleUrl: './products-list.component.css'
})
export class ProductsListComponent implements OnInit {
  recommendedProducts: RecommendedProduct[] = [];

  constructor(private recommendedService: RecommendedProductsService) {}

  ngOnInit() {
    this.recommendedService.getRecommendedProducts().subscribe(data => {
      this.recommendedProducts = data;
    });
  }
   onImgError(event: Event) {
  (event.target as HTMLImageElement).src = '';
}
}
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { CarouselModule } from 'primeng/carousel';
import { RecommendedProduct } from '../../../../domain/related-product';
import { RecommendedProductsService } from '../../../../service/recommended-products.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-recommended-products',
  imports: [    CommonModule,
    CarouselModule,
    ButtonModule,
    FormsModule,
  HttpClientModule ],
  templateUrl: './recommended-products.component.html',
  styleUrl: './recommended-products.component.css'
})
export class RecommendedProductsComponent  implements OnInit {
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

import { Component, OnInit } from '@angular/core';
import { CarouselModule } from 'primeng/carousel';
import { CardModule } from 'primeng/card';
import { ButtonModule } from 'primeng/button';
import { CommonModule, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RecommendedProduct } from '../../../../domain/related-product';
import { RelatedProductsService } from '../../../../service/related-products.service';

@Component({
  selector: 'app-related-products',
  standalone: true,
  imports: [    CommonModule,
    CarouselModule,
    ButtonModule,
    FormsModule],
  templateUrl: './related-products.component.html',
  styleUrls: ['./related-products.component.css']
})
export class RelatedProductsComponent implements OnInit {
  relatedProducts: RecommendedProduct[] = [];

  constructor(private relatedService: RelatedProductsService) {}

  ngOnInit() {
    this.relatedService.getRelatedProducts().subscribe(data => {
      this.relatedProducts = data;
    });
  }
   onImgError(event: Event) {
  (event.target as HTMLImageElement).src = '';
}
}
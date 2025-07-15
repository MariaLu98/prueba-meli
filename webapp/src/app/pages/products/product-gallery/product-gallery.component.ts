import { Component, OnInit } from '@angular/core';
import { GalleriaModule } from 'primeng/galleria';
import { CommonModule, NgFor } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../../../../domain/product';
import { ProductService } from '../../../../service/product.service';

@Component({
  selector: 'app-product-gallery',
  standalone: true,
  imports: [GalleriaModule, CommonModule],
  templateUrl: './product-gallery.component.html',
  styles: './product-gallery.component.css',
})
export class ProductGalleryComponent  implements OnInit {
  product?: Product;

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    const productId = this.route.snapshot.paramMap.get('id');
    if (productId) {
      this.productService.getProductById(productId).subscribe(data => {
        this.product = data;
      });
    }
  }
   onImgError(event: Event) {
  (event.target as HTMLImageElement).src = '';
}
}
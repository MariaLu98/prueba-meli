import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../../../../domain/product';
import { ProductService } from '../../../../service/product.service';

@Component({
  selector: 'app-seller-info',
  imports: [CommonModule],
  templateUrl: './seller-info.component.html',
  styleUrl: './seller-info.component.css'
})
export class SellerInfoComponent  implements OnInit {
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
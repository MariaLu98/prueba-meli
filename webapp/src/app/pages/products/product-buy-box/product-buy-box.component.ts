import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { Product } from '../../../../domain/product';
import { ProductService } from '../../../../service/product.service';

@Component({
  selector: 'app-product-buy-box',
  imports: [ CommonModule,
    FormsModule,
    ButtonModule],
  templateUrl: './product-buy-box.component.html',
  styleUrl: './product-buy-box.component.css'
})
export class ProductBuyBoxComponent  implements OnInit {
  product?: Product;
  quantities = [1, 2, 3, 4, 5];

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    const productId = this.route.snapshot.paramMap.get('id');
    debugger;
    if (productId) {
      this.productService.getProductById(productId).subscribe(data => {
        this.product = data;
      });
    }
  }
}
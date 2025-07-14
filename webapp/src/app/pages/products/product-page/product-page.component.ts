import { Component } from '@angular/core';
import { ProductGalleryComponent } from '../product-gallery/product-gallery.component';
import { ProductInfoComponent } from '../product-info/product-info.component';
import { RelatedProductsComponent } from '../related-products/related-products.component';
import { ProductDescriptionComponent } from '../product-description/product-description.component';
import { NgIf } from '@angular/common';
import { CardModule } from 'primeng/card';
import { SellerInfoComponent } from '../seller-info/seller-info.component';
import { RecommendedProductsComponent } from '../recommended-products/recommended-products.component';
import { ProductBuyBoxComponent } from '../product-buy-box/product-buy-box.component';
import { MethodPaymentComponent } from '../method-payment/method-payment.component';
import { ProductsListComponent } from '../products-list/products-list.component';

@Component({
  selector: 'app-product-page',
  standalone: true,
  imports: [
    ProductGalleryComponent,
    ProductInfoComponent,
    RelatedProductsComponent,
    ProductDescriptionComponent,
    NgIf,
    CardModule,
    SellerInfoComponent,
    RecommendedProductsComponent,
    ProductBuyBoxComponent,
    MethodPaymentComponent,
    ProductsListComponent
  ],
  styleUrls: ['./product-page.component.css'],
  templateUrl: './product-page.component.html'
})
export class ProductPageComponent {}

import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-product-buy-box',
  imports: [ CommonModule,
    FormsModule,
    ButtonModule],
  templateUrl: './product-buy-box.component.html',
  styleUrl: './product-buy-box.component.css'
})
export class ProductBuyBoxComponent {
  quantities = [1, 2, 3, 4, 5];
  stock = 50;
  seller = 'Samsung';
  sales = 5000;
}
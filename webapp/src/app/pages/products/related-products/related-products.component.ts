import { Component } from '@angular/core';
import { CarouselModule } from 'primeng/carousel';
import { CardModule } from 'primeng/card';
import { ButtonModule } from 'primeng/button';
import { CommonModule, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';

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
export class RelatedProductsComponent {
  samsungProducts = [
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/sm-s926bzsjlco/gallery/co-galaxy-s24-plus-sm-s926-476988-sm-s926bzsjlco-thumb-538433253?$344_344_PNG$',
    title: 'Samsung Galaxy S25 256 Gb Garantía Oficial',
    priceOld: 1299,
    priceNew: 959,
    discount: 26,
    cuotas: '10 cuotas de $ 4.181,24 sin interés',
    envioGratis: true
  },
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/sm-s928bzvjlco/gallery/co-galaxy-s24-ultra-sm-s928-476989-sm-s928bzvjlco-thumb-538433255?$344_344_PNG$',
    title: 'Samsung Galaxy S25 Plus 512 Gb Garantía Oficial',
    priceOld: 1699,
    priceNew: 1379,
    discount: 18,
    cuotas: '10 cuotas de $ 6.012,44 sin interés',
    envioGratis: true
  }
];

}

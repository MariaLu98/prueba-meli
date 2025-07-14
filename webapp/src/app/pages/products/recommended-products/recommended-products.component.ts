import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { CarouselModule } from 'primeng/carousel';

@Component({
  selector: 'app-recommended-products',
  imports: [    CommonModule,
    CarouselModule,
    ButtonModule,
    FormsModule ],
  templateUrl: './recommended-products.component.html',
  styleUrl: './recommended-products.component.css'
})
export class RecommendedProductsComponent {
relatedProducts = [
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/sm-a546ezkveco/gallery/co-galaxy-a54-5g-sm-a546-464889-sm-a546ezkveco-thumb-534035492?$344_344_PNG$',
    title: 'Samsung Galaxy A54 5G 128GB',
    priceOld: 499,
    priceNew: 439,
    discount: 12,
    cuotas: 'en 10 cuotas de $ 1.914 sin interés',
    envioGratis: true
  },
  {
    image: 'https://motorolaus.vtexassets.com/arquivos/ids/162412/motorola-edge-50-pro-mx-pdp-render-nimbus-1.jpg?v=638490728605730000',
    title: 'Motorola Edge 50 Pro 256GB Azul',
    priceOld: 469,
    priceNew: 419,
    discount: 11,
    cuotas: 'en 10 cuotas de $ 1.826 sin interés',
    envioGratis: true
  },
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/sm-a146mzkeco/sm-a146mzkeco-gallery-001-534083421?$344_344_PNG$',
    title: 'Samsung Galaxy A14 5G 128GB',
    priceOld: 336,
    priceNew: 326,
    discount: 3,
    cuotas: 'en 10 cuotas de $ 1.424 sin interés',
    envioGratis: true
  }
];



}

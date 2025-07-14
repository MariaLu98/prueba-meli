import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-products-list',
  imports: [CommonModule],
  templateUrl: './products-list.component.html',
  styleUrl: './products-list.component.css'
})
export class ProductsListComponent {
relatedProducts = [
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/2303/gallery/co-galaxy-a54-5g-sm-a546-sm-a546ezgveco-thumb-534035492?$344_344_PNG$',
    title: 'Samsung Galaxy M55 5g 8/256gb Dual Sim',
    priceOld: 485,
    priceNew: 421.95,
    discount: 13,
    cuotas: '10 cuotas de $ 1.839,70 sin interés'
  },
  {
    image: 'https://motorolaus.vtexassets.com/arquivos/ids/162412/motorola-edge-50-pro-mx-pdp-render-nimbus-1.jpg?v=638490728605730000',
    title: 'Motorola Edge 50 Fusion 5g 256 Gb Azul Ártico 8 Gb Ram',
    priceOld: 469,
    priceNew: 419,
    discount: 11,
    cuotas: '10 cuotas de $ 1.826,84 sin interés'
  },
  {
    image: 'https://images.samsung.com/is/image/samsung/p6pim/co/sm-a146mzkeco/sm-a146mzkeco-gallery-001-534083421?$344_344_PNG$',
    title: 'Samsung Galaxy A16 5g 8gb 256gb Negro Tranza',
    priceOld: 336.25,
    priceNew: 326.74,
    discount: 3,
    cuotas: '10 cuotas de $ 1.424,59 sin interés'
  },
  {
    image: 'https://motorolaus.vtexassets.com/arquivos/ids/163325-800-auto?v=638481375153030000&width=800&height=auto&aspect=true',
    title: 'Motorola G85 5g 256gb Gris 8ram',
    priceOld: 365,
    priceNew: 329,
    discount: 10,
    cuotas: '10 cuotas de $ 1.434,44 sin interés'
  }
];

}

import { Component } from '@angular/core';
import { GalleriaModule } from 'primeng/galleria';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-product-gallery',
  standalone: true,
  imports: [GalleriaModule, NgFor],
  templateUrl: './product-gallery.component.html',
  styles: './product-gallery.component.css',
})
export class ProductGalleryComponent {
  images: any[];

  constructor() {
    this.images = [
      {
        itemImageSrc: 'https://picsum.photos/400/800?random=1',
        thumbnailImageSrc: 'https://picsum.photos/100/200?random=1',
        alt: 'Phone Front'
      },
      {
        itemImageSrc: 'https://picsum.photos/400/800?random=2',
        thumbnailImageSrc: 'https://picsum.photos/100/200?random=2',
        alt: 'Phone Back'
      },
      {
        itemImageSrc: 'https://picsum.photos/400/800?random=3',
        thumbnailImageSrc: 'https://picsum.photos/100/200?random=3',
        alt: 'Display Feature'
      },
      {
        itemImageSrc: 'https://picsum.photos/400/800?random=4',
        thumbnailImageSrc: 'https://picsum.photos/100/200?random=4',
        alt: 'Camera Detail'
      },
      {
        itemImageSrc: 'https://picsum.photos/400/800?random=5',
        thumbnailImageSrc: 'https://picsum.photos/100/200?random=5',
        alt: 'Specs Detail'
      }
    ];
  }
  producto = {
  nombre: 'Samsung Galaxy A55 5G Dual SIM 256 GB Azul Oscuro 8 GB RAM',
  precio: 439,
  cuotas: 'en 10 cuotas de $ 1.914 sin interés',
  caracteristicas: [
    'Memoria RAM: 8 GB',
    'Dispositivo desbloqueado para que elijas tu compañía telefónica preferida',
    'Memoria interna de 256 GB'
  ]
};
}
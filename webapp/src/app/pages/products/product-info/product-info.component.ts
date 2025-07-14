import { Component } from '@angular/core';
import { CardModule } from 'primeng/card';
import { ButtonModule } from 'primeng/button';
import { DropdownModule } from 'primeng/dropdown';
import { InputNumberModule } from 'primeng/inputnumber';
import { PanelModule } from 'primeng/panel';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-info',
  standalone: true,
  imports: [
   CommonModule
  ],
  templateUrl: './product-info.component.html',
  styleUrls: ['./product-info.component.css'],
})
export class ProductInfoComponent {
 productFeatures = [
  {
    icon: 'pi pi-mobile',
    label: 'Tamaño de la pantalla',
    value: '6.6"',
    subValue: '(16.11 cm x 7.74 cm x 8.2 mm)',
    hasBar: true
  },
  {
    icon: 'pi pi-database',
    label: 'Memoria interna',
    value: '256 GB'
  },
  {
    icon: 'pi pi-camera',
    label: 'Cámara trasera principal',
    value: '50 Mpx'
  },
  {
    icon: 'pi pi-nfc',
    label: 'Con NFC',
    value: 'Sí'
  },
  {
    icon: 'pi pi-camera',
    label: 'Cámara frontal principal',
    value: '32 Mpx'
  },
  {
    icon: 'pi pi-lock',
    label: 'Desbloqueo',
    value: 'Huella dactilar y reconocimiento facial'
  }
];


}

import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-seller-info',
  imports: [CommonModule],
  templateUrl: './seller-info.component.html',
  styleUrl: './seller-info.component.css'
})
export class SellerInfoComponent {
storeInfo = {
  name: 'Samsung',
  logoUrl: 'https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg',
  official: true,
  products: 50,
  sales: '+5mil',
  indicators: [
    { icon: 'pi pi-check-circle', text: 'Brinda buena atención' },
    { icon: 'pi pi-clock', text: 'Entrega sus productos a tiempo' }
  ],
  storeLink: '#'
};

}

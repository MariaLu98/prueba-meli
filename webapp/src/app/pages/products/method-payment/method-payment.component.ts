import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-method-payment',
  imports: [CommonModule],
  templateUrl: './method-payment.component.html',
  styleUrl: './method-payment.component.css'
})
export class MethodPaymentComponent {
paymentOptions = {
  cuotasMessage: '¡Paga en hasta 12 cuotas sin interés!',
  creditCards: [
    { name: 'Mastercard', logo: 'https://upload.wikimedia.org/wikipedia/commons/0/04/Mastercard-logo.png' },
    { name: 'Visa', logo: 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg' },
    { name: 'OCA', logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/OCA_Logo.svg/512px-OCA_Logo.svg.png' }
  ],
  debitCards: [
    { name: 'Visa Débito', logo: 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg' },
    { name: 'Mastercard Débito', logo: 'https://upload.wikimedia.org/wikipedia/commons/0/04/Mastercard-logo.png' }
  ],
  cash: [
    { name: 'Abitab', logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_Abitab.png/320px-Logo_Abitab.png' },
    { name: 'RedPagos', logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Logo_Redpagos.svg/320px-Logo_Redpagos.svg.png' }
  ]
};

}

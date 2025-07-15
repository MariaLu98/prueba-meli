import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { PaymentMethods } from '../../../../domain/payment-methods';
import { PaymentMethodsService } from '../../../../service/payment-methods.service';

@Component({
  selector: 'app-method-payment',
  imports: [CommonModule],
  templateUrl: './method-payment.component.html',
  styleUrl: './method-payment.component.css'
})
export class MethodPaymentComponent implements OnInit {
  paymentOptions?: PaymentMethods;

  constructor(private paymentService: PaymentMethodsService) {}

  ngOnInit() {
    this.paymentService.getPaymentMethods().subscribe(data => {
      this.paymentOptions = data;
    });
  }
  onImgError(event: Event) {
  (event.target as HTMLImageElement).src = '';
}
}
export interface Card {
  name: string;
  logo: string;
}

export interface PaymentMethods {
  cuotasMessage: string;
  creditCards: Card[];
  debitCards: Card[];
  cash: Card[];
}

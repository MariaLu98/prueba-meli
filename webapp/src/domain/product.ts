export interface Seller {
  name: string;
  logoUrl: string;
  official: boolean;
  products: number;
  sales: string;
  indicators: { icon: string; text: string }[];
  storeLink: string;
}

export interface Features {
  icon: string;
  label: string;
  value: string;
  subValue?: string;
  hasBar?: boolean;
}

export interface Product {
  id: string;
  title: string;
  price: number;
  discount_percentage: number;
  installments: string;
  images: any[];
  color: string;
  stock: number;
  description: string;
  seller: Seller;
  payment_methods: any;
  features: Features[];
}

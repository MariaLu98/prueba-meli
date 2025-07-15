import { Routes } from '@angular/router';
import { ProductPageComponent } from './pages/products/product-page/product-page.component';

export const routes: Routes = [
  {
    path: '',
    redirectTo: '/product/samsung-a55-5g',
    pathMatch: 'full'
  },
  {
    path: 'product/:id',
    component: ProductPageComponent
  },
  {
    path: '**',
    redirectTo: '/product/samsung-a55-5g'
  }
];

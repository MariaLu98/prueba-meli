import { Routes } from '@angular/router';
import { ProductPageComponent } from './pages/products/product-page/product-page.component';

export const routes: Routes = [
  {
    path: '',
    redirectTo: '/product/1',
    pathMatch: 'full'
  },
  {
    path: 'product/:id',
    component: ProductPageComponent
  },
  {
    path: '**',
    redirectTo: '/product/1'
  }
];

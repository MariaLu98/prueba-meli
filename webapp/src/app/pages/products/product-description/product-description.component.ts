import { Component } from '@angular/core';
import { PanelModule } from 'primeng/panel';

@Component({
  selector: 'app-product-description',
  standalone: true,
  imports: [PanelModule],
  templateUrl: './product-description.component.html'
})
export class ProductDescriptionComponent {}

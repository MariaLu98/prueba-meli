import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../../../../domain/product';
import { ProductService } from '../../../../service/product.service';

interface GalleryImage {
  itemImageSrc: string;
  thumbnailImageSrc: string;
  alt: string;
}

@Component({
  selector: 'app-product-gallery',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-gallery.component.html',
  styleUrl: './product-gallery.component.css',
})
export class ProductGalleryComponent implements OnInit {
  product?: Product;
  galleryImages: GalleryImage[] = [];
  defaultImagePath = '/assets/default-image.jpg';
  numVisible = 1;
  currentImageIndex = 0;

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    console.log('🔥 COMPONENT INIT - Starting...');
    const productId = this.route.snapshot.paramMap.get('id');
    console.log('🔍 Product ID:', productId);
    
    if (productId) {
      this.productService.getProductById(productId).subscribe(data => {
        this.product = data;
        console.log('📦 Product loaded:', this.product);
        console.log('🖼️ Product images:', this.product?.images);
        this.prepareGalleryImages();
        console.log('🎠 Gallery images prepared:', this.galleryImages);
        console.log('📍 Current index:', this.currentImageIndex);
      });
    } else {
      console.error('❌ No product ID found in route');
    }
  }

  private prepareGalleryImages() {
    if (this.product?.images && Array.isArray(this.product.images) && this.product.images.length > 0) {
      this.galleryImages = this.product.images.map((imageUrl: string, index: number) => ({
        itemImageSrc: imageUrl || this.defaultImagePath,
        thumbnailImageSrc: imageUrl || this.defaultImagePath,
        alt: `${this.product?.title || 'Producto'} - Imagen ${index + 1}`
      }));
    } else {
      // Si no hay imágenes, usar imagen por defecto
      this.galleryImages = [{
        itemImageSrc: this.defaultImagePath,
        thumbnailImageSrc: this.defaultImagePath,
        alt: `${this.product?.title || 'Producto'} - Imagen por defecto`
      }];
    }
    
    // Resetear índice si es necesario
    if (this.currentImageIndex >= this.galleryImages.length) {
      this.currentImageIndex = 0;
    }
    
    // Calcular número de thumbnails visibles
    this.numVisible = Math.min(this.galleryImages.length, 5);
    
    console.log('Gallery images prepared:', this.galleryImages.length, 'images');
  }

  onImgError(event: Event) {
    const img = event.target as HTMLImageElement;
    if (img.src !== this.defaultImagePath) {
      img.src = this.defaultImagePath;
    }
  }

  selectImage(index: number) {
    console.log('🖱️ Thumbnail clicked:', index);
    this.currentImageIndex = index;
    console.log('📍 New current index:', this.currentImageIndex);
  }

  nextImage() {
    console.log('➡️ Next image clicked, current:', this.currentImageIndex);
    if (this.currentImageIndex < this.galleryImages.length - 1) {
      this.currentImageIndex++;
      console.log('📍 New index:', this.currentImageIndex);
    }
  }

  prevImage() {
    console.log('⬅️ Previous image clicked, current:', this.currentImageIndex);
    if (this.currentImageIndex > 0) {
      this.currentImageIndex--;
      console.log('📍 New index:', this.currentImageIndex);
    }
  }
}
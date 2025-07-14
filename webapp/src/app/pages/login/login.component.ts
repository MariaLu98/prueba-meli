import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { ButtonModule } from 'primeng/button';
import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';
import { IftaLabelModule } from 'primeng/iftalabel';
import { MessageService } from 'primeng/api';
import { SplitButtonModule } from 'primeng/splitbutton';
import { ToastModule } from 'primeng/toast';
import { ImportsModule } from '../imports';



import { Product } from '../../../domain/product';
import { ProductService } from '../../../service/productservice';
import { HttpClient } from '@angular/common/http';
import { ViewChild } from '@angular/core';
import { Table } from 'primeng/table';

interface City {
  name: string;
  code: string;
}

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    InputTextModule,
    PasswordModule,
    ButtonModule,
    InputIconModule,
    IconFieldModule,
    InputTextModule,
    IftaLabelModule,
    SplitButtonModule,
    ToastModule,
    ImportsModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [MessageService]
})
export class LoginComponent implements OnInit {
  nombre = '';
  correo = '';
  nombreMateria = '';
  value: string | undefined;
  items: any;
  products!: Product[];
  materias: any[] = [];

  value3: any = null;
  profesores: any[] = [];

  constructor(
    private messageService: MessageService,
    private productService: ProductService,
    private http: HttpClient
  ) {
    this.items = [
      {
        label: 'Crear Profesor',
        command: () => {
          this.saveProfesor();
        }
      }
    ];
  }

  crearMateria(): void {
    if (!this.value3 || !this.nombreMateria.trim()) {
      this.messageService.add({
        severity: 'warn',
        summary: 'Campos requeridos',
        detail: 'Debe completar todos los campos.'
      });
      return;
    }

    const nuevaMateria = {
      nombre: this.nombreMateria,
      creditos: 3,
      profesorId: this.value3.value
    };

    this.http.post('http://localhost:5128/api/Materias', nuevaMateria, {
      responseType: 'text' // Para que también podamos leer errores 400 como texto
    }).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Éxito',
          detail: 'Materia creada exitosamente.'
        });
        // Opcional: limpia campos después de crear
        this.nombreMateria = '';
        this.value3 = null;
      },
      error: (err) => {
        const errorMsg = err.status === 400 ? err.error : 'Ocurrió un error al crear la materia.';
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: errorMsg
        });
      }
    });
  }

  saveEstudiante(severity: string): void {
    if (!this.nombre.trim() || !this.correo.trim()) {
      this.messageService.add({
        severity: 'warn',
        summary: 'Campos obligatorios',
        detail: 'Por favor completa todos los campos'
      });
      return;
    }

    const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.correo);
    if (!correoValido) {
      this.messageService.add({
        severity: 'error',
        summary: 'Correo inválido',
        detail: 'Por favor ingresa un correo válido'
      });
      return;
    }

    const payload = {
      nombre: this.nombre,
      correo: this.correo
    };

    this.http.post('http://localhost:5128/api/Estudiantes', payload, { responseType: 'text' }).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Éxito',
          detail: 'Estudiante creado correctamente'
        });
        this.nombre = '';
        this.correo = '';
        if (this.mostrarEstudiantes) {
          this.cargarEstudiantes();
          this.cargando = false;

        }
      },
      error: (err) => {
        // err.error contendrá el string del backend si es 400
        const mensaje = typeof err.error === 'string' ? err.error : 'Ocurrió un error inesperado';
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: mensaje
        });
        console.error('Error del backend:', err);
      }
    });
  }

  saveProfesor(): void {
    if (!this.nombre.trim() || !this.correo.trim()) {
      this.messageService.add({
        severity: 'warn',
        summary: 'Campos obligatorios',
        detail: 'Por favor completa todos los campos'
      });
      return;
    }

    const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.correo);
    if (!correoValido) {
      this.messageService.add({
        severity: 'error',
        summary: 'Correo inválido',
        detail: 'Por favor ingresa un correo válido'
      });
      return;
    }

    const payload = {
      nombre: this.nombre,
      correo: this.correo
    };

    this.http.post('http://localhost:5128/api/Profesores', payload, { responseType: 'text' }).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Éxito',
          detail: 'Estudiante creado correctamente'
        });
        this.nombre = '';
        this.correo = '';
        if (this.mostrarTabla) {
          this.cargarMaterias();
          this.cargando = false;
        }
      },
      error: (err) => {
        // err.error contendrá el string del backend si es 400
        const mensaje = typeof err.error === 'string' ? err.error : 'Ocurrió un error inesperado';
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: mensaje
        });
        console.error('Error del backend:', err);
      }
    });
  }


  update() {
    this.messageService.add({ severity: 'success', summary: 'Success', detail: 'Data Updated' });
  }

  delete() {
    this.messageService.add({ severity: 'success', summary: 'Success', detail: 'Data Deleted' });
  }

  cities: City[] | undefined;
  ngOnInit() {
    this.productService.getProductsMini().then((data) => {
      this.products = data;
    });

    this.cargarProfesores();

    this.cities = [
      { name: 'New York', code: 'NY' },
      { name: 'Rome', code: 'RM' },
      { name: 'London', code: 'LDN' },
      { name: 'Istanbul', code: 'IST' },
      { name: 'Paris', code: 'PRS' },
    ];

  }

  cargarProfesores(): void {
    this.http.get<any[]>('http://localhost:5128/api/Profesores').subscribe({
      next: (data) => {
        // Solo mantener nombre y profesorId para el select
        this.profesores = data.map(p => ({
          name: p.nombre,
          value: p.profesorId
        }));
      },
      error: (err) => {
        console.error('Error al cargar profesores:', err);
      }
    });
  }


  cargarMaterias() {
    this.http.get<any[]>('http://localhost:5128/api/Materias').subscribe({
      next: (data) => {
        this.materias = data;
        this.cargando = false;
      },
      error: (err) => {
        console.error('Error al cargar materias', err);
        this.cargando = false;
      }
    });
  }

  mostrarTabla = false;

  cargando = false;

  toggleMaterias() {
    if (this.mostrarTabla) {
      this.mostrarTabla = false;
      return;
    }

    this.mostrarTabla = true;
    this.mostrarEstudiantes = false;

    if (this.materias.length === 0) {
      this.cargando = true;
      this.cargarMaterias();
      this.cargando = false;

    }
  }

  @ViewChild('dt') dt!: Table;
  @ViewChild('dtEstudiantes') dtEstudiantes!: Table;

  onGlobalFilterMaterias(event: Event) {
    const input = event.target as HTMLInputElement;
    this.dt?.filterGlobal(input.value, 'contains');
  }

  onGlobalFilterEstudiantes(event: Event) {
    const input = event.target as HTMLInputElement;
    this.dtEstudiantes?.filterGlobal(input.value, 'contains');
  }

  estudiantes: any[] = [];
  mostrarEstudiantes: boolean = false;

  async toggleEstudiantes(): Promise<void> {
    this.mostrarEstudiantes = !this.mostrarEstudiantes;

    this.mostrarTabla = this.mostrarEstudiantes ? false : this.mostrarTabla;
    if (this.mostrarEstudiantes) {
      this.mostrarTabla = false; // Oculta la tabla de materias
      if (this.estudiantes.length === 0) {
        this.cargando = true;
        await this.cargarEstudiantes();
        this.cargando = false;

      }
    }
  }

  cargarEstudiantes(): void {
    this.http.get<any[]>('http://localhost:5128/api/Estudiantes').subscribe({
      next: (data) => {
        this.estudiantes = data;
      },
      error: (err) => {
        console.error('Error al recargar estudiantes:', err);
      }
    });
  }


  login() {
    console.log('Nombre:', this.nombre);
    console.log('Correo:', this.correo);
    console.log(this.value);
    alert('Intentando iniciar sesión...');
  }
}

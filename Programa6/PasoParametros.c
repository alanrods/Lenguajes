#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define M_PI 3.14159265358979323846

void invierteLista(int *arreglo, int tam);

double **distanciaAngulo(double **arreglo, int tam);

void main(){
	int i, tam, *A;
	double **B;

	printf("Ingrese el tamano del arreglo -> ");
	scanf("%d", &tam);

	A = (int *)malloc(tam*sizeof(int));
	putchar('\n');
	for (i = 0; i < tam; ++i){
		printf("arreglo[%d] -> ", i);
		scanf("%d", A+i);
	}

	putchar('\n');
	B = (double **)malloc(tam*sizeof(double *));
	for (i=0; i<tam; i++)
        *(B + i) = (double *)malloc(2*sizeof(double));

	putchar('\n');
	for (i = 0; i < tam; ++i){
		printf("(x%d, y%d) -> ", i, i);
		scanf("%lf, %lf", *(B + i), *(B + i) + 1);
	}

	invierteLista(A, tam);

	putchar('\n');
	for (i = 0; i < tam; ++i){
		printf("%d\n", *(A+i));
	}

	B = distanciaAngulo(B, tam);

	putchar('\n');
	for (i = 0; i < tam-1; ++i){
		printf("(%.4lf, %.4lf)\n", *(*(B+i)), *(*(B+i) + 1));
	}
}

void invierteLista(int *arreglo, int tam){
	int i, aux;

	for(i = 0; i < (tam/2); i++){		 
		aux = *(arreglo + i);
		*(arreglo + i) = *(arreglo + (tam-1) - i);
		*(arreglo + (tam-1) - i) = aux;
	}
}

double **distanciaAngulo(double **arreglo, int tam){
	int i;
	double **copia = (double **)malloc((tam-1)*sizeof(double *));
	for (i=0; i<tam-1; i++)
        *(copia + i) = (double *)malloc(2*sizeof(double));

	for (i = 0; i < tam - 1; ++i){
		*(*(copia + i)) = sqrt(pow(abs(*(*(arreglo + i + 1))-*(*(arreglo + i))), 2) + pow(abs(*(*(arreglo + i + 1) + 1)-*(*(arreglo + i) + 1)), 2));
		*(*(copia + i) + 1)	= atan2(*(*(arreglo + i + 1) + 1)-*(*(arreglo + i) + 1), *(*(arreglo + i + 1))-*(*(arreglo + i)))*(180/M_PI);
	}
	return copia;
}
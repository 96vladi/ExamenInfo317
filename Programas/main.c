
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#define MAX 128
void encriptar(char frase[],int numero);
void desencriptar(char frase[],int numero);

void desencriptar(char frase[],int numero)
{
    int i=0;
    while(frase[i]!='\0')
    {
        frase[i]=frase[i]-numero;
        i++;
    }
    printf(frase);
}

void encriptar(char frase[],int numero)
{
    int i=0;
    char letra;
    while(frase[i]!='\0')
    {
        frase[i]=frase[i]+numero;
        i++;
    }
    printf(frase);
}

int main()
{
    #pragma omp master
    {
        int des=3;
        char nom[]="Vladimir Maidana Acarapi";
        printf("Encriptacion:\n");
        encriptar(nom, des);
        getchar();
        printf("Desencriptacion:\n");
        desencriptar(nom, des);
        getchar();
    }
}

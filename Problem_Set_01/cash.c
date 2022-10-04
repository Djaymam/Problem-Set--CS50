#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    float troco;
    int trocoReceber;
    int trocoFalta;

    //promp user for positive number
    do
    {
       //intput do troco
        printf("Troco a entregar:");
        scanf("%f",&troco);
    } while (troco<0);
    
    
    //conversao do troco em centimo

    trocoFalta = round(troco*100);
    trocoReceber=trocoFalta;
    
    int moeda1, moeda5, moeda10, moeda25=0;
    
    printf("o troco em cent:%d",trocoReceber);

    while (trocoFalta!=0)
    {                             //exp 100
        moeda25=trocoReceber/25;  // = 5
        trocoFalta=trocoReceber%25;
        trocoReceber=trocoFalta;

        moeda10=trocoReceber/10;
        trocoFalta=trocoReceber%10;
        trocoReceber=trocoFalta;

        moeda5=trocoReceber/5;
        trocoFalta=trocoReceber%5;
        trocoReceber=trocoFalta;

        moeda1=trocoReceber/1;
        trocoFalta=trocoReceber%1;
    }

    //print the Result (uncoment the code for other printf result)
    /*
    printf("\nMoedas 25:%d",moeda25);
    printf("\nMoedas 10:%d",moeda10);
    printf("\nMoedas 5:%d",moeda5);
    printf("\nMoedas 1:%d",moeda1);
    */
   
    printf("\nDeve Entregar:\n %d Moeda de 25 cent.\n %d Moeda 10 cent.\n %d Moedas 5 cent.\n %d Moedas 1 cent.",moeda25,moeda10,moeda5,moeda1);
    return 0;
}


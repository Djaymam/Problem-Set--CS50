#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int count,i,k;
    
    //validation for the rows count
    do
    {
        printf("Type a number (2-10): ");
        scanf("%d", &count);
        
    } while (count>10 || count<=1);

    for (i = 1; i < count; i++) //print the collums
    {
        //print the spaces
        for (int j = i; j < count; j++)
        {
            printf(" ");
        }
        
        // print the Star
        for (int k = 1; k <= i; k++)  
        {  
            printf("#");
             
        }  
        printf ("\n");
      
    }
    return 0;
}


    



#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[]){

    //key convercion to int
    int key=atoi(argv[1]);
    //int lenght=strlen(argv[1]);

    //user Key validation
    if (argc!=2)
    {
        printf("./ceasar key");
        return 1;
    }

    
    if (key>=1)
       {
        printf("Success");
    }else{
        printf("./ceasar key!!");
        return 1;
    }


    printf("\nThe Key is: %d\n",key);
    
    //imput the message
    //string plainText="ZzzZ!?";
    string plainText=get_string("Message: ");
 
    printf("Plaintext: %s\n",plainText);

    int textLength=strlen(plainText);

    //Encripting
    printf("Ciphertext: ");

    for (int i = 0; i < textLength; i++)
    {
        int lower=islower(plainText[i]);
        int upper=isupper(plainText[i]);
        //ci = (pi + k) % 26
        int newChart=plainText[i]+key;

        //printing the Text
        
        if (lower!=0)
        {
            
            printf("%c",(newChart-97)%26+97);
        }else if (upper!=0)
        {
    
            printf("%c",(newChart-65)%26+65);

        }else{
            printf("%c",plainText[i]);

        }
        
        
    }
    
    

    return 0;
}
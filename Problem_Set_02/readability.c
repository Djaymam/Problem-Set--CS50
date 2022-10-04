#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(void){
    //uncomment the line below if u wich to type a sentense yourself or paste a new one in the text variable bellow.
   string text = get_string("Type or paste the text: ");

    //in case you uncomment the code above to imput you sentense pls comment (//) the code below
    //string text= "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.";

    printf("\n%s\n",text);

    //text length
    int textLength=strlen(text);

    //count words
    int words=1; //words its set up as 1 at begining because the program can't read the last space in the sentence

    for ( int i = 0; i < textLength; i++)
    {
        if(text[i]==' ')
        {
         words++;
        }
    }
        
    //count sentence
    int sentence;

    for ( int i = 0; i < textLength; i++)
    {
        if(text[i]=='!'||text[i]=='.'||text[i]=='?')
        {
         sentence++;
        }
    }

    //count letters

    int pontuation,simbols;
    int letters=strlen(text)-words-sentence; //i Just subtract the text lenght and the number of words and setence and i get the total letters. it's not perfect but it works!

    //grade calculator based on Coleman-Liau Index
    int averageLetters,averageSentence; 
    averageLetters=round((letters*100)/words);
    averageSentence=round((sentence*100)/words);
    
    int grade =(0.0588 * averageLetters) - (0.296 * averageSentence) - 15.8 ; 

    //Grade printing
    if (grade>=1&&grade<=16)
    {
       printf("Grade: %d\n",grade);

    }else if (grade>16)
    {
        printf("Grade 16+\n");

    }else{
        printf("Before Grade 1\n");
    }
   
    // uncomment to print the number of words, letters and sentence
    
    printf("words: %d\n",words);
    printf("Letters: %d\n",letters);
    printf("Sentence: %d\n",sentence);

    return 0;
}
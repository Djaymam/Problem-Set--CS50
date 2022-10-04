#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)// i will go to all row of the image (heigth of the image)
    {
        for (int j = 0; j < width; j++)// j will go to all column in each row (width of the image) 
        {
            //for grayscale convert the RGB value to float and divide the total values of the RGBs  by 3 
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;
            
            //calculate average
            int average =(red+green+blue)/3;

            //changing the value of the RGB
            image[i][j].rgbtRed=average;
            image[i][j].rgbtGreen=average;
            image[i][j].rgbtBlue=average;  
        }
        
    }
    return;  
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through the image 
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++) 
        {   
            //get the value of the RGB values from the original image
            float img_Red = image[i][j].rgbtRed;

            float img_Green = image[i][j].rgbtGreen;
            
            float img_Blue = image[i][j].rgbtBlue;

            //new RGB value for image[i][j].rgbt using the formula below
            int new_Red=round(0.393 * img_Red + 0.769 * img_Green + 0.189 * img_Blue);
            int new_Green=round(0.349 * img_Red + 0.686 * img_Green + 0.168 * img_Blue);
            int new_Blue=round(0.272 * img_Red + 0.534 * img_Green + 0.131 * img_Blue);
            
            //if the new value is greater than 255 it will round to 255 in any of the RGB values
            if (new_Red > 255){
                new_Red = 255;
            }

            if (new_Green > 255){
            {
                new_Green = 255;
            }

            if (new_Blue > 255){

                new_Blue = 255;
            }

            //update the RGB values
            image[i][j].rgbtBlue=new_Blue;
            image[i][j].rgbtGreen=new_Green;    
            image[i][j].rgbtRed=new_Red;            

            
        }
        
    }
    
    return;
}

// Reflect image horizontally

void reflect(int height, int width, RGBTRIPLE image[height][width])
{   
    //loop  through image[i][j]
    for (int i = 0; i < height; i++){
        
        for (int j = 0; j < width; j++){

            RGBTRIPLE temp = image[i][j]; //a temporary copy of the original pixel

            image[i][j]=image[i][width-(j+1)];     //   
            image[i][width-(j+1)]=temp;             //
        }
            
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

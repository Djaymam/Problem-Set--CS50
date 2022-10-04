#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
 
int main(int argc, char *argv[])
{
    //check for valid arguments
    if (argc != 2)
    {
        printf("usage: ./recover IMAGE \n");

        return 1;
    }
    //open file for reading
    FILE *imput_file = fopen(argv[1], "r");

    //check if file is valid
    if (imput_file != NULL)
    {
        printf("could not open the file");
        return 2;
    }

    //store block of 512 bytes in an array
    unsigned char buffer[512];

    //track mumber of images recoved
    int count_image = 0;

    //file pointer for recoved images
    FILE *output_file = NULL;

    //char filename[8]
    char *filename=malloc(8 * sizeof(char));

    //Read the blocks of 512 bytes
    while (fread(buffer, sizeof(char), 512, imput_file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff&& buffer[3] & 0xf0==0xe0)
        {
            //write the new JPEG file name
            sprintf(filename, "%03i.jpg", count_image);
            //open output_file for writing

            output_file=fopen(filename,"w")

            //count the number of images recoved
            count_image++;

        }
        
        if (output_file!=NULL)
        {
            fwrite(buffer,sizeof(char),512,output_file);
        }
        
    }
    free(filename);
    fclose(output_file);
    fclose(imput_file);


    return 0;
    
}
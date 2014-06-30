#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main()
{
    srand (time(NULL));



    char mpd[5] = "";
    char in[5] = "";

    char secret[12] = "Mbcpsbupjsf"; //cryptage

    char realsecret[12] = "";

    int i = 0;
    for(i = 0 ; i <= sizeof(secret) ; i++){
        realsecret[i] = secret[i]-1;
    }
    i = 11;
    realsecret[i]= '\0';

    for(i = 0 ; i<= 4 ; i++){
        mpd[i] = rand()%9+49;
    }
    mpd[4] = '\0';

    printf("Entrez le mot de passe (4 chiffres) pour decouvrir le secret !\n");

    while(1){
        fflush(stdin);
        gets(in);
        if(strcmp(in,mpd) == 0){
            printf("Felicitation, le secret est '%s'",realsecret);
            return 0;
        }
    }

    return 0;
}

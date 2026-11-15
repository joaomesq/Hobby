#include <stdio.h>

void main(){
    int i;
    int done;

    while(true){
        i++;
        printf("%d"\n, i);

        printf("Insira 0 para teminar\n");
        scanf("%d", &done);

        if(done == 0){
            break;
        }
    }
}
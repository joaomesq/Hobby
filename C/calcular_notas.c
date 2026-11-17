#include <stdio.h>

int main(int argc, char const *argv[])
{
	int count = 0;
	int total = 0;
	float media = 0;
	float nota;

	while(count < 3 ){
		count = count + 1;

		printf("Insira a %d nota: ", count);
		scanf("%f", &nota);

		total = total + nota;
	}

	media = total / count;
	printf("%f\n", media);
}
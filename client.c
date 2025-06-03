#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv){
	int option;
	char username[16];
	char password[16];
	printf("Welcome to the game streaming app!\n");
	printf("Enter 1 to login, 2 to exit.\n");
	
	if(scanf("%d", &option) != 1) {
		while(getchar() != '\n');
	}

	if(option == 2) {
		exit(0);
	}

	if(option == 1) {
		printf("Enter your username: ");
		scanf("%s", username);
		printf("Enter your password: ");
		scanf("%s", password);
	}


	return 0;
}

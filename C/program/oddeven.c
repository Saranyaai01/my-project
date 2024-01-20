#include <stdio.h>
int odd() {
    int num;
    printf("\nEnter a value: ");
    scanf("%d", &num);

    if(num % 2 == 0)
        printf("%d is even.", num);
    else
        printf("%d is odd.", num);
    
    return 0;
}

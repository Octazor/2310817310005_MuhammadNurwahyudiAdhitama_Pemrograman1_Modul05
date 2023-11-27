#include <stdio.h>
int MaxBilangan(int num1, int num2, int num3, int num4){
    int max = num1;

    if (num2 > max){
        max = num2;
    }
    if (num3 > max){
        max = num3;
    }
    if (num4 > max){
        max = num4;
    }
    return max;
}
int main() {
int a, b, c, d; 
scanf("%d %d %d %d", &a, &b, &c, &d);
int hasil = MaxBilangan(a, b, c, d);
printf("%d", hasil); 
return 0;
}


#include <stdio.h>
#include <math.h>
int main() {
	float x1, y1, x2, y2, gdistance,mid1,mid2;
	printf("Enter coordinates of points A:");
	scanf("%f%f", &x1,&y1);
    printf("Enter coordinates of points B:");
	scanf("%f%f", &x2,&y2);
	gdistance = ((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1));
	printf("Distance between the said points: %.2f", sqrt(gdistance));
    mid1= (x1+x2)/2;
    mid2= (y1+y2)/2;
    printf("\nThe coordinates of midpoint of A and B are (%.2f,%.2f)",mid1,mid2);
	return 0;
}


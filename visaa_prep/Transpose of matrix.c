#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int i,j,n;
    scanf("%d",&n);
    int arr[n][n];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&arr[i][j]);
        }
   }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ",arr[j][i]);
        }
        printf("\n");
   }
    return 0;
}

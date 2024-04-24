#include <stdio.h>
#include <stdlib.h>
void printMatrix(double *A, double *B, double *X, int mn){
    for (int j = 0; j < mn; j++){
        for (int i = 0; i < mn; i++){
            int p = j * mn + i;
            printf(" %12.7lf", A[p]);
        }//for (int i = 0; i < mn; i++){
        printf("|\t %12.7lf", B[j]);
        printf("\n");
    }//for (int j = 0; j < mn; j++){
    printf("\n");

    printf("X = {");
    for (int i = 0; i < mn; i++){
         
        printf(" %12.7lf", X[i]);
    }//for (int i = 0; i < mn; i++){
    printf("}\n");
}

void solver_gauss(double *A, double *B, double *X, int mn){
    double cof = 0.0;
   
    for (int j = 0; j < mn; j++){
        cof = A[j * mn + j];
        for (int i = j; i < mn; i++){
            A[j * mn + i] = A[j * mn + i] / cof ;
        }//for (int i = 0; i < mn; i++){
        B[j] = B[j] / cof;
        
        for (int k = j + 1; k < mn; k++){
            cof = A[k * mn + j];
            //if (k < mn){
                for (int i = j; i < mn; i++){
                    A[k * mn + i] = A[k * mn + i] - (cof * A[j * mn + i]);
                }//for (int i = 0; i < mn; i++){
            //}//if (k < mn){
            B[k] = B[k] - cof * B[j];
        }//for (int k = j + 1; k < mn; k++){
    }//for (int j = 0; j < mn; j++){    

    for (int i = mn - 1; i >= 0; i--){
        X[i] = B[i]; /// A[i * mn + i];
        double acc = 0.0f;
        for (int j = i + 1; j < mn; j++){
            acc += A[i * mn + j] * X[j];
        } 
        X[i] -= acc;
    }//for (int i = mn-1; i >= 0; i++ ){
        

} 

   
int main (int ac, char **av){
    int mn = 4;
    double A[] = {2.0, 2.0, 1.0, 1.0, 1.0, -1.0, 2.0, -1.0, 3.0, 2.0, -3.0, -2.0, 4.0, 3.0, 2, 1};
    double B[] = {7.0, 1.0, 4.0, 12.0};
    double X[] = {0.0, 0.0, 0.0, 0.0};
    printf("\nResolvedor de sistema linear - Método de Gauss\n");
    printMatrix(A, B, X, mn);
    solver_gauss(A, B, X, mn);
    printf("\n\nSolução: \n");
    printMatrix(A, B, X, mn);
    return EXIT_SUCCESS;
}

#include <stdio.h>
#include <omp.h>

#pragma omp declare simd uniform(width) linear(i:1)
double integracao(int i, double width) { 
    double x = (i + 0.5) * width; // Midpoint of the interval
    return 4.0 / (1.0 + x * x);
}

int main() {
    int n = 1000000;          // Number of intervals (steps)
    double width = 1.0 / n;   // Width of each rectangle
    double sum = 0.0;

    #pragma omp simd reduction(+:sum)
    for (int i = 0; i < n; i++) {
        sum += integracao(i, width);
    }

    double pi = sum * width;
    printf("Estimated Pi = %.15f\n", pi);

    return 0;
}
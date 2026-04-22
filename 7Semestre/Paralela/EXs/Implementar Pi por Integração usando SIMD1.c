#include <stdio.h>
#include <omp.h> 

int main() {
    int n = 1000000;          // Number of intervals (steps)
    double width = 1.0 / n;   // Width of each rectangle
    double sum = 0.0;
    double x;
    
    #pragma omp simd private(x) reduction(+:sum)
    for (int i = 0; i < n; i++) {
        x = (i + 0.5) * width; // Midpoint of the interval
        sum += 4.0 / (1.0 + x * x);
    }

    double pi = sum * width;
    printf("Estimated Pi = %.15f\n", pi);

    return 0;
}
/*
O código realiza a soma de dois vetores muito grandes (A e B, cada um com 50 milhões de elementos) e armazena o resultado em um terceiro vetor (C).

utiliza o paralelismo através da diretiva #pragma omp teams distribute parallel for simd. Essa diretiva orienta o compilador a dividir o trabalho em "times" de threads e aplicar vetorização (SIMD).

*/
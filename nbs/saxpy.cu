#include <stdint.h>

// SAXPY kernel: y = alpha*x + y
__global__ void saxpy(float alpha, float *x, float *y, int32_t n)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        y[i] = alpha * x[i] + y[i];
    }
}

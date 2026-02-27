/* * Copyright (c) 2026 Americo Simoes
 * License: Sovereign Research License (SRL)
 * * SOVEREIGN-LOGIC: Multi-Threaded Unitary SAT Propagator
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <complex>
#include <fstream>
#include <omp.h>

const float BETA = 1.23f;
const float LAMBDA = 0.963f;

extern "C" {
    void solve_manifold(const unsigned char* input, unsigned char* output, int width, int height) {
        #pragma omp parallel for schedule(dynamic)
        for (int y = 0; y < height; ++y) {
            double phase = 0.42317 + (y * 0.00157 * LAMBDA);
            for (int x = 0; x < width; ++x) {
                float raw = (float)input[y * width + x] / 255.0f;
                float energy = std::tanh(BETA * (raw - 0.5f) * LAMBDA);
                std::complex<double> unitary = std::exp(std::complex<double>(0, -1) * (double)energy * (33.0 / BETA));
                output[y * width + x] = (unsigned char)(std::abs(unitary.real() + std::sin(phase)) * 255.0f);
            }
        }
    }
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <input.raw> <output.pgm>" << std::endl;
        return 1;
    }
    std::ifstream in(argv[1], std::ios::binary);
    if (!in) return 1;
    int w = 1024, h = 1024;
    std::vector<unsigned char> input(w * h);
    std::vector<unsigned char> output(w * h);
    in.read((char*)input.data(), w * h);
    
    double start = omp_get_wtime();
    solve_manifold(input.data(), output.data(), w, h);
    double end = omp_get_wtime();
    
    std::ofstream out(argv[2], std::ios::binary);
    out << "P5\n" << w << " " << h << "\n255\n";
    out.write((char*)output.data(), w * h);
    
    std::cout << "Propagation Time: " << (end - start) << "s" << std::endl;
    return 0;
}

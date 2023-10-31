#include <random>
#include <iostream>
using namespace std;
struct Fraction{
    int numerator;
    int denominator;
}Four_Numbers;

int main() {
    // Create a random device
    random_device rd;

    // Initialize Mersenne Twister pseudo-random number generator
    mt19937 gen(rd());

    // Uniform distribution between 1 and 100
    uniform_int_distribution<> dis(1, 100);
    // Generate and output a random integer
    for(int fraction;)
    std::cout << dis(gen) << '\n';

    return 0;
}

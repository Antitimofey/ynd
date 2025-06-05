#include <algorithm>
#include <cmath>
#include <random>
#include <iostream>



int odd_experiment(int n, int path = 1) {

    int cnt = 0;
    
    // Random number generator setup
    std::random_device rd;  // Obtain a random seed from hardware
    std::mt19937 gen(rd()); // Standard Mersenne Twister engine
    std::uniform_real_distribution<float> dis(0.0f, 1.0f); // Uniform distribution [0, 1)

    while (path != 0) {
        ++cnt;

        if (path == n/2) {
            if (dis(gen) < float(n/2 + 1)/n) {
                --path;
            }
            continue;
        }

        if (dis(gen) < float(n-path)/n) {
            --path;
        } else {
            ++path;
        }

        /*
        
        if (step == 2) {
            if (dis(gen) < 3.f/5) {
                --step;
            }
        } else {
            if (dis(gen) < 4.f/5) {
                return cnt;
            } else {
                ++step;
            }
        }
        */

    }

    return cnt;
 }





int main() {

    int nodes_cnt = 0;
    int start_node = 0;
    std::cout << "set nodes count and start node" << std::endl;
    std::cin >> nodes_cnt >> start_node;

    long long sum = 0;
    int cnt = 0;


    for (int i = 0; i < std::pow(10, 5); ++i) {
        sum += odd_experiment(nodes_cnt, start_node);


        std::cout << "experiment No " << i + 1 << "\tavg is " << double(sum) / (i + 1);
        std::cout << std::endl;
    }
}
#include <iostream>
#include <queue>
#include <map>



int main() {
    int n, k = 0;
    std::cin >> n >> k;

    std::queue<int> que;
    std::map<int, int> dict;

    int val = 0;
    for (int i = 0; i < k; ++i) {
        std::cin >> val;
        que.push(val);
        dict[val]++;
    }

    int max_lectires = dict.size(), current_lectures = dict.size();


    int in = 0, out = 0;
    for (int i = k; i < n; ++i) {
        std::cin >> in;
        que.push(in);
        
        if (dict[in]++ == 0) {
            current_lectures++;
        }
        
        out = que.front();
        que.pop();
        dict[out]--;
        if (dict[out] == 0) {
            current_lectures--;
        }

        max_lectires = std::max(max_lectires, current_lectures);
    }

    std::cout << max_lectires <<std::endl;
}
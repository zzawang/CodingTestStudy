#include <stdio.h>
#include <vector>

using namespace std;

int N;

vector <int> Up[50];
vector <int> Down[50];

void Del(int W) {
    int num = Down[W].size();
    for (int i = num - 1; i >= 0; i--) {
        int next = Down[W][i];
        if (next == -1) {
            break;
        }
        Down[W].erase(Down[W].begin() + i);
        Del(next);
    }
    if (Down[W].size() == 0) {
        Down[W].push_back(-1);
    }
}

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        Up[i].clear();
        Down[i].clear();
    }
    for (int i = 0; i < N; i++) {
        int a;
        scanf("%d", &a);
        if (a == -1) {
            continue;
        }
        Down[a].push_back(i);
        Up[i].push_back(a);
    }
    int remove;
    scanf("%d", &remove);
    int cnt = 0;
    if (Up[remove].size() != 0) {
        int p = Up[remove][0];
        int num_p = Down[p].size();
        for (int i = 0; i < num_p; i++) {
            if (Down[p][i] == remove) {
                Down[p].erase(Down[p].begin() + i);
                break;
            }
        }
        Del(remove);

        for (int i = 0; i < N; i++) {
            if (Down[i].size() == 0) {
                cnt++;
            }
        }
    }
    printf("%d", cnt);
}

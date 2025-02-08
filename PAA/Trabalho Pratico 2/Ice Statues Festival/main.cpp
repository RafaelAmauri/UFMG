// Solução para https://judge.beecrowd.com/en/problems/view/1034


#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minBlocks(vector<int>& blockOptions, int targetHeight) {
    vector<int> cache(targetHeight + 1, INT_MAX);

    cache[0] = 0;

    for (int i = 1; i <= targetHeight; ++i)
    {

        for (int j = 0; j < blockOptions.size(); ++j)
        {
            if (blockOptions[j] <= i)
            {
                int res = cache[i - blockOptions[j]];

                if (res != INT_MAX && res + 1 < cache[i])
                {
                    cache[i] = res + 1;
                }
            }
        }
    }


    return cache[targetHeight] != INT_MAX ? cache[targetHeight] : -1;
}


int main() {
    int nTests;
    cin >> nTests;

    for (int i = 0; i < nTests; i++)
    {
        int nBlocks, targetHeight;
        cin >> nBlocks >> targetHeight;
        vector<int> blockOptions(nBlocks);

        for (int j = 0; j < nBlocks; j++) 
        {
            cin >> blockOptions[j];
        }


        cout << minBlocks(blockOptions, targetHeight) << endl;
    }
    return 0;
}

// Solução Beecrowd 1552 https://judge.beecrowd.com/en/problems/view/1552

#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

struct Edge
{
    double weight;
    int destId;

    Edge(double w, int d) : weight(w), destId(d)
    {
    }
};

struct CompareEdge
{
    bool operator()(const Edge& e1, const Edge& e2) const
    {
        return e1.weight > e2.weight;
    }
};


double prim(unordered_map<int, vector<pair<int, double>>> adjacencyList, int nPeople)
{
    
    priority_queue<Edge, vector<Edge>, CompareEdge> pq;
    unordered_set<int> includedVertices;
    pq.push(Edge(0, 0));

    int destId;
    double weight;
    double minimalDistance = 0;
    
    while(includedVertices.size() < nPeople)
    {
        // Get edge with the lowest weight
        Edge currentEdge = pq.top();
        weight           = currentEdge.weight;
        destId           = currentEdge.destId;
        pq.pop();

        // Skip already included edges
        if(includedVertices.find(destId) != includedVertices.end())
            continue;

        minimalDistance += weight;
        includedVertices.insert(destId);

        for(auto &iter: adjacencyList[destId])
        {
            int neighborId = iter.first;
            double weight  = iter.second;

            if(neighborId == destId)
                continue;
            
            pq.push(Edge(weight, neighborId));
        }
    }

    return minimalDistance;
}



double distance(int x1, int y1, int x2, int y2)
{
    return sqrt( pow(x2-x1, 2) + pow(y2-y1, 2) );
}


int main()
{
    int nTests, nPeople, x, y;
    unordered_map<int, pair<int, int>> pointIds;
    unordered_map<int, vector<pair<int, double>>> adjacencyList;
    
    cin >> nTests;

    for(int i=0; i < nTests; i++)
    {
        cin >> nPeople;
        
        pointIds.clear();
        adjacencyList.clear();
        
        for(int j=0; j < nPeople; j++)
        {
            cin >> x;
            cin >> y;

            pointIds[j] = make_pair(x,y);
            adjacencyList[j] = vector<pair<int, double>>();
        }

        for(int j=0; j < nPeople; j++)
        {
            for(int k=0; k < j; k++)
            {
                if(j == k)
                    continue;
                
                pair<int, int> point1 = pointIds[j];
                pair<int, int> point2 = pointIds[k];

                double d = distance(point1.first, point1.second, point2.first, point2.second);
                adjacencyList[j].push_back(make_pair(k, d));
                adjacencyList[k].push_back(make_pair(j, d));
            }
        }

        cout << fixed << setprecision(2) << prim(adjacencyList, nPeople)/100 << endl;
    }
    

    return 0;
}
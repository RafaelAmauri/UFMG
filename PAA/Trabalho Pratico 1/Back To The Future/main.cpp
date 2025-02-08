// Solução Beecrowd 1447 https://judge.beecrowd.com/en/problems/view/1447

#include <bits/stdc++.h>
#define PRINT_SHORTEST_PATH false

using namespace std;

bool dijkstra(unordered_map<int, unordered_map<int, pair<int, bool>>> &adjacencyList, int srcId, int destId, list<int> &shortestPath, int nCities)
{   
    vector<int> distanceFromSrc(nCities, numeric_limits<int>::max());
    vector<int> originOfVertex(nCities, -1);

    distanceFromSrc[srcId] = 0;
    
    unordered_set<int> visitedVertices;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, srcId});
    
    int currentVertexDistanceToSrc, currentVertexId, distanceToNeighbor, neighborId, neighborWeight;
    bool isFound = false;
    while((!pq.empty()) && (!isFound))
    {
        currentVertexDistanceToSrc = pq.top().first;
        currentVertexId            = pq.top().second;
        pq.pop();
        
        if(visitedVertices.find(currentVertexId) != visitedVertices.end())
            continue;

        visitedVertices.insert(currentVertexId);
        
        for(auto &iter : adjacencyList[currentVertexId])
        {
            neighborId         = iter.first;
            neighborWeight     = iter.second.first;
            int isUsed         = iter.second.second;
            if(isUsed)
                continue;

            distanceToNeighbor = currentVertexDistanceToSrc + neighborWeight;

            if(distanceToNeighbor < distanceFromSrc[neighborId])
            {
                distanceFromSrc[neighborId] = distanceToNeighbor;
                originOfVertex[neighborId]  = currentVertexId;

                pq.push({distanceToNeighbor, neighborId});
            }
        }
    }
    currentVertexId = destId;
    while(originOfVertex[currentVertexId] != -1)
    {
        shortestPath.push_front(currentVertexId);

        int price = adjacencyList[originOfVertex[currentVertexId]][currentVertexId].first;
        adjacencyList[originOfVertex[currentVertexId]].erase(currentVertexId);
        adjacencyList[originOfVertex[currentVertexId]][currentVertexId] = make_pair(price, true);

        currentVertexId = originOfVertex[currentVertexId];
    }

    shortestPath.push_front(srcId);
    
    if(PRINT_SHORTEST_PATH)
    {
        for(auto &i : shortestPath)
            cout << i+1 << " ";
        cout << endl;
    }

    return shortestPath.size() != 1;
}


int main()
{
    int nCities, nRoutes, city1, city2, price, nFriends, nFreeSeats, paidAmount, currentStop, nextStop, instance;
    bool success;
    
    instance = 1;
    unordered_map<int, unordered_map<int, pair<int, bool>>> adjacencyList;
    list<int> shortestPath;
    list<list<int>> allPaths;
    while (cin >> nCities >> nRoutes)
    {
        paidAmount = 0;
        success = false;

        for(int i = 0; i < nRoutes; i++)
        {
            cin >> city1 >> city2 >> price;

            city1 -= 1;
            city2 -= 1;

            adjacencyList[city1][city2] = make_pair(price, false);
            adjacencyList[city2][city1] = make_pair(price, false);
        }

        cin >> nFriends >> nFreeSeats;

        if(nRoutes > 0)
        {   
            for(int i=0; i < ceil((float)nFriends/(float)nFreeSeats); i++)
            {
                success = dijkstra(adjacencyList, 0, nCities-1, shortestPath, nCities);
                
                allPaths.push_back(shortestPath);
                shortestPath.clear();

                if(!success)
                    break;
            }

            if(success)
            {
                for(auto &path : allPaths)
                {
                    for(int i=0; i < path.size()-1; i++)
                    {   
                        auto iter = path.begin();
                        advance(iter, i);
                        currentStop = *iter;
                        advance(iter, 1);
                        nextStop = *iter;

                        if(adjacencyList[currentStop][nextStop].second != adjacencyList[nextStop][currentStop].second)
                        {
                            paidAmount += adjacencyList[currentStop][nextStop].first * min(nFreeSeats, nFriends);
                            
                            adjacencyList[currentStop][nextStop] = make_pair(adjacencyList[currentStop][nextStop].first, false);
                            adjacencyList[nextStop][currentStop] = make_pair(adjacencyList[currentStop][nextStop].first, false);
                        }
                    }
                    nFriends -= nFreeSeats;
                }
            }
        }

        cout << "Instancia " << instance << endl;
        if(!success)
            cout << "impossivel\n";
        else
            cout << paidAmount << endl;
        
        cout << "\n";

        instance += 1;

        for(auto &vertex : adjacencyList)
            vertex.second.clear();

        adjacencyList.clear();
        shortestPath.clear();
        allPaths.clear();
    }

    return 0;
}
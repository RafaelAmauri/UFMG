// Solução Beecrowd 1205 https://judge.beecrowd.com/en/problems/view/1205

#include <bits/stdc++.h>

using namespace std;


void dijkstra(unordered_map<int, unordered_map<int, int>> *adjacencyList, int srcId, int destId, list<int> *shortestPath)
{
    unordered_map<int, int> distanceFromSrc;
    unordered_map<int, int> originOfVertex;
    
    for(auto iter : *adjacencyList)
    {
        distanceFromSrc[iter.first] = numeric_limits<int>::max(); //Setting everything to MAX_INT
        originOfVertex[iter.first]  = -1; // Parent of all vertices is -1
    }

    distanceFromSrc[srcId] = 0;
    
    unordered_set<int> visitedVertices;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, srcId});
    
    int currentVertexDistanceToSrc, currentVertexId, distanceToNeighbor, neighborId, neighborWeight;

    while((! pq.empty()))
    {
        currentVertexDistanceToSrc = pq.top().first;
        currentVertexId            = pq.top().second;
        pq.pop();
        
        if(visitedVertices.find(currentVertexId) != visitedVertices.end())
            continue;

        visitedVertices.insert(currentVertexId);

        for(auto &iter : (*adjacencyList)[currentVertexId])
        {
            neighborId         = iter.first;
            neighborWeight     = iter.second;
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
        shortestPath->push_front(currentVertexId);
        currentVertexId = originOfVertex[currentVertexId];
    }

    shortestPath->push_front(srcId);

    return;
}


int nStrategicPoints, nRoads, nBullets, startingPoint, destinationPoint, nSnipers, p1, p2, aux, neighborId;
double probKilling, probSuccess, neighborWeight;

int main()
{
    while(cin >> nStrategicPoints >> nRoads >> nBullets >> probKilling)
    {
        unordered_map<int, unordered_map<int, int>> adj\acencyList;
        list<int> *shortestPath = new list<int>;

        for(int i = 0; i < nRoads; i++)
        {
            cin >> p1 >> p2;
            adjacencyList[p1-1][p2-1] = 0;
            adjacencyList[p2-1][p1-1] = 0;
        }

        cin >> nSnipers;
        int snipersByPos[nStrategicPoints] = { 0 };

        for(int i=0; i < nSnipers; i++)
        {
            cin >> aux;
            aux -= 1;
            snipersByPos[aux] += 1;
        }

        cin >> startingPoint >> destinationPoint;
        startingPoint -= 1;
        destinationPoint -= 1;
        nBullets -= snipersByPos[startingPoint];
        
        if(nBullets < 0)
            probSuccess = 0;
        else
        {
            probSuccess = 1.0 * pow(probKilling, snipersByPos[startingPoint]);
            snipersByPos[startingPoint] = 0;
            
            if(probSuccess > 0)
            {
                for(int i=0; i < nStrategicPoints; i++)
                    for(auto &iter : adjacencyList[i])
                        adjacencyList[i][iter.first] = snipersByPos[iter.first];
                
                dijkstra(&adjacencyList, startingPoint, destinationPoint, shortestPath);
                
                if(shortestPath->size() == 1)
                    probSuccess = 0;
                else
                {
                    for(auto pos : *shortestPath)
                    {
                        probSuccess = probSuccess * pow(probKilling, snipersByPos[pos]);
                        nBullets    -= snipersByPos[pos];
                    }
                    if(nBullets < 0)
                        probSuccess = 0;
                }
            }
        }
        cout << fixed << setprecision(3) << probSuccess << endl;
    }
}
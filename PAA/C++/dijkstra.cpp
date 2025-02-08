#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <limits>
#include <queue>
#include <vector>
#include <list>

#include "include/graph.hpp"

using namespace std;


list<int> *dijkstra(Graph* graph, int srcId, int destId)
{
    /*
    Djikstra's algorithm to find the shortest path between two vertices in a graph

        Inputs:
            graph:  The graph object
            srcId:  The ID of the source vertex
            destId: The ID of the destination vertex

        Outputs:
            shortestPath: a list with the IDs of the vertices that, when traversed, form the shortest path; Starts at srcId and ends at destId
    */

    unordered_map<int, int> distanceFromSrc;
    unordered_map<int, int> originOfVertex;
    for(auto iter : graph->vertices)
    {
        distanceFromSrc[iter.first] = numeric_limits<int>::max(); //Setting everything to MAX_INT
        originOfVertex[iter.first]  = -1; // Parent of all vertices is -1
    }
    distanceFromSrc[srcId] = 0;

    unordered_set<int> visitedVertices;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, srcId});


    int currentVertexDistanceToSrc, currentVertexId, distanceToNeighbor, neighborId, neighborWeight;
    while(! pq.empty())
    {
        currentVertexDistanceToSrc = pq.top().first;
        currentVertexId            = pq.top().second;
        pq.pop();

        if(visitedVertices.find(currentVertexId) != visitedVertices.end())
            continue;

        visitedVertices.insert(currentVertexId);

        for (auto iter : graph->vertices[currentVertexId]->neighbors)
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

    list<int> *shortestPath = new list<int>;
    currentVertexId           = destId;
    while(originOfVertex[currentVertexId] != -1)
    {
        shortestPath->push_front(currentVertexId);
        currentVertexId = originOfVertex[currentVertexId];
    }

    shortestPath->push_front(srcId);
    for(auto &i : *shortestPath)
    {
        cout << i << endl;
    }

    return shortestPath;
}


int main()
{
    Vertex *v0 = new Vertex(0);
    Graph *g = new Graph(v0);

    for(int i=1; i < 13; i++)
        g->addVertex(new Vertex(i));

    // This graph can be visualized in https://www.youtube.com/watch?v=GazC3A4OQTE&t=79
    g->addEdge(g->vertices[0], g->vertices[(int)'A' - 64], 7);
    g->addEdge(g->vertices[0], g->vertices[(int)'B' - 64], 2);
    g->addEdge(g->vertices[0], g->vertices[(int)'C' - 64], 3);
    g->addEdge(g->vertices[(int)'A' - 64], g->vertices[(int)'B' - 64], 3);
    g->addEdge(g->vertices[(int)'A' - 64], g->vertices[(int)'D' - 64], 4);
    g->addEdge(g->vertices[(int)'B' - 64], g->vertices[(int)'D' - 64], 4);
    g->addEdge(g->vertices[(int)'B' - 64], g->vertices[(int)'H' - 64], 1);
    g->addEdge(g->vertices[(int)'C' - 64], g->vertices[(int)'L' - 64], 2);
    g->addEdge(g->vertices[(int)'D' - 64], g->vertices[(int)'F' - 64], 5);
    g->addEdge(g->vertices[(int)'E' - 64], g->vertices[(int)'G' - 64], 2);
    g->addEdge(g->vertices[(int)'E' - 64], g->vertices[(int)'K' - 64], 5);
    g->addEdge(g->vertices[(int)'F' - 64], g->vertices[(int)'H' - 64], 3);
    g->addEdge(g->vertices[(int)'G' - 64], g->vertices[(int)'H' - 64], 2);
    g->addEdge(g->vertices[(int)'I' - 64], g->vertices[(int)'L' - 64], 4);
    g->addEdge(g->vertices[(int)'I' - 64], g->vertices[(int)'J' - 64], 6);
    g->addEdge(g->vertices[(int)'I' - 64], g->vertices[(int)'K' - 64], 4);
    g->addEdge(g->vertices[(int)'J' - 64], g->vertices[(int)'L' - 64], 4);
    g->addEdge(g->vertices[(int)'J' - 64], g->vertices[(int)'K' - 64], 4);

    dijkstra(g, 0, (int)'E' - 64);
    
    return 0;
}
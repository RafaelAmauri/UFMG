#include <iostream>
#include <unordered_set>
#include <queue>
#include <vector>

#include "include/graph.hpp"

using namespace std;


struct Edge
{
    int weight;
    int srcId;
    int destId;

    Edge(int w, int s, int d) : weight(w), srcId(s), destId(d)
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


Graph* prim(Graph *graph, int initialVertexId)
{
    Graph *mst = new Graph(new Vertex(initialVertexId));
    priority_queue<Edge, vector<Edge>, CompareEdge> pq;
    unordered_set<int> includedVertices;

    includedVertices.insert(initialVertexId);

    for(auto iter = graph->vertices.begin(); iter != graph->vertices.end(); ++iter)
    { 
        mst->addVertex(new Vertex(iter->first));
    }

    // iterating through the neighbors of initialVertexId and adding neighbors to the stack
    for(auto iter = graph->vertices[initialVertexId]->neighbors.begin(); iter != graph->vertices[initialVertexId]->neighbors.end(); ++iter)
    {
        //            weight      current Vertex    neighbor ID
        pq.push(Edge(iter->second, initialVertexId, iter->first));
    }


    int weight, srcId, destId;
    while(includedVertices.size() < graph->vertices.size())
    {
        // Get edge with the lowest weight
        Edge currentEdge = pq.top();
        weight           = currentEdge.weight;
        srcId            = currentEdge.srcId;
        destId           = currentEdge.destId;
        pq.pop();

        // Skip already included edges
        if(includedVertices.find(destId) != includedVertices.end())
            continue;
        
        // Add edge to the MST
        mst->addEdge(mst->vertices[destId], mst->vertices[srcId], weight);
        includedVertices.insert(destId);

        for(auto iter = graph->vertices[destId]->neighbors.begin(); iter != graph->vertices[destId]->neighbors.end(); ++iter)
        {
            //            weight      current Vertex    neighbor ID
            pq.push(Edge(iter->second, destId, iter->first));
        }

    }

    return mst;
}

int main()
{
    Vertex *v0 = new Vertex(0);
    Graph *g = new Graph(v0);

    for(int i=1; i < 9; i++)
        g->addVertex(new Vertex(i));

    // This graph can be visualized in https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    g->addEdge(g->vertices[0], g->vertices[1], 4);
    g->addEdge(g->vertices[0], g->vertices[7], 8);

    g->addEdge(g->vertices[1], g->vertices[2], 8);
    g->addEdge(g->vertices[1], g->vertices[7], 11);

    g->addEdge(g->vertices[2], g->vertices[3], 7);
    g->addEdge(g->vertices[2], g->vertices[8], 2);
    g->addEdge(g->vertices[2], g->vertices[5], 4);

    g->addEdge(g->vertices[3], g->vertices[4], 9);
    g->addEdge(g->vertices[3], g->vertices[5], 14);

    g->addEdge(g->vertices[4], g->vertices[5], 10);

    g->addEdge(g->vertices[5], g->vertices[6], 2);

    g->addEdge(g->vertices[6], g->vertices[8], 6);
    g->addEdge(g->vertices[6], g->vertices[7], 1);

    g->addEdge(g->vertices[7], g->vertices[8], 7);

    Graph *mst = prim(g, g->root->id);
    mst->printGraph();
    
    return 0;
}
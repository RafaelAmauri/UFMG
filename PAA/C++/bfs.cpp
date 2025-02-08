#include <iostream>
#include <list>
#include <unordered_set>

#include "include/graph.hpp"


void breadthFirstSearch(Graph* g, int searchId)
{
    /*
        Performs a search in graph for the vertex with id searchId

        Input:
            graph: a graph element
            searchId: the ID of the vertex to be found
        
        Output:
            None
    */


    std::list<int> stack;
    stack.push_front(g->root->id);

    std::unordered_set<int> visitedVertices;
    bool notFound = true;

    while(stack.size() > 0 && notFound)
    {
        int currentId = stack.front();
        stack.pop_front();

        std::cout << "Checking for " << currentId << "...\n";

        // if we found the searchId
        if(currentId == searchId)
        {
            std::cout << "Found " << searchId << "!\n";
            notFound = false;
        }
        // If we didn't
        else
        {
            visitedVertices.insert(currentId); // mark vertex as visited
            Vertex* currentVertex = g->vertices[currentId];

            // iterating through the neighbors of currentVertex and adding to the stack those that haven't been visited yet.
            for(auto iter = currentVertex->neighbors.begin(); iter != currentVertex->neighbors.end(); ++iter)
            { 
                if(visitedVertices.find(iter->first) == visitedVertices.end())
                    stack.push_back(iter->first);
            }
        }
    }

    if(notFound)
        std::cout << "Could not find " << searchId << " in the graph :(\n";
}


int main()
{
    Vertex v1 = Vertex(1, 100);
    Vertex v2 = Vertex(2, 200);
    Graph g = Graph(&v1);

    g.addVertex(&v1);
    g.addVertex(&v2);

    v1.addNeighbor(&v2, 1000);

    breadthFirstSearch(&g, 2);

    return 0;
}
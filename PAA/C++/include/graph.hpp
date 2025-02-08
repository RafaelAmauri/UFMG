#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <list>

#include "vertex.hpp"


class Graph
{
    public:
        Vertex *root;
        std::unordered_map<int, Vertex*> vertices;

        // Class constructor
        Graph(Vertex *root)
        {
            this->root = root;
            this->vertices[root->id] = root;
        }
    
        
        void addVertex(Vertex *v)
        {
            this->vertices[v->id] = v;
        }


        void addEdge(Vertex *src, Vertex *dest, int weight)
        {
            src->neighbors[dest->id] = weight;
            dest->neighbors[src->id] = weight;
        }

        void printGraph()
        {
            std::list<int> stack;
            stack.push_front(this->root->id);
            std::unordered_set<int> visitedVertices;

            while(stack.size() > 0)
            {
                int currentId = stack.front();
                stack.pop_front();
                visitedVertices.insert(currentId);
    
                // iterating through the neighbors of currentVertex and adding to the stack those that haven't been visited yet.
                for(auto iter = this->vertices[currentId]->neighbors.begin(); iter != this->vertices[currentId]->neighbors.end(); ++iter)
                { 
                    // if not visited
                    if(visitedVertices.find(iter->first) == visitedVertices.end())
                    {
                        std::cout << currentId << " -- " << iter->first << " // W = " << iter->second << "\n";
                        stack.push_back(iter->first);
                    }
                }
                
            }
        }
};
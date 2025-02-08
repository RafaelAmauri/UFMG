#include <iostream>
#include <unordered_map>


class Vertex
{
    public:
        int id;
        int value;
        std::unordered_map<int, int> neighbors;

        // Class constructor
        Vertex(int vertexId, int vertexValue)
        {
            this->id    = vertexId;
            this->value = vertexValue;
        }

        Vertex(int vertexId)
        {
            this->id    = vertexId;
            this->value = 0;
        }
};
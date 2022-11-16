using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms;

public class Graph
{
    private record class Edge(int ToNode, int Cost);
    private readonly bool isDirected;
    private readonly List<Edge>[] edges;
    private readonly bool[] visited;
    public Graph(int numNodes, bool isDirected)
    {
        this.isDirected = isDirected;
        this.edges = new List<Edge>[numNodes];
        this.visited = new bool[numNodes];
        for (int i = 0; i < numNodes; i++)
        {
            visited[i] = false;
            edges[i] = new();
        }
    }
    public void AddPath(int node1, int node2, int cost)
    {
        edges[node1].Add(new(node2, cost));
        if (!isDirected)
            edges[node2].Add(new(node1, cost));
    }
    public long ShortestPath(int start, int end)
    {
        List<Edge> queue = new();
        queue.Add(new(start, 0));

        while (queue[0].ToNode != end)
        {
            int next = queue[0].ToNode;
            int priority = queue[0].Cost;
            visited[next] = true;
            foreach (Edge edge in edges[next])
            {
                if (!visited[edge.ToNode])
                {
                    bool found = false;
                    for (int i = 0; i < queue.Count; i++)
                    {
                        if (queue[i].ToNode == edge.ToNode)
                        {
                            found = true;
                            if (queue[i].Cost > priority + edge.Cost)
                                queue[i] = new(queue[i].ToNode, priority + edge.Cost);
                        }
                    }
                    if (!found)
                        queue.Add(new(edge.ToNode, priority + edge.Cost));
                }
            }
            queue.RemoveAt(0);
            if (queue.Count == 0)
                return -1;
            queue = queue.OrderBy(t => t.Cost).ToList<Edge>();
        }
        return queue[0].Cost;
    }
}

using System;
using System.Collections.Generic;

namespace Algorithms
{
    public class Graph<T>    {
        private class Node
        {
            public Node(T tNode)
            {
                TNode = tNode;
                Edges = new List<Tuple<Node, long>>();
                Visited = false;
            }
            public T TNode { get; set; }
            public List<Tuple<Node, long>> Edges { get; set; }
            public bool Visited { get; private set; }
            public void AddEdge(Node dest, long cost)
            {
                Edges.Add(new Tuple<Node,long>(dest,cost));
            }
        }
        private List<Node> nodes;
        private readonly bool isDirected;
        public Graph(bool isDirected)
        {
            this.isDirected = isDirected;
            this.nodes = new List<Node>();
        }
        public void AddNode(T node)
        {
            nodes.Add(new Node(node));
        }
        public void AddPath(T node1, T node2, long cost)
        {
            Node n1 = nodes.Find(n => n.TNode.Equals(node1));
            Node n2 = nodes.Find(n => n.TNode.Equals(node2));
            n1.AddEdge(n2, cost);
            if (!isDirected)
                n2.AddEdge(n1, cost);
        }
        public long ShortestPath(T start, T end)
        {
            long priority;
            PriorityQueue<Node,long> queue = new();
            Node startNode = nodes.Find(n => n.TNode.Equals(start));
            queue.Enqueue(startNode, 0);

            while (!queue.Peek().TNode.Equals(end))
            {
                Node nextNode;
                queue.TryDequeue(out nextNode, out priority);
                while(nextNode.Visited)
                    queue.TryDequeue(out nextNode, out priority);
                foreach (Tuple<Node,long> edge in nextNode.Edges)
                {
                    if (!edge.Item1.Visited)
                        queue.Enqueue(edge.Item1, edge.Item2 + priority);
                }
                if (queue.Count == 0)
                    return -1;
            }
            queue.TryDequeue(out _, out priority);
            return priority;
        }
    }
}

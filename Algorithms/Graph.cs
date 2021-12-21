using System;
using System.Collections.Generic;
using System.Linq;

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
            public bool Visited { get; set; }
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
            List<Tuple<Node,long>> queue = new();
            Node startNode = nodes.Find(n => n.TNode.Equals(start));
            queue.Add(new(startNode, 0));

            while (!queue[0].Item1.TNode.Equals(end))
            {
                Node nextNode = queue[0].Item1;
                long priority = queue[0].Item2;
                nextNode.Visited = true;
                foreach (Tuple<Node,long> edge in nextNode.Edges)
                {
                    if (!edge.Item1.Visited)
                    {
                        bool found = false;
                        for (int i = 0; i < queue.Count; i++)
                        {
                            if (queue[i].Item1.Equals(edge.Item1))
                            {
                                found = true;
                                if (queue[i].Item2 > priority + edge.Item2)
                                    queue[i] = new(queue[i].Item1, priority + edge.Item2);
                            }
                        }
                        if (!found)
                            queue.Add(new(edge.Item1, priority + edge.Item2));
                    }
                }
                queue.RemoveAt(0);
                if (queue.Count == 0)
                    return -1;
                queue = queue.OrderBy(t => t.Item2).ToList<Tuple<Node,long>>();
            }
            return queue[0].Item2;
        }
    }
}

using Algorithms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ConstrainedExecution;
using System.Xml;
using System.Xml.Schema;

namespace AdventOfCode
{
    class Node
    {
        public string Name { get; private set; }
        public List<Node> Connections { get; set; }
        public int Flow { get; set; }
        public Node(string name)
        {
            Name = name;
            Connections = new();
        }
    }
    class Program
    {
        static Dictionary<Node, List<KeyValuePair<Node, int>>> shortest;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Node> allNodes = new();
            Node start = null;
            for (int i = 0; i < lines.Length; i++)
            {
                Node node;
                string[] s = lines[i].Split(' ');
                node = new(s[1]);
                allNodes.Add(node);
                if (i == 0)
                {
                    start = node;
                }
                string f = s[4].Substring(5);
                node.Flow = int.Parse(f.Substring(0, f.Length - 1));
                for (int j = 9; j < s.Length; j++)
                {
                    string to = s[j].Substring(0, 2);
                    foreach (Node n in allNodes)
                    {
                        if (n.Name == to)
                        {
                            n.Connections.Add(node);
                            node.Connections.Add(n);
                        }
                    }
                }
            }


            List<Node> nonZeros = new();
            foreach (Node n in allNodes)
            {
                if (n.Flow != 0)
                    nonZeros.Add(n);
            }

            shortest = new();
            foreach (Node n1 in nonZeros)
            {
                foreach (Node n2 in nonZeros)
                {
                    if (n1 != n2)
                    {
                        int c = ShortestPath(n1, n2);
                        if (!shortest.ContainsKey(n1))
                        {
                            shortest.Add(n1, new List<KeyValuePair<Node, int>>());
                        }
                        shortest[n1].Add(new KeyValuePair<Node, int>(n2, c));
                    }
                }
            }

            int best = 0;
            foreach (Node n in allNodes)
            {
                if (n.Name == "AA")
                    start = n;
            }
            foreach (Node n in nonZeros)
            {
                int dist = ShortestPath(start, n);
                int time = 30 - dist;
                int run = Traverse(n, time, 0, best, nonZeros.ToList());
                best = Math.Max(best, run);
            }

            Console.WriteLine(best);



            int num = (int)Math.Pow(2, nonZeros.Count);
            best = 0;
            for (int i = 0; i < num; i++)
            {
                List<Node> my = new();
                List<Node> his = new();
                for (int j = 0; j < nonZeros.Count; j++)
                {
                    if ((i & (1 << j)) > 0)
                        my.Add(nonZeros[j]);
                    else
                        his.Add(nonZeros[j]);
                }
                if (i % 100 == 0)
                    Console.WriteLine("Num " + i);
                // Anohter heuristics - Let's assume that one visits at most four more nodes than the other one
                if (Math.Abs(my.Count - his.Count) > 4)
                    continue;

                int myBest = 0;
                foreach (Node n in my)
                {
                    int dist = ShortestPath(start, n);
                    int run = Traverse(n, 30 - dist - 4, 0, myBest, my.ToList());
                    myBest = Math.Max(myBest, run);
                }
                int hisBest = 0;
                foreach (Node n in his)
                {
                    int dist = ShortestPath(start, n);
                    int run = Traverse(n, 30 - dist - 4, 0, hisBest, his.ToList());
                    hisBest = Math.Max(hisBest, run);
                }
                if (best < hisBest + myBest)
                    Console.WriteLine(hisBest + myBest);
                best = Math.Max(best, hisBest + myBest);
            }
            Console.WriteLine(best);
        }

        private static int Traverse(Node node, int time, int flow, int best, List<Node> remaining)
        {
            if (--time == 0)
                return flow;
            int newFlow = flow + node.Flow * time;
            // Some kind of heuristics to decide if we can find a better solution
            if (25 * (remaining.Count - 1) * (time - 2) + newFlow < best)
                return flow;
            int newBest = Math.Max(best, newFlow);
            remaining.Remove(node);
            int total = newFlow;
            foreach (KeyValuePair<Node, int> pair in shortest[node])
            {
                if (!remaining.Exists(x => x == pair.Key))
                    continue;
                if (time <= pair.Value)
                    continue;
                int newTime = time - pair.Value;
                total = Math.Max(total, Traverse(pair.Key, newTime, newFlow, newBest, remaining.ToList()));
            }
            remaining.Add(node);
            return total;
        }

        private static int GetNode(string name)
        {
            return name[0] - 'A' * 28 + name[1] - 'A';
        }

        private static int ShortestPath(Node start, Node end)
        {
            List<Node> visited = new();
            PriorityQueue<Node, int> queue = new PriorityQueue<Node, int>();
            queue.Enqueue(start, 0);
            while (true)
            {

                Node node;
                int c;
                queue.TryDequeue(out node, out c);
                if (node == end)
                    return c;
                if (!visited.Exists(x => x == node))
                {
                    foreach (Node next in node.Connections)
                    {
                        queue.Enqueue(next, c + 1);
                    }
                }
            }
        }
    }
}

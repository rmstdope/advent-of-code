using System;
using System.Collections.Generic;

namespace Day_12
{
    class Program
    {
        class Node
        {
            public bool isStart;
            public bool isEnd;
            public bool isLarge;
            public int visited;
            public string name;
            public List<Node> connections;
        }
        static int FindPaths(Node n, bool visitedSmallTwice)
        {
            if (n.visited == 2 && !n.isLarge)
                return 0;
            if (n.visited == 1 && !n.isLarge && visitedSmallTwice)
                return 0;
            int num = 0;
            if (n.isEnd)
                num++;
            bool vst = visitedSmallTwice || (n.visited == 1 && !n.isLarge);
            n.visited++;
            foreach (Node n2 in n.connections)
            {
                num += FindPaths(n2, vst);
            }
            n.visited--;
            return num;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Node> nodes = new List<Node>();
            foreach(string line in lines)
            {
                string[] path = line.Split('-');
                if (path[0] == "start" || path[0] == "end")
                {
                    string t = path[0];
                    path[0] = path[1];
                    path[1] = t;
                }
                if (!nodes.Exists(x => x.name == path[0]))
                {
                    Node node = new Node();
                    node.isEnd = false;
                    node.isStart = false;
                    node.visited = 0;
                    node.name = path[0];
                    node.isLarge = (path[0][0] >= 'A' && path[0][0] <= 'Z');
                    node.connections = new List<Node>();
                    nodes.Add(node);
                    if (path[1] == "start")
                        node.isStart = true;
                    if (path[1] == "end")
                        node.isEnd = true;
                }
                if (path[1] != "start" && path[1] != "end")
                {
                    if(!nodes.Exists(x => x.name == path[1]))
                    {
                        Node node = new Node();
                        node.isEnd = false;
                        node.isStart= false;
                        node.name = path[1];
                        node.visited = 0;
                        node.isLarge = (path[1][0] >= 'A' && path[1][0] <= 'Z');
                        node.connections = new List<Node>();
                        nodes.Add(node);
                    }
                    Node n1 = nodes.Find(x => x.name == path[0]);
                    Node n2 = nodes.Find(x => x.name == path[1]);
                    n2.connections.Add(n1);
                    n1.connections.Add(n2);
                }
                else if (path[1] == "end")
                {
                    Node n = nodes.Find(x => x.name == path[0]);
                    n.isEnd = true;
                }
                else if (path[1] == "start")
                {
                    Node n = nodes.Find(x => x.name == path[0]);
                    n.isStart = true;
                }
            }
            int paths = 0;
            foreach (Node n in nodes)
            {
                if (n.isStart)
                {
                    paths += FindPaths(n, false);
                }
            }
            Console.WriteLine(paths);
        }
    }
}

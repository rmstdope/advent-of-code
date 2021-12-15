using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_15
{
    class Pos
    {
        public int risk;
        public bool visited;
    }
    class Node
    {
        public int index;
        public int cost;
    }
    class Program
    {
        private static int maxX;
        private static int maxY;
        private static Pos[] positions;
        private static List<Node> nodes;
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            maxX = lines[0].Length;
            maxY = lines.Length;
            minCost = 100000;
            Pos[] original = new Pos[maxX * maxY];
            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    Pos p = new Pos();
                    p.risk = lines[y][x] - '0';
                    p.visited = false;
                    original[y * maxX + x] = p;
                }
            }
            int mx = maxX;
            int my = maxY;
            maxX *= 5;
            maxY *= 5;
            positions = new Pos[maxX * maxY];
            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    Pos p = new Pos();
                    Pos p2;
                    if (x < mx && y < my)
                    {
                        p2 = original[y * mx + x];
                        p.risk = p2.risk;
                    }
                    else if (x >= mx)
                    {
                        p2 = positions[y * maxX + x - mx];
                        p.risk = p2.risk == 9 ? 1 : p2.risk + 1;
                    }
                    else
                    {
                        p2 = positions[(y - my) * maxX + x];
                        p.risk = p2.risk == 9 ? 1 : p2.risk + 1;
                    }
                    p.visited = false;
                    positions[y * maxX + x] = p;
                }
            }
            nodes = new List<Node>();
            Node node = new Node();
            node.index = 0;
            node.cost = 0;
            nodes.Add(node);
            while (true)
            {
                nodes = nodes.OrderBy(n => n.cost).ToList();
                Node n = nodes[0];
                nodes.Remove(n);
                int fx = n.index % maxX;
                int fy = n.index / maxX;
                Pos p = positions[n.index];
                p.visited = true;
                if (fx == maxX - 1 && fy == maxY - 1)
                {
                    Console.WriteLine(n.cost);
                    break;
                }
                if (fx > 0)
                {
                    UpdateCosts(n, n.index - 1);
                }
                if (fy > 0)
                {
                    UpdateCosts(n, n.index - maxX);
                }
                if (fx < maxX - 1)
                {
                    UpdateCosts(n, n.index + 1);
                }
                if (fy < maxY - 1)
                {
                    UpdateCosts(n, n.index + maxX);
                }
            }
        }

        private static void UpdateCosts(Node n, int index)
        {
            Pos p2 = positions[index];
            if (!p2.visited)
            {
                Node newN = nodes.Find(q => q.index == index);
                if (newN != null)
                {
                    if (newN.cost > n.cost + p2.risk)
                        newN.cost = n.cost + p2.risk;
                }
                else
                {
                    newN = new Node();
                    newN.cost = n.cost + p2.risk;
                    newN.index = index;
                    nodes.Add(newN);
                }
            }
        }
    }
}

using Algorithms;
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
    class Program
    {
        private static int maxX;
        private static int maxY;
        private static Pos[] positions;
        static void Main(string[] _)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            maxX = lines[0].Length;
            maxY = lines.Length;
            Pos[] original = new Pos[maxX * maxY];
            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    Pos p = new();
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
                    Pos p = new();
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
            Graph graph = new(maxX * maxY, true);
            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    if (x < maxX - 1)
                    {
                        graph.AddPath(y * maxX + x, y * maxX + x + 1, positions[y * maxX + x + 1].risk);
                        graph.AddPath(y * maxX + x + 1, y * maxX + x, positions[y * maxX + x].risk);
                    }
                    if (y < maxY - 1)
                    {
                        graph.AddPath(y * maxX + x, (y + 1) * maxX + x, positions[(y + 1) * maxX + x].risk);
                        graph.AddPath((y + 1) * maxX + x, y * maxX + x, positions[y * maxX + x].risk);
                    }
                }
            }
            Console.WriteLine(graph.ShortestPath(0, maxY * maxX - 1));
        }
    }
}

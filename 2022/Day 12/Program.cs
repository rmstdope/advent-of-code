using System;

namespace AdventOfCode
{
    class Program
    {
        static string[] lines;
        static int[][] dist;
        static int endX, endY;
        static int best;
        static void Main()
        {
            lines = System.IO.File.ReadAllLines("../../../input.txt");
            dist = new int[lines.Length][];
            int startX = 0, startY = 0;
            best = 1000000;
            for(int y = 0; y < lines.Length; y++)
            {
                dist[y] = new int[lines[y].Length];
                for (int x = 0; x < lines[y].Length; x++)
                {
                    dist[y][x] = 1000000;
                    if (lines[y][x] == 'S')
                    {
                        startX = x;
                        startY = y;
                        lines[y] = lines[y].Substring(0, x) + 'a' + lines[y].Substring(x + 1);
                    }
                    if (lines[y][x] == 'E')
                    {
                        endX = x;
                        endY = y;
                        lines[y] = lines[y].Substring(0, x) + 'z' + lines[y].Substring(x + 1);
                    }
                }
            }
            Traverse(startY, startX, 0);
            Console.WriteLine(best);

            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++)
                {
                    if (lines[y][x] == 'a')
                    {
                        startY = y;
                        startX = x;
                        for (int y2 = 0; y2 < lines.Length; y2++)
                        {
                            for (int x2 = 0; x2 < lines[y2].Length; x2++)
                            {
                                dist[y2][x2] = 1000000;
                            }
                        }
                        Traverse(startY, startX, 0);
                    }
                }
            }
            Console.WriteLine(best);
        }

        private static void Traverse(int y, int x, int depth)
        {
            dist[y][x] = depth;
            if (x == endX && y == endY)
            {
                best = Math.Min(best, depth);
                return;
            }
            if (x > 0 && dist[y][x - 1] > depth + 1 &&
                (lines[y][x - 1] - lines[y][x] <= 1))
            {
                    Traverse(y, x - 1, depth + 1);
            }
            if (x < lines[y].Length - 1 && dist[y][x + 1] > depth + 1 &&
                (lines[y][x + 1] - lines[y][x] <= 1))
            {
                Traverse(y, x + 1, depth + 1);
            }
            if (y > 0 && dist[y - 1][x] > depth + 1 &&
                (lines[y - 1][x] - lines[y][x] <= 1))
            {
                Traverse(y - 1, x, depth + 1);
            }
            if (y < lines.Length - 1 && dist[y + 1][x] > depth + 1 &&
                (lines[y + 1][x] - lines[y][x] <= 1))
            {
                Traverse(y + 1, x, depth + 1);
            }
        }
    }
}

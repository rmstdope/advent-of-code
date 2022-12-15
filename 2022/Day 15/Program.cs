using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;

namespace AdventOfCode
{
    class Program
    {
        static public List<int[]> pairs = new();
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            for (int i = 0;i < lines.Length;i++)
            {
                string[] div = lines[i].Split(' ');
                int[] pair = new int[5];
                pair[0] = int.Parse(div[2].Substring(2, div[2].Length - 3));
                pair[1] = int.Parse(div[3].Substring(2, div[3].Length - 3));
                pair[2] = int.Parse(div[8].Substring(2, div[8].Length - 3));
                pair[3] = int.Parse(div[9].Substring(2));
                pair[4] = Math.Abs(pair[2] - pair[0]) + Math.Abs(pair[3] - pair[1]);
                pairs.Add(pair);
            }
            int num = 0;
            int yRow = 2000000;
            //int yRow = 10;
            for (int x = -5000000; x < 6000000; x++)
            {
                bool couldBe = true;
                foreach (int[] pair in pairs)
                {
                    int d1 = Math.Abs(x - pair[0]) + Math.Abs(yRow - pair[1]);
                    int d2 = Math.Abs(pair[2] - pair[0]) + Math.Abs(pair[3] - pair[1]);
                    bool same = pair[2] == x && pair[3] == yRow;
                    if (d1 <= d2 && !same)
                        couldBe = false;
                }
                if (!couldBe)
                    num++;
            }
            Console.WriteLine(num);

            int maxTest = 4000000;
            //int maxTest = 20;
            List<int[]> intersects = new List<int[]>();
            int[] start = new int[2];
            for (int y = 0; y < maxTest; y++)
            {
                intersects.Clear();
                start[0] = 0;
                start[1] = maxTest;
                intersects.Add(start);
                foreach (int[] pair in pairs)
                {
                    int dY = Math.Abs(y - pair[1]);
                    int xRest = pair[4] - dY;
                    if (xRest > 0)
                    {
                        int[] ranges = new int[4];
                        ranges[0] = 0;
                        ranges[1] = pair[0] - xRest - 1;
                        ranges[2] = pair[0] + xRest + 1;
                        ranges[3] = maxTest;
                        Intersect(intersects, ranges);
                    }
                }
                if (intersects.Count > 0)
                {
                    Int64 g = (Int64)intersects[0][0] * 4000000 + (Int64)y;
                    Console.WriteLine(g);
                }
            }
        }

        private static void Intersect(List<int[]> intersects, int[] ranges)
        {
            List<int[]> newIntersects = new();
            foreach (int[] inter in intersects)
            {
                int[] newIntersect = new int[2];
                if (ranges[1] >= ranges[0])
                {
                    int[] x = new int[2];
                    x[0] = Math.Max(inter[0], ranges[0]);
                    x[1] = Math.Min(inter[1], ranges[1]);
                    if (x[0] <= x[1])
                        newIntersects.Add(x);
                }
                if (ranges[2] <= ranges[3])
                {
                    int[] x = new int[2];
                    x[0] = Math.Max(inter[0], ranges[2]);
                    x[1] = Math.Min(inter[1], ranges[3]);
                    if (x[0] <= x[1])
                        newIntersects.Add(x);
                }
            }
            intersects.Clear();
            intersects.AddRange(newIntersects);
        }
    }
}

using System;
using System.Collections.Generic;
using System.Numerics;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<int> visited = new List<int>();
            int[] x = new int[10];
            int[] y = new int[10];
            for (int i = 0; i < 10; i++)
            {
                x[i] = 0;
                y[i] = 0;
            }
            visited.Add(0);
            foreach (string line in lines) 
            {
                string[] cmd = line.Split(' ');
                int num = int.Parse(cmd[1]);
                for (int i = 0; i < num; i++)
                {
                    Move(ref x[0], ref y[0], cmd[0][0]);
                    Follow(ref x[0], ref y[0], ref x[1], ref y[1]);
                    if (!visited.Exists(v => v == x[1] + y[1] * 65536))
                    {
                        visited.Add(x[1] + y[1] * 65536);
                    }
                }
            }
            Console.WriteLine(visited.Count);

            for (int i = 0; i < 10; i++)
            {
                x[i] = 0;
                y[i] = 0;
            }
            visited.Clear();
            visited.Add(0);
            foreach (string line in lines)
            {
                string[] cmd = line.Split(' ');
                int num = int.Parse(cmd[1]);
                for (int i = 0; i < num; i++)
                {
                    Move(ref x[0], ref y[0], cmd[0][0]);
                    Follow(ref x[0], ref y[0], ref x[1], ref y[1]);
                    for (int j = 1; j < 9; j++)
                    {
                        Follow(ref x[j], ref y[j], ref x[j + 1], ref y[j + 1]);
                    }
                    if (!visited.Exists(v => v == x[9] + y[9] * 65536))
                    {
                        visited.Add(x[9] + y[9] * 65536);
                    }
                }
            }
            Console.WriteLine(visited.Count);
        }

        private static void Follow(ref int hX, ref int hY, ref int tX, ref int tY)
        {
            int dX = hX - tX;
            int dY = hY - tY;
            if (int.Abs(dX) > 1 || int.Abs(dY) > 1)
            {
                if (dX > 0)
                {
                    tX++;
                }
                if (dX < 0)
                {
                    tX--;
                }
                if (dY > 0)
                {
                    tY++;
                }
                if (dY < 0)
                {
                    tY--;
                }
            }

        }

        private static void Move(ref int hX, ref int hY,char cmd)
        {
            switch (cmd)
            {
                case 'R':
                    hX++;
                    break;
                case 'L':
                    hX--;
                    break;
                case 'U':
                    hY++;
                    break;
                case 'D':
                    hY--;
                    break;
            }
        }
    }
}

using System;
using System.Runtime.CompilerServices;
using System.Runtime.Versioning;
using System.Security.Cryptography;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int count = 0;
            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++)
                {
                    bool visible = true;
                    for (int x2 = 0; x2 < x; x2++)
                    {
                        if (lines[y][x] <= lines[y][x2])
                            visible = false;
                    }
                    if (visible)
                    {
                        count++;
                        continue;
                    }
                    visible = true;
                    for (int x2 = x + 1; x2 < lines[y].Length; x2++)
                    {
                        if (lines[y][x] <= lines[y][x2])
                            visible = false;
                    }
                    if (visible)
                    {
                        count++;
                        continue;
                    }
                    visible = true;
                    for (int y2 = 0; y2 < y; y2++)
                    {
                        if (lines[y][x] <= lines[y2][x])
                            visible = false;
                    }
                    if (visible)
                    {
                        count++;
                        continue;
                    }
                    visible = true;
                    for (int y2 = y + 1; y2 < lines.Length; y2++)
                    {
                        if (lines[y][x] <= lines[y2][x])
                            visible = false;
                    }
                    if (visible)
                    {
                        count++;
                    }
                }
            }
            Console.WriteLine(count);
            int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
            int max = 0;
            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++)
                {
                    c1 = 0;
                    int h = lines[y][x];
                    for (int x2 = x - 1; x2 >= 0; x2--)
                    {
                        c1++;
                        if (lines[y][x2] >= h)
                            break;
                    }
                    c2 = 0;
                    h = lines[y][x];
                    for (int x2 = x + 1; x2 < lines[y].Length; x2++)
                    {
                        c2++;
                        if (lines[y][x2] >= h)
                            break;
                    }
                    c3 = 0;
                    h = lines[y][x];
                    for (int y2 = y - 1; y2 >= 0; y2--)
                    {
                        c3++;
                        if (lines[y2][x] >= h)
                            break;
                    }
                    c4 = 0;
                    h = lines[y][x];
                    for (int y2 = y + 1; y2 < lines.Length; y2++)
                    {
                        c4++;
                        if (lines[y2][x] >= h)
                            break;
                    }
                    if (c1 * c2 * c3 * c4 > max)
                        max = c1 * c2 * c3 * c4;
                }
            }
            Console.WriteLine(max);
        }
    }
}

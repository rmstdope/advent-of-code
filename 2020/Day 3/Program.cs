using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            Console.WriteLine(Traverse(lines, 3, 1));
            Int64 p = Traverse(lines, 1, 1);
            p *= Traverse(lines, 3, 1);
            p *= Traverse(lines, 5, 1);
            p *= Traverse(lines, 7, 1);
            p *= Traverse(lines, 1, 2);
            Console.WriteLine(p);
            }

        private static int Traverse(string[] lines, int xAdd, int yAdd)
        {
            int x = 0;
            int y = 0;
            int num = 0;
            int width = lines[0].Length;
            do
            {
                if (lines[y][x % width] == '#')
                    num++;
                x += xAdd;
                y += yAdd;
            } while (y < lines.Length);
            return num;
        }
    }
}

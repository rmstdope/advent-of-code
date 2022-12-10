using System;
using System.Diagnostics.CodeAnalysis;
using System.Runtime.CompilerServices;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int str = 1;
            int sum = 0;
            int i = 0;
            int s = 0;
            int cycle = 0;
            string[] crt = new string[6];
            while (cycle <= 239)
            {
                int y = cycle / 40;
                int x = cycle % 40;
                if (x == (str - 1) || x == (str + 0) || x == (str + 1))
                {
                    if (y < 6)
                        crt[y] += "#";
                }
                else
                {
                    if (y < 6)
                        crt[y] += ".";
                }

                cycle++;
                if (cycle == 20 || cycle == 60 || cycle == 100 || cycle == 140 || cycle == 180 || cycle == 220)
                {
                    sum += cycle * str;
                }
                string[] cmd = lines[i].Split(' ');
                if (cmd[0] == "addx")
                {
                    if (s == 1)
                    {
                        str += int.Parse(cmd[1]);
                        i++;
                        s = 0;
                    }
                    else
                    {
                        s = 1;
                    }
                }
                else
                {
                    i++;
                }
            }

            Console.WriteLine(sum);
            for (int j = 0; j < 6; j++)
            {
                Console.WriteLine(crt[j]);
            }
        }
    }
}

using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        class Board
        {
            public int[] numbers;
            public bool[] taken;
            public bool won;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int[] board = new int[1000 * 1000];
            for (int i = 0; i < 1000*1000; i++)
            {
                board[i] = 0;
            }
            foreach (string line in lines)
            {
                string[] s = line.Split(' ');
                string[] s0 = s[0].Split(',');
                string[] s2 = s[2].Split(',');
                int x1 = Int32.Parse(s0[0]);
                int y1 = Int32.Parse(s0[1]);
                int x2 = Int32.Parse(s2[0]);
                int y2 = Int32.Parse(s2[1]);
                if (y1 != y2 && x1 != x2)
                {
                    int x;
                    if (y1 < y2)
                        x = x1;
                    else
                        x = x2;
                    for (int y = Math.Min(y1, y2); y <= Math.Max(y1, y2); y++)
                    {
                        board[y * 1000 + x]++;
                        if (y1 < y2)
                        {
                            if (x1 < x2)
                            {
                                x++;
                            }
                            else
                            {
                                x--;
                            }
                        }
                        else
                        {
                            if (x1 < x2)
                            {
                                x--;
                            }
                            else
                            {
                                x++;
                            }
                        }
                    }
                }
                else
                {
                    for (int y = Math.Min(y1, y2); y <= Math.Max(y1, y2); y++)
                    {
                        for (int x = Math.Min(x1, x2); x <= Math.Max(x1, x2); x++)
                        {
                            board[y * 1000 + x]++;
                        }
                    }
                }
            }
            int num = 0;
            for (int i = 0; i < 1000 * 1000; i++)
            { 
                if (board[i] > 1)
                {
                    num++;
                }
            }
            //Console.WriteLine("O2 : " + o2 + ", CO2: " + co2);
            Console.WriteLine(num);
        }
    }
}

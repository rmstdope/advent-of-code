using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        class Fish
        {
            public int[] numbers;
            public bool[] taken;
            public bool won;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            string[] nums = lines[0].Split(',');
            int[] pos = new int[nums.Length];
            for(int i = 0; i < nums.Length; i++)
            {
                pos[i] = Int32.Parse(nums[i]);
            }
            int max = 0;
            foreach(int p in pos)
            {
                if (p > max)
                    max = p;
            }
            int minCost = 1000000000;
            int minPos = 0;
            for (int i = 0; i <= max; i++)
            {
                int cost = 0;
                foreach(int p in pos)
                {
                    int x = Math.Abs(p - i);
                    for (int y = 0; y < x; y++)
                        cost += (y + 1);
                }
                if (cost < minCost)
                {
                    minCost = cost;
                    minPos = i;
                }
            }
            Console.WriteLine(minCost + "," + minPos);
        }
    }
}

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
            string[] ages = lines[0].Split(',');
            Int64[] totals = new Int64[9];
            for (int i = 0; i < 9; i++)
            {
                totals[i] = 0;
            }
            foreach (string age in ages)
            {
                totals[Int64.Parse(age)]++;
            }
            for (int i = 0; i < 256; i++)
            {
                Int64 numNew = totals[0];
                for (int f = 1; f < 9; f++)
                {
                    totals[f - 1] = totals[f];
                }
                totals[8] = numNew;
                totals[6] += numNew;
                /*foreach (int fish in fishes)
                {
                    Console.Write(fish + ",");
                }
                Console.WriteLine();*/
            }
            //Console.WriteLine("O2 : " + o2 + ", CO2: " + co2);
            Int64 sum = 0;
            foreach (Int64 f in totals)
            {
                sum += f;
            }
            Console.WriteLine(sum);
        }
    }
}

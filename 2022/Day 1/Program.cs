using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            List<int> calories = new();
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int sum = 0;
            for (int i = 0; i < lines.Length; i++)
            {
                if (lines[i] == "")
                {
                    calories.Add(sum);
                    sum = 0;
                }
                else
                {
                    sum += int.Parse(lines[i]);
                }
            }
            calories.Add(sum);
            calories.Sort();
            Console.WriteLine(calories[calories.Count - 1]);
            Console.WriteLine(calories[calories.Count - 1] + calories[calories.Count - 2] + calories[calories.Count - 3]);
        }
    }
}

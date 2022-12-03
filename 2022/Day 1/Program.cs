using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            //string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            //List<string> l2 = System.IO.File.ReadAllLines("../../../input.txt").ToList<string>();
            string t = System.IO.File.ReadAllText("../../../input.txt");
            List<int> calories = new();
            foreach (string s in t.Split("\r\n\r\n"))
            {
                int[] c = Array.ConvertAll(s.Split("\r\n"), int.Parse);
                calories.Add(c.Sum());
            }
            calories.Sort();
            calories.Reverse();
            Console.WriteLine(calories[0]);
            Console.WriteLine(calories.GetRange(0, 3).Sum());
        }
    }
}

using System;

namespace Day_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int last = 10000;
            int num = 0;
            for (int i = 0; i < lines.Length - 2; i++)
            {
                int current = Int32.Parse(lines[i]) + Int32.Parse(lines[i + 1]) + Int32.Parse(lines[i + 2]);
                if (last < current)
                {
                    num++;
                }
                last = current;
            }
            Console.WriteLine(num);
        }
    }
}

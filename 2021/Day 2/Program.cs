using System;

namespace Day_2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int horizontal = 0;
            int depth = 0;
            int aim = 0;
            for (int i = 0; i < lines.Length; i++)
            {
                if (lines[i].Substring(0, 2) == "up")
                {
                    aim -= Int32.Parse(lines[i].Substring(3));
                }
                else if (lines[i].Substring(0, 4) == "down")
                {
                    aim += Int32.Parse(lines[i].Substring(5));
                }
                else if (lines[i].Substring(0, 7) == "forward")
                {
                    horizontal += Int32.Parse(lines[i].Substring(8));
                    depth += aim * Int32.Parse(lines[i].Substring(8));
                }
                else
                {
                    throw new Exception("Error");
                }
            }
            Console.WriteLine("Depth : " + depth + ", horizontal : " + horizontal);
            Console.WriteLine(depth * horizontal);
        }
    }
}

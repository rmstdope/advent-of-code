using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");

            Calculate(lines, 4);
            Calculate(lines, 14);
        }

        private static void Calculate(string[] lines, int count)
        {
            for (int i = count - 1; i < lines[0].Length; i++)
            {
                bool found = true;
                for (int j = 0; j < count - 1; j++)
                {
                    for (int k = j + 1; k < count; k++)
                    {
                        if (lines[0][i - j] == lines[0][i - k])
                            found = false;
                    }
                }
                if (found)
                {
                    Console.WriteLine(i + 1);
                    break;
                }
            }
        }
    }
}

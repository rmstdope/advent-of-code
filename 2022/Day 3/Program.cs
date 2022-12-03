using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int sum = 0;
            foreach (string line in lines)
            {
                string had = "";
                string s1 = line.Substring(0, line.Length / 2);
                string s2 = line.Substring(line.Length / 2);
                foreach (char c in s1)
                {
                    if (!had.Contains(c) && s2.Contains(c))
                    {
                        sum += GetPrio(c);
                        had = had + c;
                    }
                }
            }
            Console.WriteLine(sum);
            sum = 0;
            for (int i = 0; i < lines.Length; i += 3)
            {
                string had = "";
                foreach (char c in lines[i])
                {
                    if (!had.Contains(c) && lines[i + 1].Contains(c) && lines[i + 2].Contains(c))
                    {
                        sum += GetPrio(c);
                        had= had + c;
                    }
                }

            }
            Console.WriteLine(sum);
        }
        private static int GetPrio(char c)
        {
            if (c <= 'Z')
                return c - 'A' + 27;
            return c - 'a' + 1;
        }
    }
}

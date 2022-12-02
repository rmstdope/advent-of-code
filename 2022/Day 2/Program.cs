using System;
using System.Diagnostics.CodeAnalysis;

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
                int p = GetPoints(line[0], line[2]);
                sum += p;

            }
            Console.WriteLine(sum);

            sum = 0;
            foreach (string line in lines)
            {
                char x = 'a';
                if (line[2] == 'X')
                {
                    if (line[0] == 'A')
                        x = 'Z';
                    if (line[0] == 'B')
                        x = 'X';
                    if (line[0] == 'C')
                        x = 'Y';
                }
                if (line[2] == 'Y')
                {
                    if (line[0] == 'A')
                        x = 'X';
                    if (line[0] == 'B')
                        x = 'Y';
                    if (line[0] == 'C')
                        x = 'Z';
                }
                if (line[2] == 'Z')
                {
                    if (line[0] == 'A')
                        x = 'Y';
                    if (line[0] == 'B')
                        x = 'Z';
                    if (line[0] == 'C')
                        x = 'X';
                }
                int p = GetPoints(line[0], x);
                sum += p;

            }


            Console.WriteLine(sum);
        }

        private static int GetPoints(char l1, char l2)
        {
            int p = 0;
            if (l2 == 'X')
            {
                p += 1;
                if (l1 == 'A')
                    p += 3;
                if (l1 == 'B')
                    p += 0;
                if (l1 == 'C')
                    p += 6;
            }
            if (l2 == 'Y')
            {
                p += 2;
                if (l1 == 'A')
                    p += 6;
                if (l1 == 'B')
                    p += 3;
                if (l1 == 'C')
                    p += 0;
            }
            if (l2 == 'Z')
            {
                p += 3;
                if (l1 == 'A')
                    p += 0;
                if (l1 == 'B')
                    p += 6;
                if (l1 == 'C')
                    p += 3;
            }

            return p;
        }
    }
}

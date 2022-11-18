using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            Int64[] ints= new Int64[lines.Length];
            Int64 answer = 0;
            for (int i = 0;i < lines.Length; i++)
            {
                ints[i] = Int64.Parse(lines[i]);
            }
            int preamble = 25;
            for (int i = 0; i < lines.Length - preamble; i++)
            {
                if (!CheckIfValid(ints, i, preamble))
                {
                    answer = ints[i + preamble];
                    Console.WriteLine(answer);
                }
            }

            for (int i = 0; i < ints.Length; i++)
            {
                Int64 sum = 0;
                for (int j = i; j < ints.Length; j++)
                {
                    sum += ints[j];
                    if (sum == answer && i != j)
                    {
                        Int64 min = ints[j];
                        Int64 max = ints[j];
                        for (int k = i;k < j + 1; k++)
                        {
                            min = Math.Min(ints[k], min);
                            max = Math.Max(ints[k], max);
                        }
                        Console.WriteLine(min + max);
                    }
                }
            }
            //Console.WriteLine("Hello World!");
        }

        private static bool CheckIfValid(Int64[] ints, int start, int preamble)
        {
            for (int i = start; i < start + preamble - 1; i++)
            {
                for (int j = i + 1; j < start + preamble; j++)
                {
                    if (ints[i] + ints[j] == ints[start + preamble])
                        return true;
                }
            }
            return false;
        }
    }
}

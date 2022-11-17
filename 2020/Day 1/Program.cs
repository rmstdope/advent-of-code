using System;
using System.Globalization;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            for (int i = 0;i < lines.Length;i++)
            {
                Int32 iNum = Int32.Parse(lines[i]);
                for (int j = i + 1; j < lines.Length; j++)
                {
                    Int32 jNum = Int32.Parse(lines[j]);
                    if (iNum + jNum == 2020)
                    {
                        Console.WriteLine(iNum * jNum);
                    }
                    for (int k = j + 1; k < lines.Length; k++)
                    {
                        Int32 kNum = Int32.Parse(lines[k]);
                        if (iNum + jNum + kNum == 2020)
                        {
                            Console.WriteLine(iNum * jNum * kNum);
                        }
                    }
                }
            }
        }
    }
}

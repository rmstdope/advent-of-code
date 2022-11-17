using System;
using System.Collections.Generic;
using System.Text;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] answer;
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<string> result = new();
            int sum = 0;
            int sum2 = 0;
            foreach (string line in lines)
            {
                if (line.Length == 0)
                {
                    answer = CrossRef(result);
                    sum += answer[0].Length;
                    sum2 += answer[1].Length;
                    //Console.WriteLine(answer.Length);
                    result = new();
                }
                else
                {
                    result.Add(line);
                }
            }
            answer = CrossRef(result);
            sum += answer[0].Length;
            sum2 += answer[1].Length;
            //Console.WriteLine(answer.Length);
            Console.WriteLine(sum);
            Console.WriteLine(sum2);
        }

        private static string[] CrossRef(List<string> result)
        {
            bool[] f = new bool[28];
            bool[] f2 = new bool[28];
            bool[] f3 = new bool[28];
            for (int i = 0;i < 28; i++)
            {
                f[i] = false;
                f2[i] = true;
            }
            foreach (string line in result)
            {
                for (int i = 0; i < 28; i++)
                {
                    f3[i] = false;
                }
                foreach (char c in line)
                {
                    f[c - 'a'] = true;
                    f3[c - 'a'] = f2[c - 'a'];
                }
                f3.CopyTo(f2, 0);
            }
            int n = 0;
            string ret = "";
            string ret2 = "";
            for (int i = 0; i < 28; i++)
            {
                if (f[i])
                {
                    ret = ret + (char)('a' + i);
                }
                if (f2[i])
                {
                    ret2 = ret2 + (char)('a' + i);
                }
            }
            return new string[] { ret, ret2 };
        }
    }
}

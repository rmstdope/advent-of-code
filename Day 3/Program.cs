using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        static int findValue(int bit, Boolean most, List<string> list)
        {
            List<string> newList = new List<string>();
            int ones = 0;
            foreach (string s in list)
            {
                if (s[bit] == '1')
                {
                    ones++;
                }
            }
            foreach (string s in list)
            {
                if (ones > list.Count / 2.0f)
                {
                    // One most common
                    if (s[bit] == '1' && most)
                    {
                        newList.Add(s);
                    }
                    else if (s[bit] == '0' && !most)
                    {
                        newList.Add(s);
                    }
                } 
                else if (ones == list.Count / 2.0f)
                {
                    // Equally
                    if (s[bit] == '1' && most)
                    {
                        newList.Add(s);
                    }
                    else if (s[bit] == '0' && !most)
                    {
                        newList.Add(s);
                    }
                }
                else
                {
                    // Zero most common
                    if (s[bit] == '0' && most)
                    {
                        newList.Add(s);
                    }
                    else if (s[bit] == '1' && !most)
                    {
                        newList.Add(s);
                    }
                }
            }
            if (newList.Count == 1)
            {
                int v = 0;
                for (int x = 0; x < 12; x++)
                {
                    int p = (int)Math.Pow(2, 11 - x);
                    if (newList[0][x] == '1')
                    {
                        v += p;
                    }
                }
                return v;

            }
            else
            {
                return findValue(bit + 1, most, newList);
            }
        }
        struct Board
        {
            int[][] numbers;
            Boolean[][] taken;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<string> list = new List<string>();
            foreach(string line in lines)
            {
                list.Add(line);
            }
            int co2 = findValue(0, false, list);
            int o2 = findValue(0, true, list);
            Console.WriteLine("O2 : " + o2 + ", CO2: " + co2);
            Console.WriteLine(o2 * co2);
        }
    }
}

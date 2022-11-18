using System;
using System.Collections.Generic;
using System.Reflection.Metadata;

namespace AdventOfCode
{
    class Adapter
    {
        public int Jolts { get; set; }
        public bool Used { get; set; }
        public Int64 NumParts { get; set; }
        public Adapter(int jolts)
        {
            Jolts = jolts;
            Used = false;
            NumParts = 0;
        }
    }
    class Program
    {
        private static Stack<Adapter> used = new();
        private static List<Adapter> adapters;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            adapters = new List<Adapter>();
            int max = 0;
            for (int i = 0; i < lines.Length; i++)
            {
                int v = int.Parse(lines[i]);
                adapters.Add(new Adapter(v));
                max = Math.Max(max, v);
            }
            adapters.Add(new Adapter(max + 3));
            adapters.Sort(delegate (Adapter x, Adapter y)
            {
                return x.Jolts - y.Jolts;
            });
            int ones = 0;
            int threes = 0;
            for (int i = 0; i < adapters.Count - 1; i++)
            {
                if (adapters[i + 1].Jolts - adapters[i].Jolts == 1)
                    ones++;
                if (adapters[i + 1].Jolts - adapters[i].Jolts == 3)
                    threes++;
            }
            if (adapters[0].Jolts == 1)
                ones++;
            if (adapters[0].Jolts == 3)
                threes++;
            Console.WriteLine(ones * threes);

            for (int i = 0; i < adapters.Count; i++)
            {
                Int64 num = 0;
                if (adapters[i].Jolts <= 3)
                    num++;
                for (int j = i - 1; j >= 0; j--)
                {
                    if (adapters[i].Jolts - adapters[j].Jolts <= 3)
                        num += adapters[j].NumParts;
                }
                adapters[i].NumParts = num;
            }
            Console.WriteLine(adapters[adapters.Count - 1].NumParts);

            //int num = TryAdapter(0, 0);

        }

        private static int TryAdapter(int currentJolts, int start)
        {
            int num = 0;
            for (int i = start; i < adapters.Count; i++)
            {
                if (adapters[i].Jolts - currentJolts > 3)
                    return num;
                if (i == adapters.Count - 1)
                    return 1;
                num += TryAdapter(adapters[i].Jolts, i + 1);
            }
            return -1;
        }
    }
}

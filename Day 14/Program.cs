using System;
using System.Collections.Generic;

namespace Day_14
{
    class Key
    {
        public char a;
        public char b;
        public char c;
    }
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Key> keys = new List<Key>();
            List<Int64> counts = new List<Int64>();
            for (int i = 2; i < lines.Length; i++)
            {
                Key key = new Key();
                key.a = lines[i][0];
                key.b = lines[i][1];
                key.c = lines[i][6];
                counts.Add(0);
                keys.Add(key);
            }
            string p = lines[0];
            for (int x = 0; x < p.Length - 1; x++)
            {
                foreach (Key key in keys)
                {
                    if (key.a == p[x] && key.b == p[x + 1])
                    {
                        // key.a + key.c
                        // key.c + key.b
                        for (int k = 0; k < keys.Count; k++)
                        {
                            if (keys[k].a == key.a && keys[k].b == key.c)
                                counts[k]++;
                            if (keys[k].a == key.c && keys[k].b == key.b)
                                counts[k]++;
                        }
                        break;
                    }
                }
            }
            for (int i = 1; i < 40; i++)
            {
                Console.WriteLine(i);
                List<Int64> newCounts = new List<Int64>();
                for (int l = 0; l < keys.Count; l++)
                    newCounts.Add(0);
                for (int l = 0; l < keys.Count; l++)
                {
                    // key.a + key.c
                    // key.c + key.b
                    for (int k = 0; k < keys.Count; k++)
                    {
                        if (keys[k].a == keys[l].a && keys[k].b == keys[l].c)
                        {
                            newCounts[k] += counts[l];
                        }
                        if (keys[k].a == keys[l].c && keys[k].b == keys[l].b)
                        {
                            newCounts[k] += counts[l];
                        }
                    }
                }
                counts = newCounts;
            }
            Dictionary<char, Int64> map = new Dictionary<char, Int64>();
            for (int k = 0; k < keys.Count; k++)
            {
                if (map.ContainsKey(keys[k].a))
                {
                    map[keys[k].a] += counts[k];
                }
                else
                {
                    map.Add(keys[k].a, counts[k]);
                }
            }
            map[p[p.Length - 1]]++;
            Int64 max = 0;
            Int64 min = Int64.MaxValue;
            foreach (var pair in map)
            {
                max = Math.Max(max, pair.Value);
                min = Math.Min(min, pair.Value);
            }
            Console.WriteLine(max - min);
        }
    }
}

using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            bool[] s = new bool[859];
            for (int i = 0;i < 859; i++)
            {
                s[i] = false;
            }
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int max = 0;
            foreach (string line in lines)
            {
                int id = GetId(line);
                max = int.Max(max, id);
                s[id] = true;
            }
            Console.WriteLine(max);
            bool started = false;
            for (int i = 0; i < 859; i++)
            {
                if (!started && s[i])
                {
                    started = true;
                }
                else if (started && !s[i])
                {
                    Console.WriteLine(i);
                    break;
                }
            }
        }

        private static int GetId(string line)
        {
            int r = GetPos(line[..7], 0, 128);
            int c = GetPos(line[7..], 0, 8);
            return r * 8 + c;
        }

        private static int GetPos(string line, int s, int l)
        {
            if (l == 1)
                return s;
            if (line[0] == 'F' || line[0] == 'L')
            {
                return GetPos(line.Substring(1), s, l / 2);
            }
            else
            {
                return GetPos(line.Substring(1), s + l / 2, l / 2);
            }
        }
    }
}

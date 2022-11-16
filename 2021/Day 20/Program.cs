using System;
using System.Collections.Generic;
using System.Numerics;

namespace Day_20
{
    class Program
    {
        static string lookup = "";
        static List<char> zeroes = new();
        static List<char> ones = new();
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            lookup = lines[0];
            List<List<char>> map = new();
            for (int i = 2; i < lines.Length; i++)
            {
                List<char> l = new();
                for (int j = 0; j < lines[i].Length; j++)
                {
                    l.Add(lines[i][j]);
                }
                map.Add(l);
            }
            for (int i = 0; i < lines[2].Length; i++)
            {
                zeroes.Add('.');
                ones.Add('#');
            }
            for (int i = 0; i < 50; i++)
            {
                Expand(map, (i % 2) == 0);
                Convolute(map);
                Frame(map, (i % 2) == 0);
                if (i == 1)
                    Console.WriteLine(CalcNumLit(map));
            }
            Console.WriteLine(CalcNumLit(map));
        }

        private static void Frame(List<List<char>> map, bool toOne)
        {
            char to = '.';
            if (toOne)
                to = '#';
            for (int x = 0; x < map.Count; x++)
            {
                map[0][x] = to;
                map[map.Count - 1][x] = to;
            }
            for (int y = 0; y < map.Count; y++)
            {
                map[y][0] = to;
                map[y][map[0].Count - 1] = to;
            }
        }

            private static int CalcNumLit(List<List<char>> map)
        {
            int count = 0;
            for (int y = 0; y < map.Count; y++)
            {
                for (int x = 0; x < map[y].Count; x++)
                {
                    if (map[y][x] == '#')
                        count++;
                }
            }

            return count;
        }

        private static void Convolute(List<List<char>> map)
        {
            List<List<char>> newMap = new();
            for (int y = 0; y < map.Count; y++)
            {
                List<char> line = new(map[y]);
                newMap.Add(line);
            }
            char[] bin = new char[9];
            for (int y = 1; y < map.Count - 1; y++)
            {
                for (int x = 1; x < map[y].Count - 1; x++)
                {
                    bin[0] = map[y - 1][x - 1];
                    bin[1] = map[y - 1][x + 0];
                    bin[2] = map[y - 1][x + 1];
                    bin[3] = map[y - 0][x - 1];
                    bin[4] = map[y - 0][x + 0];
                    bin[5] = map[y - 0][x + 1];
                    bin[6] = map[y + 1][x - 1];
                    bin[7] = map[y + 1][x + 0];
                    bin[8] = map[y + 1][x + 1];
                    newMap[y][x] = Translate(bin);
                }
            }
            for (int y = 0; y < map.Count; y++)
            {
                for (int x = 0; x < map[y].Count; x++)
                {
                    map[y][x] = newMap[y][x];
                    //Console.Write(map[y][x]);
                }
                //Console.WriteLine();
            }
        }

        private static char Translate(char[] bin)
        {
            int val = 0x100;
            int num = 0;
            for (int x = 0; x < 9; x++)
            {
                if (bin[x] == '#')
                    num += val;
                val >>= 1;
            }
            return lookup[num];
        }

        private static void Expand(List<List<char>> map, bool toZero)
        {
            if (toZero)
            {
                map.Add(new List<char>(zeroes));
                map.Add(new List<char>(zeroes));
                map.Insert(0, new List<char>(zeroes));
                map.Insert(0, new List<char>(zeroes));
                foreach (List<char> l in map)
                {
                    l.Add('.');
                    l.Add('.');
                    l.Insert(0, '.');
                    l.Insert(0, '.');
                }
            }
            else
            {
                map.Add(new List<char>(ones));
                map.Add(new List<char>(ones));
                map.Insert(0, new List<char>(ones));
                map.Insert(0, new List<char>(ones));
                foreach (List<char> l in map)
                {
                    l.Add('#');
                    l.Add('#');
                    l.Insert(0, '#');
                    l.Insert(0, '#');
                }
            }
            zeroes.Add('.');
            zeroes.Add('.');
            zeroes.Add('.');
            zeroes.Add('.');
            ones.Add('#');
            ones.Add('#');
            ones.Add('#');
            ones.Add('#');
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_13
{
    class Program
    {
        static int[] map;
        static int mapX;
        static int mapY;
        static int FillBasin(int x, int y)
        {
            int fills = 0;
            if (x < 0 || y < 0 || x >= mapX || y >= mapY || map[y * mapX + x] == 9)
                return fills;
            fills++;
            map[y * mapX + x] = 9;
            fills += FillBasin(x, y - 1);
            fills += FillBasin(x, y + 1);
            fills += FillBasin(x + 1, y);
            fills += FillBasin(x - 1, y);
            return fills;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            map = new int[lines.Length * lines[0].Length];
            mapX = lines[0].Length;
            mapY = lines.Length;
            for (int y = 0; y < mapY; y++)
            {
                for (int x = 0; x < mapX; x++)
                {
                    map[y * mapX + x] = lines[y][x] - '0';
                }
            }
            int risk = 0;
            List<int> sizes = new List<int>();
            for (int y = 0; y < mapY; y++)
            {
                for (int x = 0; x < mapX; x++)
                {
                    if ((y == 0 || map[(y - 1) * mapX + x] > map[y * mapX + x]) &&
                        (x == 0 || map[y * mapX + x - 1] > map[y * mapX + x]) &&
                        (y == mapY - 1 || map[(y + 1) * mapX + x] > map[y * mapX + x]) &&
                        (x == mapX - 1 || map[y * mapX + x + 1] > map[y * mapX + x]))
                    {
                        risk += map[y * mapX + x] + 1;
                        sizes.Add(FillBasin(x, y));
                    }
                }
            }
            sizes.Sort();
            Console.WriteLine(risk);
            Console.WriteLine(sizes[sizes.Count - 1]*sizes[sizes.Count - 2] *sizes[sizes.Count - 3]);
        }
    }
}

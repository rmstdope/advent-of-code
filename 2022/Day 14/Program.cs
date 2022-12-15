using System;

namespace AdventOfCode
{

    class Program
    {
        static public int width;
        static public int height;
        static public char[] map;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int minX = 500;
            int maxX = 500;
            int maxY = 0;
            foreach (string line in lines)
            {
                string[] c = line.Split(" -> ");
                foreach (string s in c)
                {
                    string[] values = s.Split(",");
                    minX = Math.Min(minX, int.Parse(values[0]));
                    maxX = Math.Max(maxX, int.Parse(values[0]));
                    maxY = Math.Max(maxY, int.Parse(values[1]));
                }
            }
            minX -= 1;
            maxX += 1;
            width = (maxX - minX + 1);
            height = (maxY + 1);
            map = new char[width * height];
            for (int i = 0; i < map.Length; i++)
            {
                map[i] = '.';
            }
            foreach (string line in lines)
            {
                string[] c = line.Split(" -> ");
                for (int i = 0; i < c.Length - 1; i++)
                {
                    string[] values1 = c[i].Split(",");
                    string[] values2 = c[i + 1].Split(",");
                    if (values1[0] != values2[0])
                    {
                        int x1 = int.Parse(values2[0]) - minX;
                        int x2 = int.Parse(values1[0]) - minX;
                        if (x1 > x2)
                        {
                            int t = x1;
                            x1 = x2;
                            x2 = t;
                        }
                        int y = int.Parse(values1[1]);
                        for (int j = x1; j <= x2; j++)
                        {
                            map[y * width + j] = '#';
                        }
                    }
                    else
                    {
                        int x = int.Parse(values1[0]) - minX;
                        int y1 = int.Parse(values1[1]);
                        int y2 = int.Parse(values2[1]);
                        if (y1 > y2)
                        {
                            int t = y1;
                            y1 = y2;
                            y2 = t;
                        }
                        for (int j = y1; j <= y2; j++)
                        {
                            map[j * width + x] = '#';
                        }
                    }
                }
            }

            int numsands = Simulate(minX);
            Console.WriteLine(numsands);

            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    if (map[y * width + x] == 'o')
                        map[y * width + x] = '.';
                }
            }
            int newHeight = height + 2;
            int newWidth = width + height * 2;
            char[] newMap = new char[newHeight * newWidth];
            for (int y = 0; y < newHeight; y++)
            {
                for (int x = 0; x < newWidth; x++)
                {
                    if (y == newHeight - 1)
                        newMap[y * newWidth + x] = '#';
                    else
                        newMap[y * newWidth + x] = '.';
                }
            }
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    newMap[y * newWidth + x + height] = map[y * width + x];
                }
            }
            minX -= height;
            width = newWidth;
            height = newHeight;
            map = newMap;

            numsands = Simulate(minX);
            //DrawMap();
            Console.WriteLine(numsands);
        }

        private static int Simulate(int minX)
        {
            bool endless = true;
            int numsands = 0;
            while (endless)
            {
                int sandX = 500 - minX;
                int sandY = 0;
                bool rest = false;
                while (!rest)
                {
                    if (sandX == 0 || sandX == width - 1 || sandY == height - 1)
                    {
                        endless = false;
                        rest = true;
                    }
                    else
                    {
                        if (map[(sandY + 1) * width + sandX] == '.')
                        {
                            sandY += 1;
                        }
                        else if (map[(sandY + 1) * width + sandX - 1] == '.')
                        {
                            sandY += 1;
                            sandX -= 1;
                        }
                        else if (map[(sandY + 1) * width + sandX + 1] == '.')
                        {
                            sandY += 1;
                            sandX += 1;
                        }
                        else
                        {
                            map[sandY * width + sandX] = 'o';
                            rest = true;
                            numsands++;
                            if (sandY == 0)
                                endless = false;
                        }
                    }
                }
            }

            return numsands;
        }

        private static void DrawMap()
        {
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    Console.Write(map[y * width + x]);
                }
                Console.WriteLine();
            }
        }
    }
}

using System;

namespace Day_11
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int[] oct = new int[10 * 10];
            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++)
                {
                    oct[y * 10 + x] = lines[y][x] - '0';
                }
            }
            int flashes = 0;
            int i = 0;
            int num = 0;
            do
            {
                for (int y = 0; y < lines.Length; y++)
                {
                    for (int x = 0; x < lines[y].Length; x++)
                    {
                        oct[y * 10 + x]++;
                    }
                }
                bool keep = true;
                while (keep)
                {
                    keep = false;
                    for (int y = 0; y < lines.Length; y++)
                    {
                        for (int x = 0; x < lines[y].Length; x++)
                        {
                            if (oct[y * 10 + x] > 9)
                            {
                                flashes++;
                                oct[y * 10 + x] = -1000000;
                                keep = true;
                                if (x > 0)
                                    oct[y * 10 + x - 1]++;
                                if (y > 0)
                                    oct[(y - 1) * 10 + x]++;
                                if (x < lines[y].Length - 1)
                                    oct[y * 10 + x + 1]++;
                                if (y < lines.Length - 1)
                                    oct[(y + 1) * 10 + x]++;
                                if (y > 0 && x > 0)
                                    oct[(y - 1) * 10 + x - 1]++;
                                if (y > 0 && x < lines[y].Length - 1)
                                    oct[(y - 1) * 10 + x + 1]++;
                                if (y < lines.Length - 1 && x > 0)
                                    oct[(y + 1) * 10 + x - 1]++;
                                if (y < lines.Length - 1 && x < lines[y].Length - 1)
                                    oct[(y + 1) * 10 + x + 1]++;
                            }
                        }
                    }
                }
                num = 0;
                for (int y = 0; y < lines.Length; y++)
                {
                    for (int x = 0; x < lines[y].Length; x++)
                    {
                        if (oct[y * 10 + x] < 0)
                        {
                            oct[y * 10 + x] = 0;
                            num++;
                        }
                    }
                }
                //Console.WriteLine(flashes);
                i++;
                if (i == 100)
                    Console.WriteLine(flashes);
            } while (num != 100);
            Console.WriteLine(i);
        }
    }
}

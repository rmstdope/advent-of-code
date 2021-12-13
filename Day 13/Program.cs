using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_13
{
    class Program
    {
        class Coord
        {
            public int x;
            public int y;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Coord> coords = new List<Coord>();
            foreach (string line in lines)
            {
                string[] c = line.Split(',');
                if (c.Length > 1)
                {
                    Coord coord = new Coord();
                    coord.x = Int32.Parse(c[0]);
                    coord.y = Int32.Parse(c[1]);
                    coords.Add(coord);
                }
                else if (line.Length > 0 && line[0] == 'f')
                {
                    int fold = Int32.Parse(line.Substring(13));
                    if (line[11] == 'x')
                    {
                        foreach (Coord coord in coords)
                        {
                            if (coord.x > fold)
                            {
                                coord.x = 2 * fold - coord.x;
                            }
                        }
                    }
                    else
                    {
                        foreach (Coord coord in coords)
                        {
                            if (coord.y > fold)
                            {
                                coord.y = 2 * fold - coord.y;
                            }
                        }
                    }
                }
            }
            List<Coord> unique = new List<Coord>(); ;
            int maxX = 0;
            int maxY = 0;
            foreach (Coord c1 in coords)
            {
                if (c1.x + 1 > maxX)
                    maxX = c1.x + 1;
                if (c1.y  + 1> maxY)
                    maxY = c1.y + 1;
                bool found = false;
                foreach (Coord c2 in unique)
                {
                    if (c1.x == c2.x && c1.y == c2.y)
                        found = true;
                }
                if (!found)
                    unique.Add(c1);
            }
            char[] a = new char[maxX * maxY];
            for (int i = 0; i < maxX * maxY; i++)
                a[i] = '.' ;
            foreach (Coord c1 in coords)
            {
                a[maxX * c1.y + c1.x] = '*';
            }
            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    Console.Write(a[maxX * y + x]);
                }
                Console.WriteLine();
            }
            // BFKRCJZU
        }
    }
}

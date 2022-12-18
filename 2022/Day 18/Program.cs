using System;
using System.Collections.Generic;
using System.Formats.Asn1;

namespace AdventOfCode
{
    class Vec
    {
        public Vec(int x, int y, int z)
        {
            X = x;
            Y = y;
            Z = z;
        }

        public int X { get; set; }
        public int Y { get; set; }
        public int Z { get; set; }
    }
    class Program
    {
        private static List<Vec> points;
        private static Vec max;
        private static Vec min;
        static void Main()
        {
            points = new List<Vec>();
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            max = new Vec(2, 2, 2);
            min = new Vec(2, 2, 2);
            foreach (string line in lines)
            {
                string[] l = line.Split(',');
                Vec v = new Vec(int.Parse(l[0]), int.Parse(l[1]), int.Parse(l[2]));
                points.Add(v);
                if (v.X > max.X)
                    max.X = v.X;
                if (v.X < min.X)
                    min.X = v.X;
                if (v.Y > max.Y)
                    max.Y = v.Y;
                if (v.Y < min.Y)
                    min.Y = v.Y;
                if (v.Z > max.Z)
                    max.Z = v.Z;
                if (v.Z < min.Z)
                    min.Z = v.Z;
            }

            int area = 0;
            foreach (Vec v in points)
            {
                if (!IsCube(v.X + 1, v.Y, v.Z))
                    area++;
                if (!IsCube(v.X - 1, v.Y, v.Z))
                    area++;
                if (!IsCube(v.X, v.Y + 1, v.Z))
                    area++;
                if (!IsCube(v.X, v.Y - 1, v.Z))
                    area++;
                if (!IsCube(v.X, v.Y, v.Z + 1))
                    area++;
                if (!IsCube(v.X, v.Y, v.Z - 1))
                    area++;
            }

            Console.WriteLine(area);

            area = 0;
            foreach (Vec v in points)
            {
                //Console.WriteLine("Processing " + v.X + "," + v.Y + "," + v.Z);
                if (FindWayOut(v.X + 1, v.Y, v.Z, new List<Vec>()))
                    area++;
                if (FindWayOut(v.X - 1, v.Y, v.Z, new List<Vec>()))
                    area++;
                if (FindWayOut(v.X, v.Y + 1, v.Z, new List<Vec>()))
                    area++;
                if (FindWayOut(v.X, v.Y - 1, v.Z, new List<Vec>()))
                    area++;
                if (FindWayOut(v.X, v.Y, v.Z + 1, new List<Vec>()))
                    area++;
                if (FindWayOut(v.X, v.Y, v.Z - 1, new List<Vec>()))
                    area++;
            }
            Console.WriteLine(area);
        }

        private static bool FindWayOut(int x, int y, int z, List<Vec> visited)
        {
            foreach (Vec v in visited)
            {
                if (v.X == x && v.Y == y && v.Z == z)
                    return false;
            }

            foreach (Vec v in points)
            {
                if (v.X == x && v.Y == y && v.Z == z)
                    return false;
            }
            if (x > max.X || x < min.X || y > max.Y || y < min.Y || z > max.Z || z < min.Z)
                return true;
            visited.Add(new Vec(x, y, z));
            return FindWayOut(x + 1, y, z, visited) ||
                FindWayOut(x - 1, y, z, visited) ||
                FindWayOut(x, y + 1, z, visited) ||
                FindWayOut(x, y - 1, z, visited) ||
                FindWayOut(x, y, z + 1, visited) ||
                FindWayOut(x, y, z - 1, visited);
        }

        private static bool IsCube(int x, int y, int z)
        {
            foreach(Vec v in points)
            {
                if (v.X == x && v.Y == y && v.Z == z)
                    return true;
            }
            return false;
        }
    }
}

using System;
using System.Security.Principal;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int c = 0;
            int c2 = 0;
            foreach (string line in lines)
            {
                string[] pair = line.Split(',');
                string[] p1 = pair[0].Split('-');
                string[] p2 = pair[1].Split('-');
                int i1 = int.Parse(p1[0]);
                int i2 = int.Parse(p1[1]);
                int i3 = int.Parse(p2[0]);
                int i4 = int.Parse(p2[1]);
                if (i1 >= i3 && i2 <= i4)
                    c++;
                else if (i3 >= i1 && i4 <= i2)
                    c++;
                if (i1 <= i4 && i2 >= i3)
                    c2++;
                else if (i3 <= i2 && i4 >= i1)
                    c2++;
            }
            Console.WriteLine(c);
            Console.WriteLine(c2);
        }
    }
}

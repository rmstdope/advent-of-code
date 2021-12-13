using System;

namespace Day_8
{
    class Program
    {
        static int GetValue(string val, string[] list)
        {
            for (int i = 0; i < 10; i++)
            {
                bool found = true;
                foreach(char c in val)
                {
                    if (!list[i].Contains(c))
                    {
                        found = false;
                    }
                }
                if (found && val.Length == list[i].Length)
                {
                    return i;
                }
            }
            return -1;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            int count = 0;
            int total = 0;
            foreach (string line in lines)
            {
                string[] found = new string[10];
                for (int i = 0; i < 10; i++)
                {
                    found[i] = "";
                }
                string[] s = line.Split('|');
                string[] v = s[0].Split(' ');

                foreach (string o in v)
                {
                    if (o.Length == 2)
                    {
                        found[1] = o;
                    }
                    if (o.Length == 3)
                    {
                        found[7] = o;

                    }
                    if (o.Length == 4)
                    {
                        found[4] = o;
                    }
                    if (o.Length == 7)
                    {
                        found[8] = o;
                    }
                    if (o.Length == 3 || o.Length == 4 || o.Length == 7 || o.Length == 2)
                    {
                        count++;
                    }
                }
                // 0 - 6 
                // 6 - 6
                // 9 - 6
                foreach (string o in v)
                {
                    if (o.Length == 6)
                    {
                        // Check 9
                        bool f = true;
                        for (int i = 0; i < 4; i++)
                        {
                            if (!o.Contains(found[4][i]))
                            {
                                f = false;
                            }
                        }
                        if (f)
                        {
                            found[9] = o;
                        }
                    }
                }
                foreach (string o in v)
                {
                    if (o.Length == 6 && o != found[9])
                    {
                        // Check 0 and 6
                        bool f = true;
                        for (int i = 0; i < 2; i++)
                        {
                            if (!o.Contains(found[1][i]))
                            {
                                f = false;
                            }
                        }
                        if (f)
                        {
                            found[0] = o;
                        }
                        else
                        {
                            found[6] = o;
                        }
                    }
                }
                // 2 - 5
                // 3 - 5
                // 5 - 5
                foreach (string o in v)
                {
                    if (o.Length == 5)
                    {
                        // Check 3
                        bool f = true;
                        for (int i = 0; i < 2; i++)
                        {
                            if (!o.Contains(found[1][i]))
                            {
                                f = false;
                            }
                        }
                        if (f)
                        {
                            found[3] = o;
                        }
                    }
                }
                foreach (string o in v)
                {
                    if (o.Length == 5 && found[3] != o)
                    {
                        // Check 5
                        bool f = true;
                        for (int i = 0; i < 5; i++)
                        {
                            if (!found[6].Contains(o[i]))
                            {
                                f = false;
                            }
                        }
                        if (f)
                        {
                            found[5] = o;
                        }
                        else
                        {
                            found[2] = o;
                        }
                    }
                }
                string[] v2 = s[1].Split(' ');
                int num = GetValue(v2[1], found) * 1000 + GetValue(v2[2], found) * 100 + GetValue(v2[3], found) * 10 + GetValue(v2[4], found);
                Console.WriteLine(num);
                total += num;
            }
            Console.WriteLine(count);
            Console.WriteLine(total);
        }
    }
}

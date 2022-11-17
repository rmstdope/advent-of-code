using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<string> newLines = new();
            string working = "";
            foreach (string line in lines) 
            {
                if (line.Length == 0)
                {
                    working = working.Substring(0, working.Length - 1);
                    newLines.Add(working);
                    working = "";
                }
                else
                {
                    working += line + " ";
                }
            }
            working = working.Substring(0, working.Length - 1);
            newLines.Add(working);
            int num = 0;
            int num2 = 0;
            foreach (string line in newLines)
            {
                String[] fields = line.Split(' ');
                string field;
                bool f = true;
                bool f2 = true;
                field = FindField(fields, "byr");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckByr(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "iyr");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckIyr(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "eyr");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckEyr(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "hgt");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckHgt(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "hcl");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckHcl(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "ecl");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckEcl(field.Substring(4));
                }
                else
                {
                    f = false;
                }
                field = FindField(fields, "pid");
                if (field.Length != 0)
                {
                    f2 = f2 && CheckPid(field.Substring(4));
                }
                else
                {
                    f = false;
                }

                if (f)
                {
                    num++;
                    if (f2)
                        num2++;
                }
            }
            Console.WriteLine(num);
            Console.WriteLine(num2);
        }

        private static bool CheckByr(string field)
        {
            int v = Int32.Parse(field);
            return field.Length == 4 && v <= 2002 && v >= 1920;
        }

        private static bool CheckIyr(string field)
        {
            int v = Int32.Parse(field);
            return field.Length == 4 && v <= 2020 && v >= 2010;
        }

        private static bool CheckEyr(string field)
        {
            int v = Int32.Parse(field);
            return field.Length == 4 && v <= 2030 && v >= 2020;
        }

        private static bool CheckHgt(string field)
        {
            bool i = field.EndsWith("in");
            bool c = field.EndsWith("cm");
            int v = Int32.Parse(field.Substring(0, field.Length - 2));
            if (i && v >= 59 && v <= 76)
                return true;
            if (c && v >= 150 && v <= 193)
                return true;
            return false;
        }
        private static bool CheckHcl(string field)
        {
            if (field[0] != '#')
                return false;
            for (int i = 0; i < 6; i++)
            {
                if ((field[i + 1] < '0' || field[i + 1] > '9') &&
                    (field[i + 1] < 'a' || field[i + 1] > 'f'))
                    return false;
            }
            return true;
        }
        private static bool CheckEcl(string field)
        {
            if (field == "amb")
                return true;
            if (field == "blu")
                return true;
            if (field == "brn")
                return true;
            if (field == "gry")
                return true;
            if (field == "grn")
                return true;
            if (field == "hzl")
                return true;
            if (field == "oth")
                return true;
            return false;
        }
        private static bool CheckPid(string field)
        {
            if (field.Length != 9)
                return false;
            for (int i = 0; i < 9; i++)
            {
                if (field[i] < '0' || field[i] > '9')
                    return false;
            }
            return true;
        }

        private static string FindField(string[] fields, string find)
        {
            foreach (string field in fields)
            {
                if (field.Substring(0, 3) == find)
                    return field;
            }
            return "";
        }
    }
}

using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            Int64 sum = 0;
            foreach (string line in lines)
            {
                Int64 partSum = 0;
                Int64 p = 1;
                for (int i = 0; i < line.Length; i++)
                {
                    char c = line[line.Length - 1 - i];
                    switch (c   )
                    {
                        case '=':
                            partSum += p * -2;
                            break;
                        case '-':
                            partSum += p * -1;
                            break;
                        case '0':
                            partSum += p * 0;
                            break;
                        case '1':
                            partSum += p * 1;
                            break;
                        case '2':
                            partSum += p * 2;
                            break;
                    }
                    p *= 5;
                }
                Console.WriteLine(line + " " + partSum);
                sum += partSum;
            }
            string s = ToSnafu(sum);
            Console.WriteLine(s);
        }

        private static string ToSnafu(long sum)
        {
            if (sum == 0)
                return "";
            Int64 mod = sum % 5;
            switch (mod)
            {
                case 0:
                case 1:
                case 2:
                    return ToSnafu(sum / 5) + mod.ToString();
                case 3:
                    return ToSnafu((sum + 2) / 5) + "=";
                case 4:
                    return ToSnafu((sum + 1) / 5) + "-";
            }
            return "";
        }
    }
}

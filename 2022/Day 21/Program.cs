using System;
using System.Collections.Generic;
using System.Security.Cryptography;

namespace AdventOfCode
{
    class Program
    {
        static private List<KeyValuePair<string, string>> monkeys;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            monkeys = new();
            KeyValuePair<string, string> start = new KeyValuePair<string, string>("", "");
            KeyValuePair<string, string> human = new KeyValuePair<string, string>("", "");
            for (int i = 0; i < lines.Length; i++)
            {
                string[] data = lines[i].Split(": ");
                KeyValuePair<string,string> monkey = new KeyValuePair<string, string>(data[0], data[1]);
                monkeys.Add(monkey);
                if (monkey.Key == "root")
                    start = monkey;
                if (monkey.Key == "humn")
                    human = monkey;
            }

            Console.WriteLine(Calculate(start, false, 0));

            string[] d;

            bool reduced = true;
            while (reduced)
            {
                reduced = false;
                for (int i = 0; i < monkeys.Count; i++)
                {
                    if (monkeys[i].Value.Contains("+"))
                    {
                        d = monkeys[i].Value.Split(" + ");
                        KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == d[0]);
                        KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == d[1]);
                        if (!m1.Value.Contains(' ') && !m2.Value.Contains(' ') && m1.Key != "humn" && m2.Key != "humn")
                        {
                            monkeys[i] = new KeyValuePair<string, string>(monkeys[i].Key, (Calculate(m1, false, 0) + Calculate(m2, false, 0)).ToString());
                            reduced = true;
                        }
                    }
                    if (monkeys[i].Value.Contains("-"))
                    {
                        d = monkeys[i].Value.Split(" - ");
                        KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == d[0]);
                        KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == d[1]);
                        if (!m1.Value.Contains(' ') && !m2.Value.Contains(' ') && m1.Key != "humn" && m2.Key != "humn")
                        {
                            monkeys[i] = new KeyValuePair<string, string>(monkeys[i].Key, (Calculate(m1, false, 0) - Calculate(m2, false, 0)).ToString());
                            reduced = true;
                        }
                    }
                    if (monkeys[i].Value.Contains("*"))
                    {
                        d = monkeys[i].Value.Split(" * ");
                        KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == d[0]);
                        KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == d[1]);
                        if (!m1.Value.Contains(' ') && !m2.Value.Contains(' ') && m1.Key != "humn" && m2.Key != "humn")
                        {
                            monkeys[i] = new KeyValuePair<string, string>(monkeys[i].Key, (Calculate(m1, false, 0) * Calculate(m2, false, 0)).ToString());
                            reduced = true;
                        }
                    }
                    if (monkeys[i].Value.Contains("/"))
                    {
                        d = monkeys[i].Value.Split(" / ");
                        KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == d[0]);
                        KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == d[1]);
                        if (!m1.Value.Contains(' ') && !m2.Value.Contains(' ') && m1.Key != "humn" && m2.Key != "humn")
                        {
                            monkeys[i] = new KeyValuePair<string, string>(monkeys[i].Key, (Calculate(m1, false, 0) / Calculate(m2, false, 0)).ToString());
                            reduced = true;
                        }
                    }
                }
            }
            //foreach (KeyValuePair<string,string> monkey in monkeys)
            //{
            //    Console.WriteLine(monkey.Key + ": " + monkey.Value);
            //}

            d = start.Value.Split(" + ");
            KeyValuePair<string, string> left = monkeys.Find(x => x.Key == d[0]);
            KeyValuePair<string, string> right = monkeys.Find(x => x.Key == d[1]);

            Int64 low = 0;
            Int64 high = 10000000000000;
            while (low < high)
            {
                Int64 mid = (low + high) >> 1;
                if (Calculate(left, true, mid) > Calculate(right, true, mid))
                    low = mid + 1;
                else
                    high = mid;
            }
            Console.WriteLine(low + 1);
            //Console.WriteLine(Calculate(right, true, low + 1) + " != " + Calculate(left, true, low + 1));

            // Multiple inputs gives the same output. Use the lowest one.
            Int64 s = 3342154812537;
            if (Calculate(right, true, s) == Calculate(left, true, s))
                Console.WriteLine(s);
        }

        private static string Calculate2(KeyValuePair<string, string> monkey)
        {
            if (monkey.Value.Contains("+"))
            {
                string[] data = monkey.Value.Split(" + ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                string v1 = Calculate2(m1);
                string v2 = Calculate2(m2);
                if (!v1.Contains(' ') && !v2.Contains(' '))
                {
                    return (Int64.Parse(Calculate2(m1)) + Int64.Parse(Calculate2(m2))).ToString();
                }
                return "(" + Calculate2(m1) + " + " + Calculate2(m2) + ")";
            }
            if (monkey.Value.Contains("-"))
            {
                string[] data = monkey.Value.Split(" - ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                string v1 = Calculate2(m1);
                string v2 = Calculate2(m2);
                if (!v1.Contains(' ') && !v2.Contains(' '))
                {
                    return (Int64.Parse(Calculate2(m1)) - Int64.Parse(Calculate2(m2))).ToString();
                }
                return "(" + Calculate2(m1) + " - " + Calculate2(m2) + ")";
            }
            if (monkey.Value.Contains("*"))
            {
                string[] data = monkey.Value.Split(" * ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                string v1 = Calculate2(m1);
                string v2 = Calculate2(m2);
                if (!v1.Contains(' ') && !v2.Contains(' '))
                {
                    return (Int64.Parse(Calculate2(m1)) * Int64.Parse(Calculate2(m2))).ToString();
                }
                return "(" + Calculate2(m1) + " * " + Calculate2(m2) + ")";
            }
            if (monkey.Value.Contains("/"))
            {
                string[] data = monkey.Value.Split(" / ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                string v1 = Calculate2(m1);
                string v2 = Calculate2(m2);
                if (!v1.Contains(' ') && !v2.Contains(' '))
                {
                    return (Int64.Parse(Calculate2(m1)) / Int64.Parse(Calculate2(m2))).ToString();
                }
                return "(" + Calculate2(m1) + " / " + Calculate2(m2) + ")";
            }
            if (monkey.Key == "humn")
                return " x ";
            return monkey.Value;
        }

        private static Int64 Calculate(KeyValuePair<string, string> monkey, bool shouldGuess, Int64 guess)
        {
            if (monkey.Value.Contains("+"))
            {
                string[] data = monkey.Value.Split(" + ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                return Calculate(m1, shouldGuess, guess) + Calculate(m2, shouldGuess, guess);
            }
            if (monkey.Value.Contains("-"))
            {
                string[] data = monkey.Value.Split(" - ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                return Calculate(m1, shouldGuess, guess) - Calculate(m2, shouldGuess, guess);
            }
            if (monkey.Value.Contains("*"))
            {
                string[] data = monkey.Value.Split(" * ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                return Calculate(m1, shouldGuess, guess) * Calculate(m2, shouldGuess, guess);
            }
            if (monkey.Value.Contains("/"))
            {
                string[] data = monkey.Value.Split(" / ");
                KeyValuePair<string, string> m1 = monkeys.Find(x => x.Key == data[0]);
                KeyValuePair<string, string> m2 = monkeys.Find(x => x.Key == data[1]);
                return Calculate(m1, shouldGuess, guess) / Calculate(m2, shouldGuess, guess);
            }
            if (shouldGuess && monkey.Key == "humn")
                return guess;
            return Int64.Parse(monkey.Value);
        }
    }
}

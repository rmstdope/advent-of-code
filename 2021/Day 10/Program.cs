using System;
using System.Collections.Generic;

namespace Day_10
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            Stack<char> q = new Stack<char>();
            List<Int64> scores = new List<Int64>();
            int sum = 0;
            foreach (string line in lines)
            {
                bool ok = true;
                q = new Stack<char>();
                for (int i = 0; i < line.Length; i++)
                {
                    switch (line[i])
                    {
                        case '(':
                        case '[':
                        case '{':
                        case '<':
                            q.Push(line[i]);
                            break;
                        case ')':
                            if (q.Pop() != '(')
                            {
                                sum += 3;
                                i = line.Length;
                                ok = false;
                                //Console.WriteLine(line);
                            }
                            break;
                        case ']':
                            if (q.Pop() != '[')
                            {
                                sum += 57;
                                i = line.Length;
                                ok = false;
                                //Console.WriteLine(line);
                            }
                            break;
                        case '}':
                            if (q.Pop() != '{')
                            {
                                sum += 1197;
                                i = line.Length;
                                ok = false;
                                //Console.WriteLine(line);
                            }
                            break;
                        case '>':
                            if (q.Pop() != '<')
                            {
                                sum += 25137;
                                i = line.Length;
                                ok = false;
                                //Console.WriteLine(line);
                            }
                            break;
                        default:
                            throw new Exception("Wrong char");
                    }
                }
                if (ok)
                {
                    Int64 score = 0;
                    while (q.Count != 0)
                    {
                        switch (q.Pop())
                        {
                            case '(':
                                score *= 5;
                                score += 1;
                                break;
                            case '[':
                                score *= 5;
                                score += 2;
                                break;
                            case '{':
                                score *= 5;
                                score += 3;
                                break;
                            case '<':
                                score *= 5;
                                score += 4;
                                break;
                        }
                    }
                    scores.Add(score);
                }
                //Console.WriteLine("Sum is " + sum);
            }
            scores.Sort();
            Console.WriteLine("Mid score is " + scores[scores.Count / 2]);
            Console.WriteLine("Sum is " + sum);
        }
    }
}

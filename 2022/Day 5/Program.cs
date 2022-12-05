using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            int numLines = 8;
            int numStacks = 9;
            //int numLines = 3;
            //int numStacks = 3;
            Stack<char>[] stacks = new Stack<char>[numStacks];
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");

            for (int i = 0; i < numStacks; i++)
            {
                stacks[i] = new Stack<char>();
            }

            for (int i = numLines - 1;i >= 0; i--)
            {
                for (int j = 0; j < numStacks; j++)
                {
                    if (lines[i][j * 4 + 1] != ' ')
                    {
                        stacks[j].Push(lines[i][j * 4 + 1]);
                    }
                }
            }
            for (int i = 10; i < lines.Length; i++)
            {
                string[] sub = lines[i].Split(' ');
                int from = int.Parse(sub[3]);
                int to = int.Parse(sub[5]);
                int num = int.Parse(sub[1]);

                for (int j = 0; j < num; j++)
                {
                    stacks[to - 1].Push(stacks[from - 1].Pop());
                }
            }
            string s = "";
            for (int i = 0; i < 9; i++)
            {
                s += stacks[i].Pop();
            }
            Console.WriteLine(s);

            for (int i = 0; i < numStacks; i++)
            {
                stacks[i] = new Stack<char>();
            }

            for (int i = numLines - 1; i >= 0; i--)
            {
                for (int j = 0; j < numStacks; j++)
                {
                    if (lines[i][j * 4 + 1] != ' ')
                    {
                        stacks[j].Push(lines[i][j * 4 + 1]);
                    }
                }
            }
            for (int i = 10; i < lines.Length; i++)
            {
                string[] sub = lines[i].Split(' ');
                int from = int.Parse(sub[3]);
                int to = int.Parse(sub[5]);
                int num = int.Parse(sub[1]);

                Stack<char> chars= new Stack<char>();
                for (int j = 0; j < num; j++)
                {
                    chars.Push(stacks[from - 1].Pop());
                }
                for (int j = 0; j < num; j++)
                {
                    stacks[to - 1].Push(chars.Pop());
                }
            }
            s = "";
            for (int i = 0; i < 9; i++)
            {
                s += stacks[i].Pop();
            }

            Console.WriteLine(s);
        }
    }
}

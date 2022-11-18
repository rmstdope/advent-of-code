using System;

namespace AdventOfCode
{
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            bool[] visited = new bool[lines.Length];
            for (int i = 0;i < lines.Length;i++)
            {
                visited[i] = false;
            }
            int pos = 0;
            int acc = 0;
            while (!visited[pos])
            {
                visited[pos] = true;
                string cmd = lines[pos].Substring(0, 3);
                int num = Int32.Parse(lines[pos].Substring(4));
                if (cmd == "acc")
                {
                    acc += num;
                    pos++;
                }
                else if (cmd == "nop")
                {
                    pos++;
                }
                else
                {
                    pos += num;
                }
            }

            Console.WriteLine(acc);

            for (int i = 0; i < lines.Length; i++)
            {
                string cmd = lines[i].Substring(0, 3);
                if (cmd == "nop")
                {
                    lines[i] = lines[i].Replace("nop", "jmp");
                    if (Terminates(lines, out acc))
                    {
                        Console.WriteLine("Terminates with " + acc);
                    }
                    lines[i] = lines[i].Replace("jmp", "nop");
                }
                if (cmd == "jmp")
                {
                    lines[i] = lines[i].Replace("jmp", "nop");
                    if (Terminates(lines, out acc))
                    {
                        Console.WriteLine("Terminates with " + acc);
                    }
                    lines[i] = lines[i].Replace("nop", "jmp");
                }
            }
        }

        private static bool Terminates(string[] lines, out int acc)
        {
            bool[] visited = new bool[lines.Length];
            for (int i = 0; i < lines.Length; i++)
            {
                visited[i] = false;
            }
            int pos = 0;
            acc = 0;
            while (!visited[pos])
            {
                visited[pos] = true;
                string cmd = lines[pos].Substring(0, 3);
                int num = Int32.Parse(lines[pos].Substring(4));
                if (cmd == "acc")
                {
                    acc += num;
                    pos++;
                }
                else if (cmd == "nop")
                {
                    pos++;
                }
                else
                {
                    pos += num;
                }
                if (pos >= lines.Length)
                    return true;
            }
            return false;
        }
    }
}

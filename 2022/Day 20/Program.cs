using System;
using System.Collections.Generic;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace AdventOfCode
{
    class Data
    {
        public Data(Int64 value, Int64 pos, Int64 num)
        {
            Value = value;
            OrigPos = pos;
            Pos = pos;
            Num = num;
        }

        public Int64 Value { get; private set; }
        public Int64 OrigPos { get; private set; }
        public Int64 Pos { get; set; }
        public Int64 Num { get; private set; }

        internal void MoveLeft()
        {
            Pos--;
            while (Pos < 0)
                Pos += Num;
        }

        internal void MoveRight()
        {
            Pos++;
            while (Pos >= Num)
                Pos -= Num;
        }
    }
    class Program
    {
        static Int64 KEY = 1;
        static int TIMES = 1;
        //static Int64 KEY = 811589153;
        //static int TIMES = 10;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Data> numbers = new List<Data>();
            List<Data> mixed = new List<Data>();
            for (Int64 i = 0; i < lines.Length; i++)
            {
                Data number = new Data(Int64.Parse(lines[i]) * KEY, i, lines.Length);
                numbers.Add(number);
                mixed.Add(number);
            }
            //Console.WriteLine("Initial");
            //foreach (Data n in mixed)
            //{
            //    Console.Write(n.Value + ",");
            //}
            //Console.WriteLine("");
            for (int q = 0; q < TIMES; q++)
            {
                for (int i = 0; i < lines.Length; i++)
                {
                    Int64 index = mixed.FindIndex(x => x == numbers[i]);
                    //Console.WriteLine("Move " + numbers[i].Value);
                    mixed.Remove(numbers[i]);
                    Int64 newpos = index + numbers[i].Value;
                    while (newpos < 0)
                    {
                        newpos = newpos % (lines.Length - 1);
                        newpos += lines.Length - 1;
                    }
                    if (newpos == 0 && numbers[i].Value < 0)
                        newpos = mixed.Count;
                    else
                        newpos = newpos % (lines.Length - 1);
                    mixed.Insert((int)newpos, numbers[i]);
                    //foreach (Data n in mixed)
                    //{
                    //    Console.Write(n.Value + ",");
                    //}
                    //Console.WriteLine("");
                }
            }

            int zero = mixed.FindIndex(x => x.Value == 0);
            int n1 = (zero + 1000) % mixed.Count;
            int n2 = (zero + 2000) % mixed.Count;
            int n3 = (zero + 3000) % mixed.Count;
            Console.WriteLine(mixed[n1].Value);
            Console.WriteLine(mixed[n2].Value);
            Console.WriteLine(mixed[n3].Value);
            Console.WriteLine(mixed[n1].Value + mixed[n2].Value + mixed[n3].Value);
        }

        private static void DebugPrint(string[] lines, List<Data> numbers)
        {
            for (Int64 j = 0; j < lines.Length; j++)
            {
                foreach (Data number in numbers)
                {
                    if (number.Pos == j)
                    {
                        Console.Write(number.Value + ",");
                        break;
                    }
                }
            }
            Console.WriteLine("");
        }
    }
}

using System;
using System.Buffers;
using System.Collections.Generic;
using System.Data.SqlTypes;

namespace AdventOfCode
{
    public class Item
    {
        public int Worry { get; set; }
        public Item(int worry) 
        {
            Worry = worry;
        }
    }
    public class Monkey
    {
        private List<Int64> items;
        private string operation;
        private int divisible;
        private int ifTrue;
        private int ifFalse;
        private bool divide;
        public int Inspected { get; set; }

        public Monkey(bool divide)
        {
            this.divide = divide;
            items = new List<Int64>();
            Inspected = 0;
        }

        internal void AddItem(Int64 worry)
        {
            items.Add(worry);
        }

        internal void SetOperation(string v)
        {
            operation = v;
        }

        internal void SetTest(int div, int ifTrue, int ifFalse)
        {
            divisible = div;
            this.ifTrue = ifTrue;
            this.ifFalse= ifFalse;
        }

        internal void Run(Monkey[] monkeys)
        {
            for (int i = 0; i < items.Count; i++)
            {
                Inspected++;
                if (operation[10] == '+')
                {
                    items[i] += int.Parse(operation.Substring(12));
                }
                else
                {
                    if (operation[12] == 'o')
                        items[i] *= items[i];
                    else
                        items[i] *= int.Parse(operation.Substring(12));

                }
                if (monkeys.Length == 4)
                    items[i] %= (23 * 19 * 13 * 17);
                else
                    items[i] %= (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17);
                //items[i] = (int)Math.Round(items[i] / 3.0);
                if (divide)
                    items[i] = items[i] / 3;
                if (items[i] % divisible == 0)
                {
                    monkeys[ifTrue].AddItem(items[i]);
                }
                else
                {
                    monkeys[ifFalse].AddItem(items[i]);
                }
            }
            items.Clear();
        }
    }
    class Program
    {
        static void Main()
        {
            int numMonkeys = 8;
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");

            Monkey[] monkeys = Prepare(numMonkeys, lines, true);

            for (int i = 0; i < 20; i++)
            {
                foreach (Monkey m in monkeys)
                {
                    m.Run(monkeys);
                }
            }
            List<Int64> inspected = new List<Int64>();
            foreach (Monkey m in monkeys)
            {
                inspected.Add(m.Inspected);
            }
            inspected.Sort();

            Console.WriteLine(inspected[inspected.Count - 1] * inspected[inspected.Count - 2]);

            monkeys = Prepare(numMonkeys, lines, false);

            for (int i = 0; i < 10000; i++)
            {
                foreach (Monkey m in monkeys)
                {
                    m.Run(monkeys);
                }
            }

            inspected = new List<Int64>();
            foreach (Monkey m in monkeys)
            {
                inspected.Add(m.Inspected);
            }
            inspected.Sort();

            Console.WriteLine(inspected[inspected.Count - 1] * inspected[inspected.Count - 2]);
        }

        private static Monkey[] Prepare(int numMonkeys, string[] lines, bool divide)
        {
            Monkey[] monkeys = new Monkey[numMonkeys];
            int l = 0;
            for (int i = 0; i < numMonkeys; i++)
            {
                l++;
                monkeys[i] = new Monkey(divide);
                string[] items = lines[l++].Substring(18).Split(", ");
                for (int j = 0; j < items.Length; j++)
                {
                    monkeys[i].AddItem(int.Parse(items[j]));
                }
                monkeys[i].SetOperation(lines[l++].Substring(13));
                monkeys[i].SetTest(int.Parse(lines[l++].Substring(21)),
                    int.Parse(lines[l++].Substring(29)),
                    int.Parse(lines[l++].Substring(30)));
                l++;
            }

            return monkeys;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace AdventOfCode
{
    class Bag
    {
        public string Color { get; set; }
        public Bag(string colorType, string color)
        {
            Color = color + colorType;
        }
    }
    class Rule
    {
        public Bag Bag { get; set; }
        public List<BagData> Contains { get; set; }
        public Rule(Bag bag)
        {
            Bag = bag;
            Contains = new();
        }
        public void AddContain(BagData bagData)
        {
            Contains.Add(bagData);
        }
    }
    class BagData
    {
        public int Num { get; set; }
        public Bag Bag { get; set; }
        public BagData(int num, Bag bag) 
        {
            Num = num;
            Bag = bag;
        }
    }
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Rule> rules = new();
            foreach (string line in lines)
            {
                string[] data = line.Split(' ');
                Bag bag = new(data[0], data[1]);
                Rule rule = new(bag);
                int pos = 4;
                while (pos < data.Length)
                {
                    if (data[pos] == "no")
                        pos += 100;
                    else
                    {
                        rule.AddContain(new BagData(Int32.Parse(data[pos]), new Bag(data[pos + 1], data[pos + 2])));
                        pos += 4;
                    }
                }
                rules.Add(rule);
            }
            List<Bag> correct = new();
            List<Bag> trying = new();
            trying.Add(new Bag("shiny", "gold"));
            while (trying.Count != 0)
            {
                Bag bag = trying[0];
                trying.RemoveAt(0);
                foreach(Rule r in rules)
                {
                    foreach(BagData b in r.Contains)
                    {
                        if (b.Bag.Color == bag.Color)
                        {
                            trying.Add(r.Bag);
                            if (!correct.Exists(x => x.Color == r.Bag.Color)) 
                                correct.Add(r.Bag);
                        }
                    }
                }
            }
            Console.WriteLine(correct.Count);

            List<BagData> completedBags = new();
            List<BagData> uncompletedBags = new();
            uncompletedBags.Add(new BagData(1, new Bag("shiny", "gold")));
            while(uncompletedBags.Count != 0)
            {
                BagData data = uncompletedBags[0];
                uncompletedBags.RemoveAt(0);
                Rule r = rules.Find(x => x.Bag.Color == data.Bag.Color);
                completedBags.Add(data);
                if (r.Contains.Count != 0)
                {
                    foreach (BagData b in r.Contains)
                    {
                        uncompletedBags.Add(new BagData(data.Num * b.Num, b.Bag));
                    }
                }
            }
            int num = 0;
            foreach(BagData b in completedBags)
            {
                num += b.Num;
            }
            Console.WriteLine(num - 1);
        }
    }
}

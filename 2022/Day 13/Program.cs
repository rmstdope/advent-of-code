using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace AdventOfCode
{
    class Entry
    {
        public List<Entry> entries;
        public int value;
        public string data;
        public Entry(string data)
        {
            this.data = data;
            if (data[0] == '[')
            {
                entries = new();
                string n = data.Substring(0, data.Length - 1).Substring(1);
                List<string> values = new List<string>();
                int last = 0;
                int depth = 0;
                int i = 0;
                for (i = 0; i < n.Length; i++)
                {
                    if (n[i] == '[')
                        depth++;
                    if (n[i] == ']')
                        depth--;
                    if (n[i] == ',' && depth == 0)
                    {
                        values.Add(n.Substring(last, i - last));
                        last = i + 1;
                    }
                }
                if (i != last)
                    values.Add(n.Substring(last, i - last));
                foreach (string v in values)
                {
                    entries.Add(new Entry(v));
                }
            }
            else
            {
                entries = null;
                value = int.Parse(data);
            }
        }

        public enum Return
        {
            Right = -1,
            Wrong = 1,
            Continue = 0,
        }
        public int IntCompare(Entry right)
        {
            return (int)Compare(right);
        }
        public Return Compare(Entry right)
        {
            if (entries == null)
            {
                if (right.entries == null)
                {
                    if (value < right.value)
                        return Return.Right;
                    else if (value == right.value)
                        return Return.Continue;
                    return Return.Wrong;
                }
                else
                {
                    entries = new List<Entry>();
                    entries.Add(new Entry(value.ToString()));
                    return Compare(right);
                }
            }
            else
            {
                if (right.entries == null)
                {
                    right.entries = new List<Entry>();
                    right.entries.Add(new Entry(right.value.ToString()));
                    return Compare(right);
                }
                else
                {
                    for (int i = 0; i < entries.Count; i++)
                    {
                        if (right.entries.Count <= i)
                            return Return.Wrong;
                        Return v = entries[i].Compare(right.entries[i]);
                        if (v == Return.Right || v == Return.Wrong)
                            return v;
                    }
                    if (right.entries.Count > entries.Count)
                        return Return.Right;
                    return Return.Continue;
                }
            }

        }
    }
    class Program
    {
        static void Main()
        {
            int sum = 0;
            int index = 1;
            int i = 0;
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Entry> all = new();
            while (i < lines.Length)
            {
                Entry left = new Entry(lines[i++]);
                Entry right = new Entry(lines[i++]);
                all.Add(right);
                all.Add(left);
                i++;
                if (left.Compare(right) == Entry.Return.Right)
                {
                    sum += index;
                }
                index++;
            }
            Console.WriteLine(sum);

            all.Add(new Entry("[[2]]"));
            all.Add(new Entry("[[6]]"));

            all.Sort((l, r) => l.IntCompare(r));
            int mul = 1;
            for (i = 0; i < all.Count; i++)
            {
                if (all[i].data == "[[6]]" || all[i].data == "[[2]]")
                    mul *= (i + 1);

            }
            Console.WriteLine(mul);

        }
    }
}

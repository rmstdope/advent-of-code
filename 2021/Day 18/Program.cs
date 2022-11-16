using System;
using System.Collections.Generic;

namespace Day_18
{
    class Program
    {
        private class Node
        {
            public Node(char c)
            {
                C = c;
                Val = -1;
                if (Char.IsDigit(c))
                    Val = Int32.Parse(c.ToString());
            }
            public Node(int i)
            {
                C = '1';
                Val = i;
            }
            internal int Val { get; set; }
            internal char C { get; set; }
            internal bool IsStart()
            {
                return C == '[';
            }
            internal bool IsEnd()
            {
                return C == ']';
            }
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            //Pair pair;
            //string line;
            List<Node> nodes = new List<Node>();
            for (int l = 0; l < lines.Length; l++)
            {
                if (l != 0)
                {
                    nodes.Insert(0, new Node('['));
                    nodes.Add(new Node(','));
                }
                for (int i = 0; i < lines[l].Length; i++)
                {
                    Node node = new Node(lines[l][i]);
                    nodes.Add(node);
                }
                if (l != 0)
                {
                    nodes.Add(new Node(']'));
                }
                bool exploded = true;
                bool split = false;
                while (exploded || split)
                {
                    split = false;
                    exploded = false;
                    int nest = 0;
                    for (int i = 0; i < nodes.Count; i++)
                    {
                        if (nodes[i].IsStart())
                            nest++;
                        if (nodes[i].IsEnd())
                            nest--;
                        if (nest == 5)
                        {
                            // Explode
                            exploded = true;
                            int left = nodes[i + 1].Val;
                            int right = nodes[i + 3].Val;
                            List<Node> before = nodes.GetRange(0, i);
                            List<Node> after = nodes.GetRange(i + 5, nodes.Count - (i + 5));
                            for (int x = before.Count - 1; x > 0; x--)
                            {
                                if (before[x].Val >= 0)
                                {
                                    before[x].Val += left;
                                    break;
                                }
                            }
                            for (int x = 0; x < after.Count; x++)
                            {
                                if (after[x].Val >= 0)
                                {
                                    after[x].Val += right;
                                    break;
                                }
                            }
                            nodes = before;
                            nodes.Add(new Node('0'));
                            nodes.AddRange(after);
                            break;
                        }
                    }
                    if (!exploded)
                    {
                        for (int i = 0; i < nodes.Count; i++)
                        {
                            if (nodes[i].Val > 9)
                            {
                                split = true;
                                int add = 0;
                                if ((nodes[i].Val & 1) == 1)
                                    add = 1;
                                List<Node> insert = new List<Node>();
                                insert.Add(new Node('['));
                                insert.Add(new Node(nodes[i].Val / 2));
                                insert.Add(new Node(','));
                                insert.Add(new Node(nodes[i].Val / 2 + add));
                                insert.Add(new Node(']'));
                                nodes.RemoveAt(i);
                                nodes.InsertRange(i, insert);
                                break;
                            }
                        }
                    }
                    //Print(nodes);
                }
            }
            int index = 0;
            Console.WriteLine(CalcMagnitude(nodes, 0, out index));
            long max = 0;
            for (int u = 0; u < lines.Length; u++)
            {
                for (int v = 0; v < lines.Length; v++)
                {
                    if (u != v)
                    {
                        int l = -1;
                        nodes.Clear();
                        do
                        {
                            if (l == -1)
                                l = u;
                            else if (l == u)
                                l = v;
                            if (l != u)
                            {
                                nodes.Insert(0, new Node('['));
                                nodes.Add(new Node(','));
                            }
                            for (int i = 0; i < lines[l].Length; i++)
                            {
                                Node node = new Node(lines[l][i]);
                                nodes.Add(node);
                            }
                            if (l != u)
                            {
                                nodes.Add(new Node(']'));
                            }
                        } while (l != v);
                        bool exploded = true;
                        bool split = false;
                        while (exploded || split)
                        {
                            split = false;
                            exploded = false;
                            int nest = 0;
                            for (int i = 0; i < nodes.Count; i++)
                            {
                                if (nodes[i].IsStart())
                                    nest++;
                                if (nodes[i].IsEnd())
                                    nest--;
                                if (nest == 5)
                                {
                                    // Explode
                                    exploded = true;
                                    int left = nodes[i + 1].Val;
                                    int right = nodes[i + 3].Val;
                                    List<Node> before = nodes.GetRange(0, i);
                                    List<Node> after = nodes.GetRange(i + 5, nodes.Count - (i + 5));
                                    for (int x = before.Count - 1; x > 0; x--)
                                    {
                                        if (before[x].Val >= 0)
                                        {
                                            before[x].Val += left;
                                            break;
                                        }
                                    }
                                    for (int x = 0; x < after.Count; x++)
                                    {
                                        if (after[x].Val >= 0)
                                        {
                                            after[x].Val += right;
                                            break;
                                        }
                                    }
                                    nodes = before;
                                    nodes.Add(new Node('0'));
                                    nodes.AddRange(after);
                                    break;
                                }
                            }
                            if (!exploded)
                            {
                                for (int i = 0; i < nodes.Count; i++)
                                {
                                    if (nodes[i].Val > 9)
                                    {
                                        split = true;
                                        int add = 0;
                                        if ((nodes[i].Val & 1) == 1)
                                            add = 1;
                                        List<Node> insert = new List<Node>();
                                        insert.Add(new Node('['));
                                        insert.Add(new Node(nodes[i].Val / 2));
                                        insert.Add(new Node(','));
                                        insert.Add(new Node(nodes[i].Val / 2 + add));
                                        insert.Add(new Node(']'));
                                        nodes.RemoveAt(i);
                                        nodes.InsertRange(i, insert);
                                        break;
                                    }
                                }
                            }
                            //Print(nodes);
                        }
                        long mag = CalcMagnitude(nodes, 0, out index);
                        if (mag > max)
                            max = mag;
                    }
                }
            }
            Console.WriteLine(max);
        }

        private static long CalcMagnitude(List<Node> nodes, int i, out int endI)
        {
            endI = i;
            if (nodes[i].Val > -1)
            {
                endI = i + 1;
                return nodes[i].Val;
            }
            if (nodes[i].IsStart())
            {
                long a = CalcMagnitude(nodes, i + 1, out endI);
                endI++;
                long b = CalcMagnitude(nodes, endI, out endI);
                endI++;
                return a * 3 + b * 2;
            }
            return 0;
        }

        private static void Print(List<Node> nodes)
        {
            foreach (Node n in nodes)
            {
                if (n.Val == -1)
                    Console.Write(n.C);
                else
                    Console.Write(n.Val);
            }
            Console.WriteLine("");
        }

        private static int ParseNum(string s, out int index)
        {
            string digits = "";
            index = 0;
            while (Char.IsDigit(s[index]))
            {
                digits += s[index];
                index++;
            }
            return Int32.Parse(digits);
        }

        private static bool Explode(Pair pair, int depth, out int addLeft)
        {
            bool exploded = false;
            addLeft = 0;
            if(pair.pair1 != null)
            {
                if (depth == 3)
                {
                    pair.val1 = 0;
                    AddRight(pair.pair1.val2, pair);
                    pair.pair1 = null;
                }
                else
                {
                    exploded = exploded || Explode(pair.pair1, depth + 1, out addLeft);
                    if (exploded)
                    {
                        if (pair.val1 != -1)
                        {
                            pair.val1 += addLeft;
                            addLeft = 0;
                        }
                    }
                }
            }
            if (pair.pair2 != null)
            {
                if (depth == 3)
                {
                    pair.val2 = 0;
                    addLeft = pair.pair2.val1;
                    pair.pair2 = null;
                }
                else
                {
                    exploded = exploded || Explode(pair.pair2, depth + 1, out addLeft);
                    if (pair.val1 != -1)
                    {
                        pair.val1 += addLeft;
                        addLeft = 0;
                    }
                }
            }
            return exploded;
        }

        private static void AddRight(int val, Pair pair)
        {
            if (pair.val2 != -1)
                pair.val2 += val;
        }

        private class Pair
        {
            public Pair? pair1;
            public Pair? pair2;
            public int val1;
            public int val2;
            public Pair()
            {
                pair1 = null;
                pair2 = null;
                val1 = -1;
                val2 = -1;
            }
            internal string Parse(string s)
            {
                if (s[0] == '[')
                {
                    s = s.Substring(1);
                    pair1 = new Pair();
                    s = pair1.Parse(s);
                    //s = s.Substring(1);
                    //pair2 = new Pair();
                    //s = pair2.Parse(s);
                    //return s;
                }
                else
                {
                    string digits = "";
                    while (Char.IsDigit(s[0]))
                    {
                        digits += s[0];
                        s = s.Substring(1);
                    }
                    val1 = Int32.Parse(digits);
                }
                // comma
                s = s.Substring(1);

                if (s[0] == '[')
                {
                    s = s.Substring(1);
                    pair2 = new Pair();
                    s = pair2.Parse(s);
                }
                else
                {
                    string digits = "";
                    while (Char.IsDigit(s[0]))
                    {
                        digits += s[0];
                        s = s.Substring(1);
                    }
                    val2 = Int32.Parse(digits);
                }
                // ]
                s = s.Substring(1);
                return s;
            }
        }

    }
}

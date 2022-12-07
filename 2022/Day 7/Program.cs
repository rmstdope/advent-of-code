using System;
using System.Collections.Generic;
using System.Timers;

namespace AdventOfCode
{
    public class Node
    {
        public List<Node> children;
        public Node parent;
        public int size;
        public string name;
        public Node(string name)
        {
            this.name = name;
            this.parent = null;
            this.children = null;
            this.size = 0;
        }
    }
    class Program
    {
        static void Main()
        {
            string[] p = null;
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            string[] newLines = new string[lines.Length + 2];
            for (int i = 0; i < lines.Length; i++)
            {
                newLines[i] = lines[i];
            }
            newLines[lines.Length] = "$ cd ..";
            newLines[lines.Length + 1] = "$ cd ..";
            lines = newLines;
            Node root = new Node("root");
            Node node = root;
            node.children = new();
            for (int i = 1; i < lines.Length; i++)
            {
                if (lines[i] == "$ ls")
                {
                    while (i < lines.Length - 1 && lines[i + 1][0] != '$')
                    {
                        i++;
                        p = lines[i].Split(' ');
                        Node newNode = new Node(p[1]);
                        if (p[0] == "dir")
                        {
                            newNode.children = new();
                        }
                        else
                        {
                            newNode.size = int.Parse(p[0]);
                        }
                        node.children.Add(newNode);
                        newNode.parent = node;
                    }
                }
                p = lines[i].Split(' ');
                if (p[1] == "cd")
                {
                    if (p[2] == "..")
                    {
                        foreach (Node n in node.children)
                        {
                            node.size += n.size;
                        }
                        node = node.parent;
                    }
                    else
                    {
                        foreach (Node n in node.children)
                        { 
                            if (n.name == p[2])
                            {
                                node = n;
                                break;
                            }
                        }
                    }
                }
            }

            foreach (Node n in root.children)
            {
                root.size += n.size;
            }

            int sum = Walk(root);
            Console.WriteLine(sum);

            int used = 70000000 - root.size;
            int need = 30000000 - used;
            List<int> sizes = new();

            AddSizes(root, sizes);
            sizes.Sort();
            foreach(int s in sizes)
            {
                if (s > need)
                {
                    Console.WriteLine(s);
                    break;
                }
            }
        }

        private static void AddSizes(Node node, List<int> sizes)
        {
            if (node.children != null)
            {
                foreach (Node n in node.children)
                {
                    AddSizes(n, sizes);
                }
                sizes.Add(node.size);
            }
        }

        private static int Walk(Node node)
        {
            int sum = 0;
            if (node.children != null)
            {
                foreach (Node n in node.children)
                {
                    sum += Walk(n);
                }
                if (node.size < 100000)
                {
                    sum += node.size;
                }
            }
            return sum;
        }
    }
}

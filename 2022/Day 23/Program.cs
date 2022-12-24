using System;
using System.Collections.Generic;
using static AdventOfCode.Elf;

namespace AdventOfCode
{
    class Elf
    {
        static public int elfMoved;
        public int X { get; private set; }
        public int Y { get; private set; }
        public int NextMove { get; private set; }
        public int LastTry { get; private set; }
        public int NewX
        {
            get
            {
                if ((NextMove & (W + SW + NW)) != 0)
                    return X - 1;
                if ((NextMove & (E + SE + NE)) != 0)
                    return X + 1;
                return X;
            }
        }
        public int NewY
        {
            get
            {
                if ((NextMove & (N + NW + NE)) != 0)
                    return Y - 1;
                if ((NextMove & (S + SE + SW)) != 0)
                    return Y + 1;
                return Y;
            }
        }

        public bool ShouldMove { get; private set; }

        static public int N = 1;
        static public int NE = 2;
        static public int NW = 4;
        static public int E = 8;
        static public int W = 16;
        static public int S = 32;
        static public int SW = 64;
        static public int SE = 128;

        public Elf(int x, int y)
        {
            X = x;
            Y = y;
        }
        internal void ProposeMove(List<Elf> elves, List<int> consider)
        {
            int dirs = 0;
            NextMove = 0;
            foreach (Elf elf in elves)
            {
                if (elf != this)
                {
                    int dx = X - elf.X;
                    int dy = Y - elf.Y;
                    if (dx == 1 && dy == 1)
                        dirs += NW;
                    if (dx == 0 && dy == 1)
                        dirs += N;
                    if (dx == -1 && dy == 1)
                        dirs += NE;
                    if (dx == -1 && dy == 0)
                        dirs += E;
                    if (dx == 1 && dy == 0)
                        dirs += W;
                    if (dx == -1 && dy == -1)
                        dirs += SE;
                    if (dx == 0 && dy == -1)
                        dirs += S;
                    if (dx == 1 && dy == -1)
                        dirs += SW;
                }
            }
            if (dirs == 0)
            {
                NextMove = 0;
                return;
            }
            foreach (int d in consider)
            {
                if (d == N && (dirs & (N + NE + NW)) == 0)
                {
                    NextMove = N;
                    return;
                }
                if (d == S && (dirs & (S + SE + SW)) == 0)
                {
                    NextMove = S;
                    return;
                }
                if (d == W && (dirs & (W + SW + NW)) == 0)
                {
                    NextMove = W;
                    return;
                }
                if (d == E && (dirs & (E + SE + NE)) == 0)
                {
                    NextMove = E;
                    return;
                }
            }
        }

        internal void PrepareMove(List<Elf> elves)
        {
            ShouldMove = false;
            foreach(Elf elf in elves)
            {
                if (elf != this)
                {
                    if (elf.NewX == NewX && elf.NewY == NewY)
                        return;
                }
            }
            if (NewX != X || NewY != Y)
                ShouldMove = true;
        }
        internal void DoMove()
        {
            if (ShouldMove)
            {
                elfMoved++;
                X = NewX;
                Y = NewY;
            }
        }
    }
    class Program
    {
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Elf> elves = new List<Elf>();
            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++) 
                {
                    if (lines[y][x] == '#')
                    {
                        Elf elf = new Elf(x, y);
                        elves.Add(elf);
                    }
                }
            }

            List<int> consider = new List<int>();
            consider.Add(Elf.N);
            consider.Add(Elf.S);
            consider.Add(Elf.W);
            consider.Add(Elf.E);
            for (int i = 0; i < 10; i++)
            {
                foreach (Elf elf in elves)
                {
                    elf.ProposeMove(elves, consider);
                }
                foreach (Elf elf in elves)
                {
                    elf.PrepareMove(elves);
                }
                foreach (Elf elf in elves)
                {
                    elf.DoMove();
                }
                int old = consider[0];
                consider.RemoveAt(0);
                consider.Add(old);
            }
            int minX = 1000;
            int maxX = 0;
            int minY = 1000;
            int maxY = 0;
            foreach (Elf elf in elves)
            {
                maxX = Math.Max(elf.X, maxX);
                minX = Math.Min(elf.X, minX);
                maxY = Math.Max(elf.Y, maxY);
                minY = Math.Min(elf.Y, minY);
            }
            int area = (maxY - minY + 1) * (maxX - minX + 1);
            Console.WriteLine(area - elves.Count);

            int j = 11;
            while (true)
            {
                Elf.elfMoved = 0;
                foreach (Elf elf in elves)
                {
                    elf.ProposeMove(elves, consider);
                }
                foreach (Elf elf in elves)
                {
                    elf.PrepareMove(elves);
                }
                foreach (Elf elf in elves)
                {
                    elf.DoMove();
                }
                int old = consider[0];
                consider.RemoveAt(0);
                consider.Add(old);
                if (j % 100 == 0)
                    Console.WriteLine("Trying " + j + ":" + elfMoved);
                if (elfMoved == 0)
                {
                    Console.WriteLine(j);
                    break;
                }
                j++;
            }

            //for (int y = minY; y <= maxY; y++)
            //{
            //    for (int x = minX; x <= maxX; x++)
            //    {
            //        bool found = false;
            //        foreach (Elf elf in elves)
            //        {
            //            if (elf.X == x && elf.Y == y)
            //                found = true;
            //        }
            //        if (found)
            //            Console.Write('#');
            //        else
            //            Console.Write('.');
            //    }
            //    Console.WriteLine();
            //}
        }
    }
}

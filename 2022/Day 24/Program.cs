using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Transactions;

namespace AdventOfCode
{
    public class Blizzard
    {
        public Blizzard(int x, int y, char dir)
        {
            X = x;
            Y = y;
            Dir = dir;
        }

        public int X { get; private set; }
        public int Y { get; private set; }
        public char Dir { get; private set; }
    }
    public class State
    {
        public State(int x, int y)
        {
            X = x;
            Y = y;
            Time = 0;
        }

        public int X { get; }
        public int Y { get; }
        public int Time { get; }
    }
    public class Blizzard2
    {
        public Blizzard2(int coord, int delta)
        {
            Coord = coord;
            Delta = delta;
        }

        public int Coord { get; private set; }
        public int Delta { get; private set; }

    }
    class Program
    {
        static int width;
        static int height;
        static List<List<Blizzard2>> rows;
        static List<List<Blizzard2>> columns;

        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Blizzard> blizzards = new List<Blizzard>();
            rows = new List<List<Blizzard2>>();
            columns = new List<List<Blizzard2>>();
            int x;
            int y;
            for (y = 0; y < lines.Length; y++)
            {
                rows.Add(new List<Blizzard2>());
                for (x = 0; x < lines[y].Length; x++)
                {
                    if (y == 0)
                        columns.Add(new List<Blizzard2>());
                    if (lines[y][x] == '>')
                    {
                        Blizzard2 b = new(x - 1, 1);
                        rows[y - 1].Add(b);
                    }
                    if (lines[y][x] == '<')
                    {
                        Blizzard2 b = new(x - 1, -1);
                        rows[y - 1].Add(b);
                    }
                    if (lines[y][x] == '^')
                    {
                        Blizzard2 b = new(y - 1, -1);
                        columns[x - 1].Add(b);
                    }
                    if (lines[y][x] == 'v')
                    {
                        Blizzard2 b = new(y - 1, 1);
                        columns[x - 1].Add(b);
                    }
                }
            }
            width = lines[0].Length - 2;
            height = lines.Length - 2;

            //x = 0;
            //y = - 1;
            //State s = new State(x, y);
            //states.Add(s);
            int time = FoundPath(1, 0, 0, width - 1, height - 1);
            Console.WriteLine(time);
            time = FoundPath(time + 1, width - 1, height - 1, 0, 0);
            Console.WriteLine(time);
            time = FoundPath(time + 1, 0, 0, width - 1, height - 1);
            Console.WriteLine(time);

            Console.WriteLine("");
        }

        private static int FoundPath(int time, int startX, int startY, int endX, int endY)
        {
            List<State> states = new List<State>();
            while (true)
            {
                State s = new State(startX, startY);
                if (!CheckCollide(time, s.X, s.Y, s.X, s.Y))
                {
                    if (!states.Exists(x => x.X == s.X && x.Y == s.Y))
                    {
                        states.Add(s);
                    }
                }
                time++;
                if (time % 100 == 0)
                    Console.WriteLine("Time is " + time);
                List<State> newStates = new List<State>();
                for (int i = 0; i < states.Count; i++)
                {
                    s = states[i];
                    if (s.X == endX && s.Y == endY)
                    {
                        return time;
                    }
                    if (s.X > 0 && !CheckCollide(time, s.X - 1, s.Y, s.X, s.Y))
                    {
                        if (!newStates.Exists(x => x.X == s.X - 1 && x.Y == s.Y))
                        {
                            State s2 = new State(s.X - 1, s.Y);
                            newStates.Add(s2);
                        }
                    }
                    if (s.X < width - 1 && !CheckCollide(time, s.X + 1, s.Y, s.X, s.Y))
                    {
                        if (!newStates.Exists(x => x.X == s.X + 1 && x.Y == s.Y))
                        {
                            State s2 = new State(s.X + 1, s.Y);
                            newStates.Add(s2);
                        }
                    }
                    if (s.Y > 0 && !CheckCollide(time, s.X, s.Y - 1, s.X, s.Y))
                    {
                        if (!newStates.Exists(x => x.X == s.X && x.Y == s.Y - 1))
                        {
                            State s2 = new State(s.X, s.Y - 1);
                            newStates.Add(s2);
                        }
                    }
                    if (s.Y < height - 1 && !CheckCollide(time, s.X, s.Y + 1, s.X, s.Y))
                    {
                        if (!newStates.Exists(x => x.X == s.X && x.Y == s.Y + 1))
                        {
                            State s2 = new State(s.X, s.Y + 1);
                            newStates.Add(s2);
                        }
                    }
                    if (!CheckCollide(time, s.X, s.Y, s.X, s.Y))
                    {
                        if (!newStates.Exists(x => x.X == s.X && x.Y == s.Y))
                        {
                            State s2 = new State(s.X, s.Y);
                            newStates.Add(s2);
                        }
                    }
                }
                states = newStates;
            }
        }

        private static bool CheckCollide(int time, int x, int y, int oldX, int oldY)
        {
            foreach (Blizzard2 b in rows[y])
            {
                int newX = b.Coord + time * b.Delta;
                while (newX < 0)
                    newX += width;
                if (newX % width == x)
                    return true;
            }
            foreach (Blizzard2 b in columns[x])
            {
                int newY = b.Coord + time * b.Delta;
                while (newY < 0)
                    newY += height;
                if (newY % height == y)
                    return true;
            }
            //if (oldX == x - 1)
            //{
            //    foreach (Blizzard2 b in rows[y])
            //    {
            //        if (b.Delta == -1 && (b.Coord + (time - 1) * b.Delta) % width == x)
            //            return true;
            //    }
            //}
            //if (oldX == x + 1)
            //{
            //    foreach (Blizzard2 b in rows[y])
            //    {
            //        if (b.Delta == 1 && (b.Coord + (time - 1) * b.Delta) % width == x)
            //            return true;
            //    }
            //}
            //if (oldY == y - 1)
            //{
            //    foreach (Blizzard2 b in columns[x])
            //    {
            //        if (b.Delta == -1 && (b.Coord + (time - 1) * b.Delta) % height == y)
            //            return true;
            //    }
            //}
            //if (oldY == y + 1)
            //{
            //    foreach (Blizzard2 b in columns[x])
            //    {
            //        if (b.Delta == 1 && (b.Coord + (time - 1) * b.Delta) % height == y)
            //            return true;
            //    }
            //}

            return false;
        }
    }
}

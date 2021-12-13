using System;
using System.Collections.Generic;

namespace AdventOfCode
{
    class Program
    {
        class Board
        {
            public int[] numbers;
            public bool[] taken;
            public bool won;
        }
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Board> boards = new List<Board>();
            int l = 2;
            while (l < lines.Length)
            {
                Board board = new Board();
                board.won = false;
                board.numbers = new int[25];
                board.taken= new bool[25];
                for (int y = 0; y < 5; y++)
                {
                    for (int x = 0; x < 5; x++)
                    {
                        board.numbers[y * 5 + x] = Int32.Parse(lines[l].Substring(x * 3, 2));
                        board.taken[y * 5 + x] = false;
                    }
                    l++;
                }
                l++;
                boards.Add(board); 
            }

            string[] numbers = lines[0].Split(',');
            foreach (string n in numbers)
            {
                int number = Int32.Parse(n);
                foreach (Board board in boards)
                {
                    for (int y = 0; y < 5; y++)
                    {
                        for (int x = 0; x < 5; x++)
                        {
                            if (board.numbers[y * 5 + x] == number)
                            {
                                board.taken[y * 5 + x] = true;
                            }
                        }
                    }

                }
                for (int b = 0; b < boards.Count; b++)
                {
                    Board board = boards[b];
                    if (board.won)
                    {
                        continue;
                    }
                    bool winner = false;
                    int score = 0;
                    for (int y = 0; y < 5; y++)
                    {
                        bool all = true;
                        for (int x = 0; x < 5; x++)
                        {
                            if (!board.taken[y * 5 + x])
                            {
                                all = false;
                            }
                        }
                        if (all)
                        {
                            score = 0;
                            for (int x = 0; x < 5; x++)
                            {
                                score += board.numbers[y * 5 + x];
                            }
                            winner = true;
                        }
                    }
                    for (int y = 0; y < 5; y++)
                    {
                        bool all = true;
                        for (int x = 0; x < 5; x++)
                        {
                            if (!board.taken[x * 5 + y])
                            {
                                all = false;
                            }
                        }
                        if (all)
                        {
                            score = 0;
                            for (int x = 0; x < 5; x++)
                            {
                                score += board.numbers[x * 5 + y];
                            }
                            winner = true;
                        }
                    }
                    if (winner)
                    {
                        board.won = true;
                        score = 0;
                        for (int y = 0; y < 5; y++)
                        {
                            for (int x = 0; x < 5; x++)
                            {
                                if (!board.taken[x * 5 + y])
                                {
                                    score += board.numbers[x * 5 + y];
                                }
                            }
                        }
                        Console.WriteLine("Winner. Score = " + score + ", Number = " + number + ", Board = " + b + ", Total = " + score * number);//: " + o2 + ", CO2: " + co2);
                    }
                }
            }
            //Console.WriteLine("O2 : " + o2 + ", CO2: " + co2);
            //Console.WriteLine(o2 * co2);
        }
    }
}

using System;
using System.Collections.Generic;
using System.Numerics;

namespace Day_20
{
    class Program
    {
        static void Main(string[] args)
        {
            int numRoll = 0;
            int[] score = new int[2];
            int[] pos = new int[2];
            pos[0] = 5;
            pos[1] = 6;
            //pos[0] = 3;
            //pos[1] = 7;
            score[0] = 0;
            score[1] = 0;
            int player = 0;
            while (score[0] < 1000 && score[1] < 1000)
            {
                int rolls = ++numRoll + ++numRoll + ++numRoll;
                pos[player] += rolls;
                pos[player] %= 10;
                score[player] += (pos[player] + 1);

                player++;
                player %= 2;
            }
            Console.WriteLine(Math.Min(score[0], score[1]) * numRoll);

            List<Universe> universe = new List<Universe>();
            //pos[0] = 5;
            //pos[1] = 6;
            pos[0] = 3;
            pos[1] = 7;
            int[] variants = new int[] { 1, 3, 6, 7, 6, 3, 1 };
            universe.Add(new Universe(5, 6, 0, 0, 0, 1));
            Int64[] wins = new Int64[2];
            wins[0] = 0;
            wins[1] = 0;
            while (universe.Count > 0)
            {
                Universe u = universe[0];

                for (int v1 = 0; v1 < variants.Length; v1++)
                {
                    bool found = false;
                    pos[0] = u.pos[0];
                    pos[1] = u.pos[1];
                    score[0] = u.score[0];
                    score[1] = u.score[1];
                    player = u.player;
                    int rolls = v1 + 3;
                    pos[player] += rolls;
                    pos[player] %= 10;
                    score[player] += (pos[player] + 1);
                    if (score[player] >= 21)
                    {
                        wins[player] += u.num * variants[v1];
                    }
                    else
                    {
                        player++;
                        player %= 2;

                        foreach (Universe u2 in universe)
                        {
                            if (u2.pos[0] == pos[0] && u2.pos[1] == pos[1] && u2.score[0] == score[0] && u2.score[1] == score[1] && u2.player == player)
                            {
                                found = true;
                                u2.num += u.num * variants[v1];
                                break;
                            }
                        }
                        if (!found)
                        {
                            universe.Add(new(pos[0], pos[1], score[0], score[1], player, u.num * variants[v1]));
                        }
                    }
                }
                universe.RemoveAt(0);
            }
            Console.WriteLine(wins[0] + " - " + wins[1]);

        }
        private class Universe
        {
            public int[] pos = new int[2];
            public int[] score = new int[2];
            public int player;
            public Int64 num;

            public Universe(int pos1, int pos2, int score1, int score2, int player, Int64 num)
            {
                pos[0] = pos1;
                pos[1] = pos2;
                score[0] = score1;
                score[1] = score2;
                this.player = player;
                this.num = num;
            }
        }
    }
}

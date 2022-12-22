using System;
using System.Data;
using System.Diagnostics;

namespace AdventOfCode
{
    class Program
    {
        static int y;
        static int x;
        static string[] map;
        static int f;
        static void Main()
        {
            // Facing r=0, d=1, l=2, u=3
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            map = new string[lines.Length - 2];
            int maxX = 0;
            for (int i = 0; i < lines.Length - 2; i++)
            {
                maxX = Math.Max(maxX, lines[i].Length);
            }
            for (int i = 0; i < lines.Length - 2; i++)
            {
                if (lines[i].Length != maxX)
                    map[i] = lines[i] + new string(' ', maxX - lines[i].Length);
                else
                    map[i] = lines[i];
            }
            string inst = lines[lines.Length - 1];

            for (int yt = 0; yt < map.Length; yt++)
            {
                for (int xt = 0; xt < map[yt].Length; xt++)
                {
                    for (int ft = 0; ft < 4; ft++)
                    {
                        if (map[yt][xt] == '.')
                        {
                            x = xt;
                            y = yt;
                            f = ft;
                            if (yt == 149 && xt == 50 && ft == 1)
                                f = f;
                            if (ft == 0)
                                MoveRightP2();
                            else if (f == 1)
                                MoveDownP2();
                            else if (f == 2)
                                MoveLeftP2();
                            else
                                MoveUpP2();
                            if (x != xt || y != yt || f != ft)
                            {
                                f += 2;
                                if (f > 3)
                                    f -= 4;
                                if (f == 0)
                                    MoveRightP2();
                                else if (f == 1)
                                    MoveDownP2();
                                else if (f == 2)
                                    MoveLeftP2();
                                else
                                    MoveUpP2();
                                f += 2;
                                if (f > 3)
                                    f -= 4;
                                Debug.Assert(x == xt && y == yt && f == ft);
                            }
                        }
                    }
                }
            }

            RunInstructions(inst, false);
            RunInstructions(inst, true);
        }

        private static void RunInstructions(string inst, bool p2)
        {
            f = 0;
            y = 0;
            x = 0;
            while (map[y][x] != '.')
                x++;
            bool isMove = true;
            int iPtr = 0;
            while (iPtr < inst.Length)
            {
                if (isMove)
                {
                    int steps = 0;
                    while (iPtr < inst.Length && inst[iPtr] <= '9' && inst[iPtr] >= '0')
                    {
                        steps *= 10;
                        steps += inst[iPtr++] - '0';
                    }
                    while (steps > 0)
                    {
                        if (f == 0)
                        {
                            if (p2)
                                MoveRightP2();
                            else
                                MoveRight();
                        }
                        else if (f == 1)
                        {
                            if (p2)
                                MoveDownP2();
                            else
                                MoveDown();
                        }
                        else if (f == 2)
                        {
                            if (p2)
                                MoveLeftP2();
                            else
                                MoveLeft();
                        }
                        else
                        {
                            if (p2)
                                MoveUpP2();
                            else
                                MoveUp();
                        }
                        steps--;
                    }
                    isMove = false;
                }
                else
                {
                    if (inst[iPtr++] == 'R')
                    {
                        if (++f == 4)
                            f = 0;
                    }
                    else
                    {
                        if (--f == -1)
                            f = 3;

                    }
                    isMove = true;
                }
            }

            // 162169
            Console.WriteLine(1000 * (y + 1) + 4 * (x + 1) + f);
        }

        private static void MoveUp()
        {
            int newY = y - 1;
            // Wrapping?
            if (newY < 0 || map[newY][x] == ' ')
            {
                newY = map.Length - 1;
                while (map[newY][x] == ' ')
                {
                    newY--;
                }
            }
            if (map[newY][x] == '#')
                newY = y;
            y = newY;
        }

        private static void MoveUpP2()
        {
            int newX = x;
            int newY = y - 1;
            int newF = f;
            // Wrapping?
            if (newY < 0  || map[newY][x] == ' ')
            {
                if (newY < 0 && x < 100)
                {
                    newX = 0;
                    newY = 150 + (x - 50);
                    newF = 0;
                }
                else if (newY == 99)
                {
                    newX = 50;
                    newY = 50 + (x - 0);
                    newF = 0;
                }
                else
                {
                    newX = 0 + (x - 100);
                    newY = 199;
                    newF = 3;
                }
            }
            if (map[newY][newX] == '#')
                return;
            x = newX;
            y = newY;
            f = newF;
        }

        private static void MoveLeft()
        {
            int newX = x - 1;
            // Wrapping?
            if (newX < 0 || map[y][newX] == ' ')
            {
                newX = map[y].Length - 1;
                while (map[y][newX] == ' ')
                {
                    newX--;
                }
            }
            if (map[y][newX] == '#')
                newX = x;
            x = newX;
        }

        private static void MoveLeftP2()
        {
            int newX = x - 1;
            int newY = y;
            int newF = f;
            // Wrapping?
            if (newX < 0 || map[y][newX] == ' ')
            {
                if (newX < 0 && y < 150)
                {
                    newX = 50;
                    newY = 0 + (149 - y);
                    newF = 0;
                }
                else if (newX < 0)
                {
                    newX = 50 + (y - 150);
                    newY = 0;
                    newF = 1;
                }
                else if (x == 50 && newY < 50)
                {
                    newX = 0;
                    newY = 149 - (y - 0);
                    newF = 0;
                }
                else
                {
                    newX = 0 + (y - 50);
                    newY = 100;
                    newF = 1;
                }
            }
            if (map[newY][newX] == '#')
                return;
            x = newX;
            y = newY;
            f = newF;
        }
        private static void MoveDown()
        {
            int newY = y + 1;
            // Wrapping?
            if (newY >= map.Length || map[newY][x] == ' ')
            {
                newY = 0;
                while (map[newY][x] == ' ')
                {
                    newY++;
                }
            }
            if (map[newY][x] == '#')
                newY = y;
            y = newY;
        }
        private static void MoveDownP2()
        {
            int newX = x;
            int newY = y + 1;
            int newF = f;
            // Wrapping?
            if (newY >= map.Length || map[newY][x] == ' ')
            {
                if (newY >= map.Length)
                {
                    newX = 100 + (x - 0);
                    newY = 0;
                    newF = f;
                }
                else if (newY == 150)
                {
                    newX = 49;
                    newY = 150 + (x - 50);
                    newF = 2;
                }
                else
                {
                    newX = 99;
                    newY = 50 + (x - 100);
                    newF = 2;
                }
            }
            if (map[newY][newX] == '#')
                return;
            x = newX;
            y = newY;
            f = newF;
        }

        private static void MoveRight()
        {
            int newX = x + 1;
            // Wrapping?
            if (newX >= map[y].Length || map[y][newX] == ' ')
            {
                newX = 0;
                while (map[y][newX] == ' ')
                {
                    newX++;
                }
            }
            if (map[y][newX] == '#')
                newX = x;
            x = newX;
        }
        private static void MoveRightP2()
        {
            int newX = x + 1;
            int newY = y;
            int newF = f;
            // Wrapping?
            if (newX >= map[y].Length || map[y][newX] == ' ')
            {
                if (newX == map[y].Length)
                {
                    newX = 99;
                    newY = 149 - (y - 0);
                    newF = 2;
                }
                else if (y < 100)
                {
                    newX = 100 + (y  - 50);
                    newY = 49;
                    newF = 3;
                }
                else if (y < 150)
                {
                    newX = 149;
                    newY = 49 - (y - 100);
                    newF = 2;
                }
                else
                {
                    newX = 50 + (y - 150);
                    newY = 149;
                    newF = 3;
                }
            }
            if (map[newY][newX] == '#')
                return;
            x = newX;
            y = newY;
            f = newF;
        }
    }
}

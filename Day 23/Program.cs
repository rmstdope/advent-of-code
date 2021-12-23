
namespace Day_23
{
    class Program
    {
        static private long cost;
        static private long lowestCost;
        static private int inCorridor;
        static private Amphipod[] amphipods = new Amphipod[16];
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<char> chars = new();
            string[] s = lines[2].Split('#');
            chars.Add(s[3][0]);
            chars.Add(s[4][0]);
            chars.Add(s[5][0]);
            chars.Add(s[6][0]);
            s = lines[3].Split('#');
            chars.Add(s[1][0]);
            chars.Add(s[2][0]);
            chars.Add(s[3][0]);
            chars.Add(s[4][0]);
            s = lines[4].Split('#');
            chars.Add(s[1][0]);
            chars.Add(s[2][0]);
            chars.Add(s[3][0]);
            chars.Add(s[4][0]);
            s = lines[5].Split('#');
            chars.Add(s[1][0]);
            chars.Add(s[2][0]);
            chars.Add(s[3][0]);
            chars.Add(s[4][0]);
            int p = 0;
            while (p < 16)
            {
                for (int i = 0; i < chars.Count; i++)
                {
                    if (chars[i] == 'A' + p / 4)
                    {
                        amphipods[p] = new Amphipod(11 + i, p);
                        p++;
                    }
                }
            }
            inCorridor = 0;
            lowestCost = long.MaxValue;
            cost = 0;
            //inCorridor = 0;

            Move();

            Console.WriteLine(lowestCost);
        }
        static internal void Move()
        {
            // Check if we are too expensive
            if (cost >= lowestCost)
                return;

            // Check if we are done
            bool done = true;
            for (int i = 0; i < amphipods.Length; i++)
            {
                if (amphipods[i].Pos != 11 + i / 4 &&
                    amphipods[i].Pos != 15 + i / 4 &&
                    amphipods[i].Pos != 19 + i / 4 &&
                    amphipods[i].Pos != 23 + i / 4)
                    done = false;
            }
            if (done)
            {
                lowestCost = cost;
                Console.WriteLine(lowestCost);
            }

            // Start moving
            {
                //int numMoved = 0;
                //string dString = "";
                //string dString2 = "";
                //for (int i = 0; i < amphipods.Length; i++)
                //{
                //    if (amphipods[i].DoneMoving())
                //    {
                //        numMoved++;
                //        dString = dString + "1";
                //        dString2 += amphipods[i].Pos.ToString() + ", ";
                //    }
                //    else
                //    {
                //        dString = dString + "0";
                //    }
                //}
                //Console.WriteLine(dString);
                //Console.WriteLine(dString2);
                for (int i = 0; i < amphipods.Length; i++)
                {
                    Amphipod a = amphipods[i];
                    // Are we already in place?
                    if (a.Pos == 23 + (i / 4) ||
                        (a.Pos == 19 + (i / 4) && a.WhoIsThere(23 + (i / 4)) / 4 == i / 4) ||
                        (a.Pos == 15 + (i / 4) && a.WhoIsThere(19 + (i / 4)) / 4 == i / 4 && a.WhoIsThere(23 + (i / 4)) / 4 == i / 4) ||
                        (a.Pos == 11 + (i / 4) && a.WhoIsThere(15 + (i / 4)) / 4 == i / 4 && a.WhoIsThere(19 + (i / 4)) / 4 == i / 4 && a.WhoIsThere(23 + (i / 4)) / 4 == i / 4))
                        continue;
                    List<int> tries = new List<int>();
                    int save = a.Pos;
                    // Try to move to another place

                    // Move to finish?
                    for (int j = 0; j < 4; j++)
                    {
                        if (a.WhoIsThere(11 + j * 4 + (i / 4)) == -1)
                        {
                            tries.Clear();
                            tries.Add(11 + j * 4 + (i / 4));
                        }
                        else if (a.WhoIsThere(11 + j * 4 + (i / 4)) / 4 == i / 4)
                        {
                            continue;
                        }
                        else
                        {
                            tries.Clear();
                            break;
                        }
                    }

                    // If not, move into corridor
                    if (inCorridor < 8 && tries.Count == 0 && a.Pos > 10)
                    {
                        for (int q = 0; q < 11; q++)
                        {
                            if (q != 2 && q != 4 && q != 6 && q != 8)
                                tries.Add(q);
                        }
                    }

                    // Try to move
                    foreach (int c in tries)
                    {
                        if (a.TryMoveTo(c))
                        {
                            int delta = a.CostTo(c);
                            // Keep moving
                            cost += delta;
                            //if (a.Pos > 10)
                            //    Console.WriteLine("Moved " + i + " from " + save + " to " + a.Pos + " at cost " + delta);
                            if (save <= 10 && a.Pos > 10)
                                inCorridor--;
                            if (save > 10 && a.Pos <= 10)
                                inCorridor++;
                            Move();
                            if (save <= 10 && a.Pos > 10)
                                inCorridor++;
                            if (save > 10 && a.Pos <= 10)
                                inCorridor--; cost -= delta;
                            //if (a.Pos > 10)
                            //    Console.WriteLine("Moved " + i + " back to " + a.Pos);
                            a.Return(save);
                        }
                    }
                }
            }
        }

        private class Amphipod
        {
            public int Pos { get; set; }
            public bool HaveMoved { get; set; }
            public int Index{ get; set; }
            public int BaseCost { get; }
            private int numSteps;

            public Amphipod(int pos, int index)
            {
                Pos = pos;
                HaveMoved = false;
                Index = index;
                int pow = (Index / 4);
                BaseCost = 1;
                while (pow > 0)
                {
                    BaseCost *= 10;
                    pow--;
                }
            }

            internal bool InARoom()
            {
                return Pos > 10;
            }

            internal bool TryMoveTo(int c)
            {
                numSteps = 0;
                // Can only move once into the corridor and otherwise not if it has already moved
                //if (HaveMoved)
                //{
                //    if (c <= 10)
                //        return false;
                //    if (Pos > 10)
                //        return false;
                //}

                // Don't move within a room
                //if (Pos > 14 && c == Pos - 4)
                //    return false;

                // Check that we are ok to move into a room
                //if (c > 10 && c < 15)
                //{
                //    for (int a = 0; a < amphipods.Length; a++)
                //    {
                //        if (amphipods[a].Pos == c + 4 &&
                //            a / 2 != Index)
                //            return false;
                //    }
                //}

                // Check that we are ok to move into corridor
                if (c <= 10)
                {
                    if ((c == 2 && (Pos == 11 || Pos == 15 || Pos == 19 || Pos == 23)) ||
                        (c == 4 && (Pos == 12 || Pos == 16 || Pos == 20 || Pos == 24)) ||
                        (c == 6 && (Pos == 13 || Pos == 17 || Pos == 21 || Pos == 25)) ||
                        (c == 8 && (Pos == 14 || Pos == 18 || Pos == 22 || Pos == 26)))
                        return false;
                }

                // Anyone blocking path?
                int temp = Pos;
                // Get out
                while (temp > 10)
                {
                    numSteps++;
                    if (temp > 14)
                    {
                        temp -= 4;
                    }
                    else
                    {
                        temp -= (9 - (temp - 11));
                    }
                    if (AnyoneThere(temp))
                        return false;
                }
                // Move along corridor
                int add = 1;
                int cDest = c;
                while (cDest > 10)
                {
                    if (cDest > 14)
                    {
                        cDest -= 4;
                    }
                    else
                    {
                        cDest -= (9 - (cDest - 11));
                    }
                }
                if (cDest < temp)
                    add = -1;
                while (temp != cDest)
                {
                    numSteps++;
                    temp += add;
                    if (AnyoneThere(temp))
                        return false;
                }

                // Move into room
                while (temp != c)
                {
                    numSteps++;
                    if (temp > 10)
                    {
                        temp += 4;
                    }
                    else
                    {
                        temp = 11 + (temp - 2) / 2;
                    }
                    if (AnyoneThere(temp))
                        return false;
                }

                Pos = temp;
                HaveMoved = true;

                return true;
            }

            internal bool AnyoneThere(int pos)
            {
                for (int a = 0; a < amphipods.Length; a++)
                {
                    if (Index != a && amphipods[a].Pos == pos)
                        return true;
                }
                return false;
            }

            internal int WhoIsThere(int pos)
            {
                for (int a = 0; a < amphipods.Length; a++)
                {
                    if (Index != a && amphipods[a].Pos == pos)
                        return a;
                }
                return -1;
            }

            internal void Return(int save)
            {
                Pos = save;
                if (save > 10)
                    HaveMoved = false;
            }

            internal int CostTo(int c)
            {
                return BaseCost * numSteps;
            }

            internal bool DoneMoving()
            {
                return (HaveMoved && Pos > 10);
            }
        }
    }
}

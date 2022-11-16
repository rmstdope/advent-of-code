using System;
using System.Collections.Generic;
using System.Numerics;

namespace Day_19
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            Scanner scanner = new();
            List<Scanner> scanners = new List<Scanner>();
            List<Scanner> noOverlap = new List<Scanner>();
            List<Scanner> notChecked = new List<Scanner>();
            List<Scanner> isChecked = new List<Scanner>();
            foreach (string line in lines)
            {
                if (line.Length > 0)
                {
                    if (line[0] == '-' && line[1] == '-')
                    {
                        scanner = new();
                        scanners.Add(scanner);
                        if (scanners.Count != 1)
                            noOverlap.Add(scanner);
                        else
                            notChecked.Add(scanner);
                    }
                    else
                    {
                        string[] c = line.Split(',');
                        scanner.AddCoord(int.Parse(c[0]), int.Parse(c[1]), int.Parse(c[2]));
                    }
                }
            }
            foreach (Scanner s in scanners)
            {
                s.CreatePermutations();
            }
            notChecked[0].Diff = new Vector3(0, 0, 0);
            while (noOverlap.Count > 0 && notChecked.Count > 0)
            {
                //int i = notChecked.Count - 1;
                //for (int i = 0; i < notChecked.Count; i++)
                {
                    for (int j = 0; j < noOverlap.Count; j++)
                    {
                        for (int l = 0; l < 24; l++)
                        {
                            noOverlap[j].SetPermutation(l);
                            Vector3 diff;
                            if (notChecked[0].DoesOverlap12(noOverlap[j], out diff))
                            {
                                noOverlap[j].Diff = notChecked[0].Diff + diff;
                                notChecked.Add(noOverlap[j]);
                                noOverlap.RemoveAt(j);
                                l = 1000;
                                //i = 1000;
                                //j = 1000;
                                j--;
                            }
                        }
                        //Console.WriteLine(j);
                    }
                    //Console.WriteLine(i);
                }
                isChecked.Add(notChecked[0]);
                notChecked.RemoveAt(0);
                Console.WriteLine("Iterating " + noOverlap.Count + "," + notChecked.Count);
            }
            List<Vector3> probes = new();
            foreach (Scanner s in scanners)
            {
                foreach (Vector3 v in s.GetPermutation())
                {
                    bool found = false;
                    foreach (Vector3 v2 in probes)
                    {
                        if (v2 == (v + s.Diff))
                            found = true;
                    }
                    if (!found)
                    {
                        probes.Add(v + s.Diff);
                    }
                }
            }
            Console.WriteLine(probes.Count);
            int dist = 0;
            for (int i = 0; i < scanners.Count; i++)
            {
                for (int j = i + 1; j < scanners.Count; j++)
                {
                    int diffX = (int)(scanners[i].Diff.X - scanners[j].Diff.X);
                    int diffY = (int)(scanners[i].Diff.Y - scanners[j].Diff.Y);
                    int diffZ = (int)(scanners[i].Diff.Z - scanners[j].Diff.Z);
                    dist = Math.Max(dist, Math.Abs(diffX) + Math.Abs(diffY) + Math.Abs(diffZ));
                }
            }
            Console.WriteLine(dist);
        }
        private class Scanner
        {
            private List<List<Vector3>> permutations;
            private List<Vector3> coord;
            private int permutation;

            public Vector3 Diff { get; internal set; }

            public Scanner()
            {
                permutations = new();
                coord = new List<Vector3>();
            }
            internal void AddCoord(int x, int y, int z)
            {
                coord.Add(new(x, y, z));
            }

            internal void CreatePermutations()
            {
                for (int i = 0; i < 24; i++)
                {
                    permutations.Add(new());
                }
                for (int i = 0; i < coord.Count; i++)
                {
                    permutations[0].Add(new Vector3(coord[i].X, coord[i].Y, coord[i].Z));
                    permutations[1].Add(new Vector3(coord[i].X, -coord[i].Z, coord[i].Y));
                    permutations[2].Add(new Vector3(coord[i].X, -coord[i].Y, -coord[i].Z));
                    permutations[3].Add(new Vector3(coord[i].X, coord[i].Z, -coord[i].Y));

                    permutations[4].Add(new Vector3(-coord[i].X, coord[i].Y, -coord[i].Z));
                    permutations[5].Add(new Vector3(-coord[i].X, -coord[i].Z, -coord[i].Y));
                    permutations[6].Add(new Vector3(-coord[i].X, -coord[i].Y, coord[i].Z));
                    permutations[7].Add(new Vector3(-coord[i].X, coord[i].Z, coord[i].Y));

                    permutations[8].Add(new Vector3(coord[i].Y, -coord[i].Z, -coord[i].X));
                    permutations[9].Add(new Vector3(coord[i].Y, coord[i].X, -coord[i].Z));
                    permutations[10].Add(new Vector3(coord[i].Y, coord[i].Z, coord[i].X));
                    permutations[11].Add(new Vector3(coord[i].Y, -coord[i].X, coord[i].Z));

                    permutations[12].Add(new Vector3(-coord[i].Y, -coord[i].Z, coord[i].X));
                    permutations[13].Add(new Vector3(-coord[i].Y, coord[i].X, coord[i].Z));
                    permutations[14].Add(new Vector3(-coord[i].Y, coord[i].Z, -coord[i].X));
                    permutations[15].Add(new Vector3(-coord[i].Y, -coord[i].X, -coord[i].Z));

                    permutations[16].Add(new Vector3(coord[i].Z, coord[i].Y, -coord[i].X));
                    permutations[17].Add(new Vector3(coord[i].Z, coord[i].X, coord[i].Y));
                    permutations[18].Add(new Vector3(coord[i].Z, -coord[i].Y, coord[i].X));
                    permutations[19].Add(new Vector3(coord[i].Z, -coord[i].X, -coord[i].Y));

                    permutations[20].Add(new Vector3(-coord[i].Z, coord[i].Y, coord[i].X));
                    permutations[21].Add(new Vector3(-coord[i].Z, coord[i].X, -coord[i].Y));
                    permutations[22].Add(new Vector3(-coord[i].Z, -coord[i].Y, -coord[i].X));
                    permutations[23].Add(new Vector3(-coord[i].Z, -coord[i].X, coord[i].Y));
                }
            }

            internal bool DoesOverlap12(Scanner scanner, out Vector3 diff)
            {
                List<Vector3> a = GetPermutation();
                List<Vector3> b = scanner.GetPermutation();
                int num = 0;
                foreach (Vector3 v1 in a)
                {
                    foreach (Vector3 v2 in b)
                    {
                        num = 0;
                        diff = v1 - v2;
                        foreach (Vector3 v3 in a)
                        {
                            foreach (Vector3 v4 in b)
                            {
                                if ((v3 - (v4 + diff)).LengthSquared() < 1)
                                {
                                    num++;
                                    if (num == 12)
                                    {
                                        return true;
                                    }
                                }
                            }
                        }
                    }
                }
                diff = new Vector3();
                return false;
            }

            internal List<Vector3> GetPermutation()
            {
                return permutations[permutation];
            }
            internal void SetPermutation(int perm)
            {
                permutation = perm;
            }
        }
    }
}

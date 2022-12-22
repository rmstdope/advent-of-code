using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.InteropServices;

namespace AdventOfCode
{
    class Blueprint
    {
        public Blueprint(string data)
        {
            string[] b = data.Split(':');
            Id = int.Parse(b[0].Substring(10));

            string[] w = b[1].Split(' ');
            Costs = new List<int[]>();
            int[] c1 = { int.Parse(w[5]), 0, 0 };
            int[] c2 = { int.Parse(w[11]), 0, 0 };
            int[] c3 = { int.Parse(w[17]), int.Parse(w[20]), 0 };
            int[] c4 = { int.Parse(w[26]), 0, int.Parse(w[29]) };
            Costs.Add(c1);
            Costs.Add(c2);
            Costs.Add(c3);
            Costs.Add(c4);
        }

        public int Id { get; private set; }
        public List<int[]> Costs { get; private set; }
    }
    class State
    {
        public State(int time, int ore, int cla, int obs, int geo, int r1, int r2, int r3, int r4)
        {
            Time = time;
            Ore = ore;
            Cla = cla;
            Obs = obs;
            Geo = geo;
            R1 = r1;
            R2 = r2;
            R3 = r3;
            R4 = r4;
        }
        public override bool Equals(object obj)
        {
            if (obj is State)
            {
                State s = (State)obj;
                return Time == s.Time && Ore == s.Ore && Cla == s.Cla && Obs == s.Obs && /*Geo == s.Geo &&*/ R1 == s.R1 && R2 == s.R2 && R3 == s.R3 && R4 == s.R4;
            }
            return false;
        }
        public override int GetHashCode()
        {
            //System.Diagnostics.Debug.Assert(R4 < 32);
            //System.Diagnostics.Debug.Assert(R3 < 32);
            //System.Diagnostics.Debug.Assert(R2 < 32);
            //System.Diagnostics.Debug.Assert(R1 < 32);
            //System.Diagnostics.Debug.Assert(Ore < 64);
            //System.Diagnostics.Debug.Assert(Cla < 64);
            //System.Diagnostics.Debug.Assert(Obs < 32);
            //System.Diagnostics.Debug.Assert(Time < 64);
            int v = Time;
            v = v * 64 + Ore;
            v = v * 64 + Cla;
            v = v * 64 + Obs;
            //v = v * 32 + Geo;
            v = v * 32 + R1;
            v = v * 32 + R2;
            v = v * 32 + R3;
            v = v * 16 + R4;
            return v;
        }

        public int Time { get; set; }
        public int Ore { get; set; }
        public int Cla { get; set; }
        public int Obs { get; set; }
        public int Geo { get; set; }
        public int R1 { get; set; }
        public int R2 { get; set; }
        public int R3 { get; set; }
        public int R4 { get; set; }
    }
    class Program
    {
        public static int best = 0;
        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines("../../../input.txt");
            List<Blueprint> blueprints = new List<Blueprint>();
            foreach (string line in lines)
            {
                Blueprint blueprint = new Blueprint(line);
                blueprints.Add(blueprint);
            }
            Solve(blueprints, blueprints.Count, 24);
            Solve(blueprints, 3, 32);
        }

        private static void Solve(List<Blueprint> blueprints, int numPrints, int time)
        {
            int quality = 0;
            if (time == 32)
                quality = 1;
            for (int i = 0; i < numPrints; i++)
            {
                Blueprint blueprint = blueprints[i];
                Console.WriteLine("Blueprint " + blueprint.Id);
                int maxOreCost = Math.Max(Math.Max(Math.Max(blueprint.Costs[0][0], blueprint.Costs[1][0]), blueprint.Costs[2][0]), blueprint.Costs[3][0]);
                State start = new State(time, 0, 0, 0, 0, 1, 0, 0, 0);
                List<State> states = new();
                HashSet<State> visited = new HashSet<State>();
                states.Add(start);
                best = 0;
                while (states.Count > 0)
                {
                    State state = states[0];
                    states.RemoveAt(0);
                    if (state.Time == 0)
                    {
                        best = Math.Max(best, state.Geo);
                        continue;
                    }

                    // Need to reduce the number of visited nodes
                    if (state.R1 > maxOreCost)
                        continue;
                    if (state.Ore >= state.Time * maxOreCost - state.R1 * (state.Time - 1))
                        state.Ore = state.Time * maxOreCost - state.R1 * (state.Time - 1);
                    if (state.R2 > blueprint.Costs[2][1])
                        continue;
                    if (state.Cla >= state.Time * blueprint.Costs[2][1] - state.R2 * (state.Time - 1))
                        state.Cla = state.Time * blueprint.Costs[2][1] - state.R2 * (state.Time - 1);
                    if (state.R3 > blueprint.Costs[3][2])
                        continue;
                    if (state.Obs >= state.Time * blueprint.Costs[3][2] - state.R3 * (state.Time - 1))
                        state.Obs = state.Time * blueprint.Costs[3][2] - state.R3 * (state.Time - 1);

                    State nearlySame;
                    if (visited.TryGetValue(state, out nearlySame))//.Exists(x => x.Ore == state.Ore && x.Cla == state.Cla && x.Obs == state.Obs && x.Geo == state.Geo && x.R1 == state.R1 && x.R2 == state.R2 && x.R3 == state.R3 && x.R4 == state.R4 && x.Time == state.Time))
                    {
                        if (nearlySame.Geo < state.Geo)
                        {
                            visited.Remove(nearlySame);
                        }
                        else
                        {
                            continue;
                        }
                    }
                    visited.Add(state);

                    // Don't create unnecessary states
                    State newState = new State(state.Time - 1, state.Ore + state.R1, state.Cla + state.R2, state.Obs + state.R3, state.Geo + state.R4, state.R1, state.R2, state.R3, state.R4);
                    if (state.Ore >= blueprint.Costs[3][0] && state.Obs >= blueprint.Costs[3][2])
                    {
                        states.Add(new State(newState.Time, newState.Ore - blueprint.Costs[3][0], newState.Cla, newState.Obs - blueprint.Costs[3][2], newState.Geo, newState.R1, newState.R2, newState.R3, newState.R4 + 1));
                    }
                    else
                    {
                        int add = 0;
                        if (state.Ore >= blueprint.Costs[0][0])
                        {
                            states.Add(new State(newState.Time, newState.Ore - blueprint.Costs[0][0], newState.Cla, newState.Obs, newState.Geo, newState.R1 + 1, newState.R2, newState.R3, newState.R4));
                            add++;
                        }
                        if (state.Ore >= blueprint.Costs[1][0])
                        {
                            states.Add(new State(newState.Time, newState.Ore - blueprint.Costs[1][0], newState.Cla, newState.Obs, newState.Geo, newState.R1, newState.R2 + 1, newState.R3, newState.R4));
                            add++;
                        }
                        if (state.Ore >= blueprint.Costs[2][0] && state.Cla >= blueprint.Costs[2][1])
                        {
                            states.Add(new State(newState.Time, newState.Ore - blueprint.Costs[2][0], newState.Cla - blueprint.Costs[2][1], newState.Obs, newState.Geo, newState.R1, newState.R2, newState.R3 + 1, newState.R4));
                            add++;
                        }
                        if (add != 3)
                            states.Add(newState);
                    }
                }
                Console.WriteLine("Best is " + best);
                if (time == 32)
                    quality *= best;
                else
                    quality += best * blueprint.Id;
            }
            Console.WriteLine(quality);
        }

        private static void Build(Blueprint blueprint, int time, int[] material, int[] robots)
        {
            if (time == 24)
            {
                if (material[3] > best)
                    Console.WriteLine("Found " + material[3]);
                best = Math.Max(best, material[3]);
                return;
            }
            // Max number of clay we will be able to get if we spend the remaining time building clay robots
            int halfRemainingTime = (24 - time + 1) / 2;
            int maxClay = material[2] + halfRemainingTime * (robots[2] + (24 - time));
            // Max number of geo robots we will be able to build
            int maxGeo = (maxClay + blueprint.Costs[3][2] + 1) / blueprint.Costs[3][2];
            if (robots[0] > 10 || robots[1] > 7)
                return;
            if (best >= material[3] + (24 - time) / 2 * maxGeo)
            {
                //return;
            }
            int couldBuild = 0;
            for (int i = 3; i >= 0; i--)
            {
                if (material[0] >= blueprint.Costs[i][0] &&
                    material[1] >= blueprint.Costs[i][1] &&
                    material[2] >= blueprint.Costs[i][2])
                {
                    int[] newMaterials = new int[] {
                        material[0] + robots[0] - blueprint.Costs[i][0],
                        material[1] + robots[1] - blueprint.Costs[i][1],
                        material[2] + robots[2] - blueprint.Costs[i][2],
                        material[3] + robots[3]
                    };
                    int[] newRobots = robots.ToArray();
                    newRobots[i]++;
                    Build(blueprint, time + 1, newMaterials, newRobots);
                    if (i == 3)
                        return;
                    couldBuild += 1 << i;
                }
            }
            int[] newMaterials2 = new int[] { material[0] + robots[0], material[1] + robots[1], material[2] + robots[2], material[3] + robots[3] };
            int[] newRobots2 = robots.ToArray();
            if (couldBuild < 7)
            {
                Build(blueprint, time + 1, newMaterials2, newRobots2);
            }
        }
    }
}

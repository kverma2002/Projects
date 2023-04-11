#include <cmath>
#include "heur.h"
#include <vector>
#include <set>
using namespace std;


// Complete
size_t BFSHeuristic::compute(const Board& b)
{
    return 0U;
}


// To be completed
size_t DirectHeuristic::compute(const Board& b)
{
    // Avoid compiler warnings -- replace this
    Board::VehicleMap inRowA = vehiclesAcrossA(b);
    return inRowA.size();
}

Board::VehicleMap DirectHeuristic::vehiclesAcrossA(const Board& b)
{
    Board::VehicleMap inRowA;
    Vehicle escapeJawn = b.escapeVehicle();
    for(int i = escapeJawn.startc + escapeJawn.length; i < b.size(); i++)
    {
        Board::VID_T it = b.at(escapeJawn.startr, i);
        {
            if(it != Vehicle::INVALID_ID )
            {
                inRowA.insert(std::make_pair(it, b.vehicle(it)));
            }
        }
    }
    return inRowA;
}


// To be completed
size_t IndirectHeuristic::compute(const Board& b)
{
    Board::VehicleMap inRowA = vehiclesAcrossA(b);
    Board::VehicleMap::iterator it;
    Vehicle a = b.escapeVehicle();
    std::set<Board::VID_T> indirectVehicles;
    for(it = inRowA.begin(); it != inRowA.end(); it ++)
    {
        int jawn = canVehicleBothWay(it->second, b.size(), a.startr);
        if(jawn != 3)
        {
            if(jawn == 1)
            {
                for(int i = it->second.startr - 1; i >= 0.; i--)
                {
                    Board::VID_T above = b.at(i, it->second.startc);
                    {
                        if(above != Vehicle::INVALID_ID)
                        {
                            indirectVehicles.insert(above);
                        }
                    }
                }
            }
            else if(jawn == 2)
            {
                for(int i = it->second.startr + it->second.length; i < b.size(); i++)
                {
                    Board::VID_T below = b.at(i, it->second.startc);
                    {
                        if(below != Vehicle::INVALID_ID)
                        {
                            indirectVehicles.insert(below);
                        }
                    }
                }
            }
        }
    }
    return inRowA.size() + indirectVehicles.size();
}

Board::VehicleMap IndirectHeuristic::vehiclesAcrossA(const Board& b)
{
    Board::VehicleMap inRowA;
    Vehicle escapeJawn = b.escapeVehicle();
    for(int i = escapeJawn.startc + escapeJawn.length; i < b.size(); i++)
    {
        Board::VID_T it = b.at(escapeJawn.startr, i);
        {
            if(it != Vehicle::INVALID_ID)
            {
                inRowA.insert(std::make_pair(it, b.vehicle(it)));
            }
        }
    }
    return inRowA;
}

int IndirectHeuristic::canVehicleBothWay(Vehicle x, int sizeOfGrid, int aRow)
{
    int i = 0;
    if(x.length <= aRow)
    {
        i += 1;
    }
    if(sizeOfGrid - x.length > aRow)
    {
        i += 2;
    }
    return i;
}


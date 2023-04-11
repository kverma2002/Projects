#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include "solver.h"
#include <iostream>

using namespace std;

// To be completed
Solver::Solver(const Board& b, Heuristic *heur)
{
    b_ = new Board(b);
    this->heur_ = heur;
}

// To be completed
Solver::~Solver()
{
    delete b_;
}

// To be completed
bool Solver::run()
{
    bool solved = false;
    MoveScoreComp comp;
    MoveHeap openList = MoveHeap(2, comp);
    MoveSet closedLists;
    Move* original = new Move(b_);
    if(original->b->solved())
    {
        delete original;
        return true;
    }
    openList.push(original);
    closedLists.insert(original);
    Board::MovePairList potMoves;
    while(!openList.empty())
    {
        Move* top = openList.top();
        openList.pop();
        potMoves.clear();
        potMoves = top->b->potentialMoves();
        Board::MovePairList::iterator it;
        for(it = potMoves.begin(); it != potMoves.end(); it ++)
        {
            Move* temp = new Move(*it, top->b, top);
            temp->score(heur_);
            MoveSet::iterator it2 = closedLists.find(temp);
            if(it2 == closedLists.end())
            {
                expansions_ +=1;
                openList.push(temp);
                closedLists.insert(temp);
                if(temp->b->solved())
                {
                    solved = true;
                    Stack<Board::MovePair> jawn;
                    while (temp->prev != NULL)
                    {

                        jawn.push(temp->m);
                        temp = temp->prev;
                    }
                    while(!jawn.empty())
                    {
                        solution_.push_back(jawn.top());
                        jawn.pop();
                    }
                }
            }
            else
            {
                delete temp;
            }
        }
        if(solved)
        {
            break;
        }
    }
    MoveSet::iterator it2 = closedLists.begin();
    while(it2 != closedLists.end())
    {
        delete *it2;
        it2++;
    }
    return solved;
    /*
    if(!solved)
    {
        MoveSet::iterator it2 = closedLists.begin();
        while(it2 != closedLists.end())
        {
            delete *it2;
            it2++;
        }
        return false;
        
    }
    else
    {
        MoveSet::iterator it2 = closedLists.begin();
        while(it2 != closedLists.end())
        {
            delete *it2;
            it2++;
        }
        return true;
    }
    */
}

// To be completed
Board::MovePairList Solver::solution() const
{
    // Avoid compiler warnings - replace this
    return solution_;
}

// Complete
size_t Solver::numExpansions() const
{
    return expansions_;
}

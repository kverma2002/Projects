#include "move.h"


// Complete
Move::Move(Board* board)
{
    m.first = Vehicle::INVALID_ID;
    m.second = 0;
    b = board;
    g = 0;
    h = 0;
    prev = NULL;
}

// To be completed
Move::Move(const Board::MovePair& move, Board* b,  Move *parent)
{
    m = move;
    this->b = new Board(*b);
    this->b->move(m.first, m.second);
    g = parent->g + 1;
    h = 0;
    prev = parent;
}

// To be completed
Move::~Move()
{
    delete b;
}

// To be completed
bool Move::operator<(const Move& rhs) const
{
    if((this->h + this->g) < (rhs.h + rhs.g))
    {
        return true;
    }
    else if ((rhs.h + rhs.g) < (this->h + this->g))
    {
        return false;
    }
    else 
    {
        if(this->h < rhs.h)
        {
            return true;
        }
        else if(rhs.h < this->h)
        {
            return false;
        }
        else
        {
            return (this->b < rhs.b);
        }
    }
}


// To be completed
void Move::score(Heuristic *heur) 
{
    h = heur->compute(*b);
}

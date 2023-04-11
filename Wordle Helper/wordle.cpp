// For debugging
#include <iostream>
// For std::remove
#include <algorithm> 
#include <map>
#include <set>
#include "wordle.h"
#include "dict-eng.h"
using namespace std;


void possibleFloatCombos(set<string>& stringSet, const string &in, const string &flTS, int start, int dashes, const std::set<std::string> &dic);
void faneto(string dash, set<string>& stringSet, int start, int added, const std::set<std::string> &dic);

// Definition of primary wordle function
std::set<std::string> wordle(
    const std::string& in,
    const std::string& floating,
    const std::set<std::string>& dict)
{
    std::set<std::string> floatCombo;
    
    int dashes = 0;
    for(int i = 0; i < in.size(); ++i)
    {
        if(in[i] == '-')
        {
            dashes +=1;
        }
    }
    possibleFloatCombos(floatCombo, in, floating, 0, dashes - floating.size(), dict);

    return floatCombo;
    

}

void possibleFloatCombos(set<string>& stringSet, const string &in, const string &flTS, int start, int dashes, const std::set<std::string> &dic)
{
    if(flTS == "")
    {
        faneto(in, stringSet, 0, dashes, dic);
    }
    else
    {
        for(int i = 0; i < flTS.size(); ++i)
        {
            for(int j = start; j < in.size(); ++j)
            {
                if(in.at(j) == '-')
                {
                    string temp1 = in;
                    string temp2 = flTS;
                    possibleFloatCombos(stringSet, temp1.replace(j, 1, temp2.substr(i, 1)), temp2.replace(i, 1, ""), j + 1, dashes, dic);
                }
            }
        }
    }
}

void faneto(string dash, set<string>& stringSet, int start, int added, const std::set<std::string> &dic)
{
    if(added == 0)
    {
        
        set<string>::const_iterator it = dic.find(dash);
        if(it != dic.end())
        {
            stringSet.insert(dash);
        }
        
    }
    else
    {
        for(int i = 0; i < 26; i ++)
        {
            for(int j = start; j < dash.size(); ++j)
            {
                if(dash.at(j) == '-')
                {
                    string temp1 = dash;
                    string letter = "";
                    letter.push_back(char(i + 97));
                    faneto(temp1.replace(j, 1, letter), stringSet, j + 1, added - 1, dic);
                }
            }
        }
    }
}
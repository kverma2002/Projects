#ifndef RBBST_H
#define RBBST_H

#include <iostream>
#include <exception>
#include <cstdlib>
#include <algorithm>
#include "bst.h"

struct KeyError { };

template <typename Key, typename Value>
class AVLNode : public Node<Key, Value>
{
public:
    // Constructor/destructor.
    AVLNode(const Key& key, const Value& value, AVLNode<Key, Value>* parent);
    virtual ~AVLNode();

    // Getter/setter for the node's height.
    signed char getBalance () const;
    void setBalance (signed char balance);
    void updateBalance(signed char diff);

    // Getters for parent, left, and right. These need to be redefined since they
    // return pointers to AVLNodes - not plain Nodes. See the Node class in bst.h
    // for more information.
    virtual AVLNode<Key, Value>* getParent() const override;
    virtual AVLNode<Key, Value>* getLeft() const override;
    virtual AVLNode<Key, Value>* getRight() const override;

protected:
    signed char balance_;
};

/**
* An explicit constructor to initialize the elements by calling the base class constructor and setting
* the color to red since every new node will be red when it is first inserted.
*/
template<class Key, class Value>
AVLNode<Key, Value>::AVLNode(const Key& key, const Value& value, AVLNode<Key, Value> *parent) :
    Node<Key, Value>(key, value, parent), balance_(0)
{

}

/**
* A destructor which does nothing.
*/
template<class Key, class Value>
AVLNode<Key, Value>::~AVLNode()
{

}

/**
* A getter for the balance of a AVLNode.
*/
template<class Key, class Value>
signed char AVLNode<Key, Value>::getBalance() const
{
    return balance_;
}

/**
* A setter for the balance of a AVLNode.
*/
template<class Key, class Value>
void AVLNode<Key, Value>::setBalance(signed char balance)
{
    balance_ = balance;
}

/**
* Adds diff to the balance of a AVLNode.
*/
template<class Key, class Value>
void AVLNode<Key, Value>::updateBalance(signed char diff)
{
    balance_ += diff;
}

/**
* An overridden function for getting the parent since a static_cast is necessary to make sure
* that our node is a AVLNode.
*/
template<class Key, class Value>
AVLNode<Key, Value> *AVLNode<Key, Value>::getParent() const
{
    return static_cast<AVLNode<Key, Value>*>(this->parent_);
}

/**
* Overridden for the same reasons as above.
*/
template<class Key, class Value>
AVLNode<Key, Value> *AVLNode<Key, Value>::getLeft() const
{
    return static_cast<AVLNode<Key, Value>*>(this->left_);
}

/**
* Overridden for the same reasons as above.
*/
template<class Key, class Value>
AVLNode<Key, Value> *AVLNode<Key, Value>::getRight() const
{
    return static_cast<AVLNode<Key, Value>*>(this->right_);
}


template <class Key, class Value>
class AVLTree : public BinarySearchTree<Key, Value>
{
public:
    virtual void insert (const std::pair<const Key, Value> &new_item); // TODO
    virtual void remove(const Key& key);  // TODO
protected:
    virtual void nodeSwap( AVLNode<Key,Value>* n1, AVLNode<Key,Value>* n2);
    
    void rotateRight(AVLNode<Key,Value>* p);
    void rotateLeft(AVLNode<Key,Value>* n);
    bool isLeftChild(AVLNode<Key,Value>* n, AVLNode<Key,Value>* p);
    bool isRightChild(AVLNode<Key,Value>* n, AVLNode<Key,Value>* p);
    void insertFix( AVLNode<Key,Value>* p, AVLNode<Key,Value>* n);
    void removeFix(AVLNode<Key,Value>* n, signed char diff);


    // Add helper functions here
    static AVLNode<Key, Value>* predecessor(AVLNode<Key, Value>* current);
    AVLNode<Key, Value>* internalFind(const Key& k) const;

};

template<class Key, class Value>
bool AVLTree<Key, Value>::isLeftChild(AVLNode<Key,Value>* n, AVLNode<Key,Value>* p)
{
    return (p->getLeft() == n);
}

template<class Key, class Value>
bool AVLTree<Key, Value>::isRightChild(AVLNode<Key,Value>* n, AVLNode<Key,Value>* p)
{
    return (p->getRight() == n);
}

template<class Key, class Value>
void AVLTree<Key, Value>::rotateRight(AVLNode<Key,Value>* p)
{
    AVLNode<Key, Value>* c = p->getLeft();
    if(c == NULL)
    {
        return;
    }
    if(p->getParent() != NULL)
    {
        AVLNode<Key, Value>* g = p->getParent();
        c->setParent(g);
        if(this->isRightChild(p, g))
        {
            g->setRight(c);
        }
        else
        {
            g->setLeft(c);

        }
    }
    else
    {   
        this->root_ = c;
        c->setParent(NULL);
    }
    // When we have two children right subtree of c is attached to left of p
    if(c->getRight() != NULL)
    {
        AVLNode<Key, Value>* rSubC = c->getRight();
        p->setLeft(rSubC);
        rSubC->setParent(p);
    }
    else
    {
        p->setLeft(NULL);
    }
    p->setParent(c);
    c->setRight(p);
}

template<class Key, class Value>
void AVLTree<Key, Value>::rotateLeft(AVLNode<Key,Value>* p)
{
    AVLNode<Key, Value>* c = p->getRight();
    if(c == NULL)
    {
        return;
    }
    if(p->getParent() != NULL)
    {
        AVLNode<Key, Value>* g = p->getParent();
        c->setParent(g);
        if(this->isRightChild(p, g))
        {
            g->setRight(c);
        }
        else
        {
            g->setLeft(c);
        }
    }
    else
    {   
        this->root_ = c;
        c->setParent(NULL);
    }
    // When we have two children right subtree of c is attached to left of p
    if(c->getLeft() != NULL)
    {
        AVLNode<Key, Value>* lSubC = c->getLeft();
        p->setRight(lSubC);
        lSubC->setParent(p);
    }
    else
    {
        p->setRight(NULL);
    }
    p->setParent(c);
    c->setLeft(p);
}

template<class Key, class Value>
void AVLTree<Key, Value>::insertFix(AVLNode<Key,Value>* p, AVLNode<Key,Value>* n)
{
    if(p == NULL || p->getParent() == NULL)
    {
        // We are DONE
    }
    else
    {
        AVLNode<Key, Value>* g = p->getParent();
        if(this->isLeftChild(p, g))
        {
            g->updateBalance(-1);
            if(g->getBalance() == 0)
            {
                // We are DONE
            }
            else if(g->getBalance() == -1)
            {
                this->insertFix(g, p);
            }
            else if(g->getBalance() == -2)
            {
                // ZIG ZAG
                if(p->getBalance() == 1)
                {
                    // Rotate Left on p
                    this->rotateLeft(p);
                    this->rotateRight(g);
                    if((n->getBalance() == -1))
                    {
                        p->setBalance(0);
                        g->setBalance(1);
                        n->setBalance(0);
                    }
                    else if(n->getBalance() == 0)
                    {
                        p->setBalance(0);
                        g->setBalance(0);
                        n->setBalance(0);
                    }
                    else if(n->getBalance() == 1)
                    {
                        p->setBalance(-1);
                        g->setBalance(0);
                        n->setBalance(0);
                    }
                }
                else
                {
                    this->rotateRight(g);
                    g->setBalance(0);
                    p->setBalance(0);
                }
                
            }
        }
        else if(this->isRightChild(p, g))
        {
            g->updateBalance(1);
            if(g->getBalance() == 0)
            {
                // We are DONE
            }
            else if(g->getBalance() == 1)
            {
                this->insertFix(g, p);
            }
            else if(g->getBalance() == 2)
            {
                // ZIG ZAG
                if(p->getBalance() == -1)
                {
                    // Rotate Left on p
                    this->rotateRight(p);
                    this->rotateLeft(g);
                    if((n->getBalance() == 1))
                    {
                        p->setBalance(0);
                        g->setBalance(-1);
                        n->setBalance(0);
                    }
                    else if(n->getBalance() == 0)
                    {
                        p->setBalance(0);
                        g->setBalance(0);
                        n->setBalance(0);
                    }
                    else if(n->getBalance() == -1)
                    {
                        p->setBalance(1);
                        g->setBalance(0);
                        n->setBalance(0);
                    }
                }
                else
                {
                    this->rotateLeft(g);
                    g->setBalance(0);
                    p->setBalance(0);
                }
                
            }
        }
    }
}

/*
 * Recall: If key is already in the tree, you should 
 * overwrite the current value with the updated value.
 */
template<class Key, class Value>
void AVLTree<Key, Value>::insert (const std::pair<const Key, Value> &new_item)
{
    // Copy from bst but then just update balance of parent and call insert fix if b(p) was 0 before
    if(this->root_ == NULL)
    {
        AVLNode<Key, Value>* x = new AVLNode<Key, Value>(new_item.first, new_item.second, NULL);
        this->root_ = x;
    }

    else
    {
        AVLNode<Key, Value>* parent = static_cast<AVLNode<Key, Value>*>(this->root_);
        AVLNode<Key, Value>* transverse;
        int rightOrLeft = 0;
        if(this->root_->getKey() < new_item.first)
        {
            transverse = static_cast<AVLNode<Key, Value>*>(this->root_)->getRight();
            rightOrLeft = 2;
        }
        else if(this->root_->getKey() > new_item.first)
        {
            transverse = static_cast<AVLNode<Key, Value>*>(this->root_)->getLeft();
            rightOrLeft = 1;
        }
        else if (this->root_->getKey() == new_item.first)
        {
            this->root_->setValue(new_item.second);
            transverse = NULL;
        }
        while(transverse != NULL)
        {
            if(transverse->getKey() < new_item.first)
            {
                parent = transverse;
                transverse = transverse->getRight();
                rightOrLeft = 2;
            }
            else if(transverse->getKey() > new_item.first)
            {
                parent = transverse;
                transverse = transverse->getLeft();
                rightOrLeft = 1;
            }
            else if(transverse->getKey() == new_item.first)
            {
                transverse->setValue(new_item.second);
                rightOrLeft = 0;
                break;
            }
        }
        if(rightOrLeft == 1)
        {
            AVLNode<Key, Value>* x = new AVLNode<Key, Value>(new_item.first, new_item.second, parent);
            parent->setLeft(x);
            parent->updateBalance(-1);
            if(parent->getBalance() != 0)
            {
                this->insertFix(parent, x);
            }
        }
        else if(rightOrLeft == 2)
        {
            AVLNode<Key, Value>* x = new AVLNode<Key, Value>(new_item.first, new_item.second, parent);
            parent->setRight(x);
            parent->updateBalance(1);
            if(parent->getBalance() != 0)
            {
                this->insertFix(parent, x);
            }
        }
    }
}

template<class Key, class Value>
void AVLTree<Key, Value>::removeFix(AVLNode<Key,Value>* n, signed char diff)
{
    if( n == NULL)
    {
        // DO NOTHING
    }
    else
    {
        signed char nextDiff;
        AVLNode<Key,Value>* p = n->getParent();
        if( p != NULL)
        {
            if(isRightChild(n, p))
            {
                nextDiff = -1;
            }
            else
            {
                nextDiff = 1;
            }
        }
        signed char calculate = n->getBalance() + diff;
        if(calculate == -2)
        {
            AVLNode<Key,Value>* c = n->getLeft();
            if(c->getBalance() == -1)
            {
                this->rotateRight(n);
                c->setBalance(0);
                n->setBalance(0);
                this->removeFix(p, nextDiff);
            }
            else if(c->getBalance() == 0)
            {
                this->rotateRight(n);
                n->setBalance(-1);
                c->setBalance(1);
            }
            else if(c->getBalance() == 1)
            {
                AVLNode<Key,Value>* gC = c->getRight();
                this->rotateLeft(c);
                this->rotateRight(n);
                if(gC->getBalance() == 1)
                {
                    n->setBalance(0);
                    c->setBalance(-1);
                    gC->setBalance(0);
                }
                else if(gC->getBalance() == 0)
                {
                    n->setBalance(0);
                    c->setBalance(0);
                    gC->setBalance(0);
                }
                else if(gC->getBalance() == -1)
                {
                    n->setBalance(1);
                    c->setBalance(0);
                    gC->setBalance(0);
                }
                this->removeFix(p, nextDiff);
            }
        }
        //
        else if(calculate == 2)
        {
            AVLNode<Key,Value>* c = n->getRight();
            if(c->getBalance() == 1)
            {
                this->rotateLeft(n);
                c->setBalance(0);
                n->setBalance(0);
                this->removeFix(p, nextDiff);
            }
            else if(c->getBalance() == 0)
            {
                this->rotateLeft(n);
                n->setBalance(1);
                c->setBalance(-1);
            }
            else if(c->getBalance() == -1)
            {
                AVLNode<Key,Value>* gC = c->getLeft();
                this->rotateRight(c);
                this->rotateLeft(n);
                if(gC->getBalance() == -1)
                {
                    n->setBalance(0);
                    c->setBalance(1);
                    gC->setBalance(0);
                }
                else if(gC->getBalance() == 0)
                {
                    n->setBalance(0);
                    c->setBalance(0);
                    gC->setBalance(0);
                }
                else if(gC->getBalance() == 1)
                {
                    n->setBalance(-1);
                    c->setBalance(0);
                    gC->setBalance(0);
                }
                this->removeFix(p, nextDiff);
            }
        }
        //
        else if(calculate == -1 || calculate == 1)
        {
            n->setBalance(diff);
        }
        else if(calculate == 0)
        {
            n->setBalance(0);
            this->removeFix(p, nextDiff);
        }
    }
}
/*
 * Recall: The writeup specifies that if a node has 2 children you
 * should swap with the predecessor and then remove.
 */
template<class Key, class Value>
void AVLTree<Key, Value>::remove(const Key& key)
{
    // TODO
    AVLNode<Key, Value>* x = this->internalFind(key);
    if(x == NULL)
    {
        // Do nothing
    }
    else
    {
        signed char diff;
        if(x->getRight() != NULL && x->getLeft() != NULL)
        {
            AVLNode<Key, Value>* y = this->predecessor(x);
            this->nodeSwap(x, y);
        }
        // So now x either has 0ne or 0 children
        AVLNode<Key, Value>* parent = x->getParent();
        if(x->getRight() == NULL && x->getLeft() == NULL)
        {
            if(this->root_ == x)
            {
                this->root_ = NULL;
            }
            else
                {
                if(parent->getRight() == x)
                {
                    parent->setRight(NULL);
                    diff = -1;
                }
                else
                {
                    parent->setLeft(NULL);
                    diff = 1;
                }
            }
        }
        else if(x->getRight() != NULL && x->getLeft() == NULL)
        {
            AVLNode<Key, Value>* rChild = x->getRight();
            rChild->setParent(parent);
            if(parent != NULL)
            {
                if(parent->getRight() == x)
                {
                    parent->setRight(rChild);
                    diff = -1;

                }
                else
                {
                    parent->setLeft(rChild);
                    diff = 1;
                }
            }
            else
            {
                this->root_ = rChild;
            }
        }
        else if(x->getLeft() != NULL && x->getRight() == NULL)
        {
            AVLNode<Key, Value>* lChild = x->getLeft();
            //this->nodeSwap(x, lChild);
            lChild->setParent(parent);
            if(parent != NULL)
            {
                if(parent->getRight() == x)
                {
                    parent->setRight(lChild);
                    diff = -1;
                }
                else
                {
                    parent->setLeft(lChild);
                    diff = 1;
                }
            }
            else
            {
                this->root_ = lChild;
            }
        }
        delete x;
        this->removeFix(parent, diff);
    }
}

template<class Key, class Value>
void AVLTree<Key, Value>::nodeSwap( AVLNode<Key,Value>* n1, AVLNode<Key,Value>* n2)
{
    BinarySearchTree<Key, Value>::nodeSwap(n1, n2);
    signed char tempB = n1->getBalance();
    n1->setBalance(n2->getBalance());
    n2->setBalance(tempB);
}

template<class Key, class Value>
AVLNode<Key,Value>* AVLTree<Key, Value>::predecessor(AVLNode<Key,Value>* current)
{
    if(current->getLeft() != NULL)
    {
        AVLNode<Key, Value>* succ = current->getLeft();
        while(succ->getRight() != NULL)
        {
            succ = succ->getRight();
        }
        return succ;
    }
    //else we have to transverse up until when we finally go right to a parent
    // (Until we are the left child of a parent)
    else if(current->getParent() != NULL)
    {
        AVLNode<Key, Value>* child = current;
        AVLNode<Key, Value>* par = current->getParent();
        while(par != NULL)
        {
            if(par->getRight() == child)
            {
                break;
            }
            else
            {
                child = par;
                par = par->getParent();
            }
        }
        return par;
    }
    else
    {
        return NULL;
    }
}

template<class Key, class Value>
AVLNode<Key, Value>* AVLTree<Key, Value>::internalFind(const Key& k) const
{
    if(this->root_ == NULL)
    {
        return NULL;
    }
    else
    {
        AVLNode<Key, Value>* parent = static_cast<AVLNode<Key,Value>*>(this->root_);
        AVLNode<Key, Value>* transverse;
        if(this->root_->getKey() > k)
        {
            transverse = static_cast<AVLNode<Key,Value>*>(this->root_->getLeft());
        }
        else if(this->root_->getKey() < k)
        {
            transverse = static_cast<AVLNode<Key,Value>*>(this->root_->getRight());
        }
        else if (this->root_->getKey() == k)
        {
            return static_cast<AVLNode<Key,Value>*>(this->root_);
        }

        while(transverse != NULL)
        {
            if(transverse->getKey() > k)
            {
                parent = transverse;
                transverse = transverse->getLeft();
            }
            else if(transverse->getKey() < k)
            {
                parent = transverse;
                transverse = transverse->getRight();
                
            }
            else if(transverse->getKey() == k)
            {
                return transverse;
            }
        }
        return NULL;
    }
}
#endif

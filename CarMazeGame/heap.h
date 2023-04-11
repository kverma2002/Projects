#ifndef HEAP_H
#define HEAP_H
#include <functional>
#include <stdexcept>
#include <vector>

template <typename T, typename PComparator = std::less<T> >
class Heap
{
public:
  /**
   * @brief Construct a new Heap object
   * 
   * @param m ary-ness of heap tree (default to 2)
   * @param c binary predicate function/functor that takes two items
   *          as an argument and returns a bool if the first argument has
   *          priority over the second.
   */
  Heap(int m=2, PComparator c = PComparator());

  /**
  * @brief Destroy the Heap object
  * 
  */
  ~Heap();

  /**
   * @brief Push an item to the heap
   * 
   * @param item item to heap
   */
  void push(const T& item);

  /**
   * @brief Returns the top (priority) item
   * 
   * @return T const& top priority item
   * @throw std::underflow_error if the heap is empty
   */
  T const & top() const;

  /**
   * @brief Remove the top priority item
   * 
   * @throw std::underflow_error if the heap is empty
   */
  void pop();

  /// returns true if the heap is empty

  /**
   * @brief Returns true if the heap is empty
   * 
   */
  bool empty() const;

private:
  /// Add whatever helper functions and data members you need below
  int treeLeaves;
  PComparator comp;
  std::vector<T> items_;
  void trickleDown(int location);
  void trickleUp();
};

// Add implementation of member functions here
template <typename T, typename PComparator>
Heap<T,PComparator>::Heap(int m, PComparator c)
{
  treeLeaves = m;
  comp = c;
}

template <typename T, typename PComparator>
Heap<T,PComparator>::~Heap()
{
  
}




// We will start top() for you to handle the case of 
// calling top on an empty heap
template <typename T, typename PComparator>
T const & Heap<T,PComparator>::top() const
{
  // Here we use exceptions to handle the case of trying
  // to access the top element of an empty heap
  if(empty()){
    // ================================
    // throw the appropriate exception
    // ================================
    throw std::underflow_error("Heap Empty AF");
  }
  // If we get here we know the heap has at least 1 item
  // Add code to return the top element
  return items_.at(0);
}

template <typename T, typename PComparator>
bool Heap<T,PComparator>::empty() const
{
  // Here we use exceptions to handle the case of trying
  // to access the top element of an empty heap
  return items_.empty();
  
}


// We will start pop() for you to handle the case of 
// calling top on an empty heap
template <typename T, typename PComparator>
void Heap<T,PComparator>::pop()
{
  if(empty()){
    // ================================
    // throw the appropriate exception
    // ================================
    throw std::underflow_error("Heap Empty AF");
  }
  T temp = items_.at(0);
  items_.at(0) = items_.back();
  items_.at(items_.size() - 1) = temp;
  items_.pop_back();
  trickleDown(0);
}

template <typename T, typename PComparator>
void Heap<T,PComparator>::push(const T& item)
{
  items_.push_back(item);
  trickleUp();
}


template <typename T, typename PComparator>
void Heap<T,PComparator>::trickleDown(int location)
{
  if((treeLeaves*location)+1 >= items_.size())
    {
        //it is a leaf node. Its done trickling down
    }
    else
    {
        int largeChild = (treeLeaves*location)+1;
        for(int i = 2; i <= treeLeaves; i++)
        {
          if((treeLeaves*location) + i < items_.size())
          {
              int rightChild = (treeLeaves*location) + i;
              if(!comp(items_[largeChild], items_[rightChild]))
              {
                  largeChild = rightChild;
              }
          }
        }
        if(!(comp(items_[location],items_[largeChild])))
        {
            std::swap(items_[location], items_[largeChild]);
            trickleDown(largeChild);
        }
    }
}

template <typename T, typename PComparator>
void Heap<T,PComparator>::trickleUp()
{
  int location = items_.size() - 1;
  while (location != 0) {
      int parent_index = (location-1)/treeLeaves;
      T& current = items_[location];
      T& parent = items_[parent_index];
      if (comp(parent, current)) 
      {

        break;
      }
      std::swap(current, parent);
      location = parent_index;
  }
}



#endif


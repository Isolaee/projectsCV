// LinedListItem.cpp

#include <iostream>
#include <climits>

using namespace std;
typedef char Item;

// Fast hack for empty lists
#define INFONIL '\x1';

class LinkedListNullptr {
    private:
        struct node {
            Item item;  // data item
            node *next; // pointer to next item
        
            node(Item x, node *t) {
                item = x;
                next = t;
            }
        };
        
        typedef node *Link;
        Link head;

    public:
        LinkedListNullptr() {   // constructor
            head = nullptr; // empty list
        }

        ~LinkedListNullptr() {  // class name with "~" is deconstructor
            while(!isEmpty()) {
                remove();
            }
        }

        void insert(Item item) {
            head = new node(item, head);
        }
        Item remove() {
            if (!isEmpty()) {
                Link t = head;
                Item value = t->item;
                head = head->next;
                delete t;
                return value;
            }
            return INFONIL;
        }
        int isEmpty() {
            return (head == nullptr);
        }
        void traverse(void (*pf)(Item item)){
            Link t = head;
            while (t != nullptr) {
                (*pf)(t->item);
                t = t-> next;
            }
        }
};

void printItem(Item item) {
    cout << "Traverse: " << item << endl;
}

int main(int argc, char *argv[]) {
    int i;
    const string testString = "LOOCSIGNIDOC";
    LinkedListNullptr *list = new LinkedListNullptr();

    for (i=0; i < testString.length(); i++){
        list-> insert(testString.at(i));
    }
    cout << "Is list empty: " << (list -> isEmpty() ? "True" : "False") << endl;

    // cout << "Traverse" << endl;
    // list ->traverse(printItem);
    
    while(!list ->isEmpty()) {
        Item value = list -> remove();
        cout << "Removed " << value << endl;
    }
    cout << "Is list empty: " << (list -> isEmpty() ? "True" : "False") << endl;
    delete list;
    return 0;
}
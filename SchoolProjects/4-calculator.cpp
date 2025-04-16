// 4-calculator using reverse polish notation

#include <iostream>
#include <cassert>
#include <regex>

using namespace std;

typedef float Item;

#define MAX_SIZE 1024

class StackImpl {
    private:
        int sp;
        int size;
        Item *_data;


    public:
        StackImpl(int size = MAX_SIZE) {
            size = size;
            sp = -1;
            _data = new Item[size];
        }
        ~StackImpl() {
            delete []_data;
        }

        void push(Item x) {
            // assert(sp<(size-1));
            _data[++sp] = x;
        }
        Item pop() {
            // assert(sp>=0);
            return _data[sp--];
        }
};

regex rgx_float = regex("-?[0-9]+([\\.][0-9]+)?");
regex rgx_op = regex("(\\+|-|\\*|/|=|d)");

int calculate(StackImpl& stack, string s) {
    Item    f, argl, argr;
    char op;

    // Match numbers and convert to float
    if(regex_match(s, rgx_float)) {
        // s is float
        f = std::stod(s);
        stack.push(f);
    }
    // Match Operation and perform operation
    else if(regex_match(s, rgx_op)) {
        op = s.at(0);
        switch (op) {
            // + = a + b
            case '+':
                f = stack.pop() + stack.pop();
                stack.push(f);
                break;
            // - = a - b
            case '-':
                f = stack.pop() - stack.pop();
                stack.push(f);
                break;
            // * = a * b
            case '*':
                f = stack.pop() * stack.pop();
                stack.push(f);
                break;
            // / = a / b
            case '/':
                f = stack.pop() / stack.pop();
                stack.push(f);
                break;
            // Print what is on top of stack
            case '=':
                f = stack.pop();
                cout << "= " << f << endl;
                break;
            // d = break the loop
            case 'd':
                break;
            // Default print for swich case default
            default:
                cout << "Default" << endl;
        }
    }
    // If input not regonized print unkown
    else {
        cout << "Unknown command" << endl;
        return 0;
    }

    return 0;
}


int main(int argc, char *argv[]) {
    StackImpl stack;
    int done = 0;
    string s;

    // Loop while
    while(!done) {
        cout << " Give input (One per line): ";
        getline(cin, s);

        if(s.length() == 0)
            break;

        calculate(stack, s);
    }
    return 0;
}

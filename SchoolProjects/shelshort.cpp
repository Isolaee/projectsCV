# include <iostream>
# include <stdlib.h>

using namespace std;



static int compareCount = 0;
static int swapCount = 0;

template <class Item>
void itemSwap(Item &a, Item &b) {
    Item t = a; a = b; b = t;
    swapCount++;
}

template <class Item>
void dbgOutput(Item a, int N) {
    for(int i = 0; i < N; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

template <class Item>
void compareAndSwap(Item &a, Item &b) {
    compareCount++;
    if(b < a)   itemSwap(a,b);
}

template <class Item>
void shellSort(Item a[], int l, int r) {
    int h;
    // h seq in [1, 4, 13, 40, 121, 364, 1093, 3280, 9841..]
    for(h = 1; h <= (r-l)/9; h=3*h+1) ;

    
    for( ; h > 0; h /= 3) {
        cout << h << " (s:" << swapCount << " c:" << compareCount << ")" << endl;
        for(int i = l+h; i <= r; i++) {
            int j = i;
            Item v = a[i];
            while(j >= l+h && v < a[j-h]) {
                compareCount += 2;  // not counting the exit condition
                a[j] = a[j-h];
                j -= h;
            }
            a[j] = v;
            swapCount++;
            dbgOutput(a, r+1); // should be r+1
        }
    }
}

# define TEST_INPUT "ASRERFFKOLKVPIJRNSD"

int main(int argc, char argv[]) {
    int i;
    int N = strlen(TEST_INPUT);
    char *a = new char[N+1];
    strcpy(a, TEST_INPUT);
    dbgOutput(a, N);
    shellSort(a, 0, N-1);

    cout << "Total swaps " << swapCount << " compares " << compareCount << endl;

    return 0;
}
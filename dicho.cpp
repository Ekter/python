//dichotomy over a sorted and rotated array of integers


#include <iostream>

using namespace std;

int dichotomy(int *tab, int n, int x)
{
    int left = 0;
    int right = n-1;
    int middle = (left+right)/2;
    while (left <= right)
    {
        if (tab[middle] == x)
            return middle;
        if (tab[left] < x || x < tab[middle])
            left = middle+1;
        else
            right = middle-1;
        middle = (left+right)/2;
    }
    return -1;
}

//test
int main()
{
    int tab[10] = {4,5,6,7,8,9,10,1,2,3};
    cout << dichotomy(tab, 9, 10) << endl;
    int tab2[10] = {1,2,3,4,5,6,7,8,9,10};
    cout << dichotomy(tab2, 10, 10) << endl;
    int tab3[9] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
    cout << dichotomy(tab3, 9, 10) << endl;
    int tab4[4] = {3, 5, 1, 2};
    cout << dichotomy(tab4, 4, 10) << endl;
    return 0;
}


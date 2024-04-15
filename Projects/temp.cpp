#include <iostream>
using std::cin;
using std::cout;
using std::endl;

void fizzBuzz(int n) {
    std::string mOfThree = "Fizz";
    std::string mOfFive = "Buzz";
    std::string out = "";
    for (int i = 1; i <= n; i++) {
        if ((i%3 == 0) && (i%5 == 0)) out = mOfThree + mOfFive;
        else if ((i%3 == 0) && (i%5 != 0)) out = mOfThree;
        else if ((i%5 == 0) && (i%3 != 0)) out = mOfFive;
        else out = std::to_string(i);

        cout<<out<<endl;
    }
}

int main()
{
/*    int M,N,sum=0;
    cout<<"Enter the dimensions of the matrix: "<<endl;
    cin>>M>>N;
    int arr[M][N];
    for(int i=0;i<M;i++) //outer loop
    {
        for(int j=0;j<N;j++) //inner loop
        {
            cout<<"Enter the element in position "<<i<<","<<j<<": "<<endl;
            cin>>arr[i][j];
            sum+=arr[i][j];
        }
    }
    cout<<"The sum of the elements is "<<sum<<endl;
*/

    fizzBuzz(15);
    return 0;
}


#include <iostream>
#include <fstream>
using namespace std;

int main(){
   ofstream writer;
   writer.open("output.txt");
   writer << "5,6\n";
   writer << "2,3\n";
   writer << "3,6\n";
   writer << "6,7\n";
   writer.close();
   return 0;
}

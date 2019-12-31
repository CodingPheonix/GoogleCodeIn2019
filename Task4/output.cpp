#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int main(){
   ofstream writer;
   writer.open("output.txt");
   for (int i = 0; i<100; i++)
   {
      writer << to_string(i) << "," <<  to_string((int) pow(i,2)) << "\n";
   }   
   writer.close();
   return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <iostream>

float odd(float i)
{
  return 2 * i + 1;
}

float square(float i)
{
  return i * i;
}

int main(int argc, char* argv[])
{
  using namespace std;

  float var = atof(argv[1]);

  cout << odd(var) <<endl;
  cout << square(var) << endl;
}

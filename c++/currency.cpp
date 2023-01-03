#include <iostream>

int main()
{

  double p;
  double r;
  double s;

  double dollars;

  std::cout << "Enter number of Colombian Pesos: ";
  std::cin >> p;

  std::cout << "Enter number of Guatemalan Quetzals: ";
  std::cin >> r;

  std::cout << "Enter number of Salvadoran Colons: ";
  std::cin >> s;

  dollars = 0.049 * p + 0.1305 * r + 0.1144 * s;

  std::cout << "Total USD = $" << dollars << "\n";

}

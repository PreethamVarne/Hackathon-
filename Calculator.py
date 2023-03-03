#include <math.h>
#include <stdio.h>
int convert(long long);
int main() 
{
  char op;
  double first, second;
  long long n;
  printf("Enter an operator (+, -, *, /): ");
  scanf("%c", &op);
  printf("Enter two operands: ");
  scanf("%lf %lf", &first, &second);

  switch (op) {
    case '+':
      printf("%.1lf + %.1lf = %.1lf", first, second, first + second);
        printf("%lld in binary = %d in decimal", n, convert(n));

      break;
    case '-':
      printf("%.1lf - %.1lf = %.1lf", first, second, first - second);
        printf("%lld in binary = %d in decimal", n, convert(n));

      break;
    case '*':
      printf("%.1lf * %.1lf = %.1lf", first, second, first * second);
        printf("%lld in binary = %d in decimal", n, convert(n));

      break;
    case '/':
      printf("%.1lf / %.1lf = %.1lf", first, second, first / second);
        printf("%lld in binary = %d in decimal", n, convert(n));

      break;
    // operator doesn't match any case constant
    default:
      printf("Error! operator is not correct");
  }

  return 0;
}
int convert(long long n)
{
  int dec = 0, i = 0, rem;

  while (n!=0) {
    rem = n % 10;
    n /= 10;
    dec += rem * pow(2, i);
    ++i;
  }

  return dec;
}
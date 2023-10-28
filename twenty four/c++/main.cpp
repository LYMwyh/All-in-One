#include <random>
#include <iostream>
using namespace std;
struct Friction{
    int numerator;
    int denominator;
}Four_Numbers[4];
char Operators[] = {'+', '-', '*', '/'};
char Selected_Operators[3];
void calculate_the_whole_answers()
{
    for(int first_element=0;first_element<=3;first_element++)
    {
        swap(Four_Numbers[first_element], Four_Numbers[0]);
        for(int second_element=1;second_element<=3;second_element++)
        {
            swap(Four_Numbers[second_element], Four_Numbers[1]);
            for(int third_element=2;third_element<=3;third_element++)
            {
                swap(Four_Numbers[third_element], Four_Numbers[2]);
                for(int first_operator=0;first_operator<=3;first_operator++)
                {
                    Selected_Operators[0] = Operators[first_operator];
                    for(int second_operator=0;second_operator<=3;second_operator++)
                    {
                        Selected_Operators[1] = Operators[second_operator];
                        for(int third_operator=0;third_operator<=3;third_operator++)
                        {
                            Selected_Operators[2] = Operators[third_operator];
                            for(int Type_of_Brackets=0;Type_of_Brackets<=6;Type_of_Brackets++)
                            {

                            }
                        }
                    }
                }
                swap(Four_Numbers[2], Four_Numbers[third_element]);
            }
            swap(Four_Numbers[1], Four_Numbers[second_element]);
        }
        swap(Four_Numbers[0], Four_Numbers[first_element]);
    }
}

int main() {
    // 创建一个随机设备
    random_device rd;

    // 使用随机设备来种子一个Mersenne twister引擎
    // engine是mt19937类型的对象，rd()每一次都会返回一个不确定的种子
    mt19937 engine(rd());

    // 创建一个均匀分布
    // uniform_int_distribution<int> 是一个类型， dist是变量， uniform_int_distribution是一个模板类
    // 变量的两个参数分别是边界，属于一个闭区间[a, b]
    uniform_int_distribution<int> dist(1, 6);
    while(true)
    {
        for(auto element: Four_Numbers)
        {
            element.numerator = dist(engine);
            element.denominator = 1;
        }
        printf("%d, %d, %d, %d", Four_Numbers[0].numerator, Four_Numbers[1].numerator, Four_Numbers[2].numerator, Four_Numbers[3].numerator);
        calculate_the_whole_answers();
        break;
    }

    return 0;
}

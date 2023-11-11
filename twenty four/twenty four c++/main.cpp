#include <iostream>
#include <random>
#include <chrono>
#include <vector>
using namespace std;

struct Fraction{
    int numerator=1;
    int denominator=1;
};
Fraction Four_Numbers[4];
string Operators[] = {"+", "-", "*", "/"};
string the_Select_Operators[3];
vector<string> answer;
string complete_answer;

auto return_fraction(string fraction_in_str)
{
    size_t position = fraction_in_str.find('/');
    if(position == variant_npos)    return make_pair(-1, -1);
    else    return make_pair(stoi(fraction_in_str.substr(0, position)) , stoi(fraction_in_str.substr(position + 1)));
}


auto before_or_after_one(int index_of_one, int before, vector<string> answer)
{
    if(before)
    {
        if(answer[index_of_one + 1] == "/") return false;
        else if(answer[index_of_one + 1] == "+" or answer[index_of_one + 1] == "-") return true;
        before = -1;
    }
    else
    {
        if(answer[index_of_one - 1] == "+" or answer[index_of_one - 1] == "-")  return true;
        before = 1;
    }
    while(true)
    {
        index_of_one += before;
        if(index_of_one < 0 or index_of_one >= answer.size())   return true;
        if(answer[index_of_one] == "(" or answer[index_of_one] == ")")  return true;
        else if(answer[index_of_one] == "/" and before == -1)   return false;
        else if(answer[index_of_one] == "+" or answer[index_of_one] == "-") return true;
        pair<int, int> temporary_variable = return_fraction(answer[index_of_one]);
        if(temporary_variable.first != -1 and temporary_variable.first != temporary_variable.second)    return false;
    }
}


auto calculate_answer(vector<string> answer)
{
    int step = 0;
    int layer = 0;
    vector<bool> whether_use_addition_and_subtraction;
    vector<bool> whether_use_multiplication_and_division;
    vector<bool> whether_found_multiplication_or_division;
    whether_use_addition_and_subtraction.push_back(false);
    whether_use_addition_and_subtraction.push_back(true);
    whether_found_multiplication_or_division.push_back(false);
    while(answer.size() != 1)
    {
        if(step == answer.size())
        {
            step = 0;
            for(auto & element : whether_use_addition_and_subtraction)
            {

            }
        }
    }
}


auto calculate_whole_answers()
{
    for(int first_number_ordinal = 0;first_number_ordinal < 4; first_number_ordinal ++)
    {
        swap(Four_Numbers[first_number_ordinal], Four_Numbers[0]);
        for(int second_number_ordinal = 1; second_number_ordinal < 4; second_number_ordinal ++)
        {
            swap(Four_Numbers[second_number_ordinal], Four_Numbers[1]);
            for(int third_number_ordinal = 2; third_number_ordinal < 4; third_number_ordinal ++)
            {
                swap(Four_Numbers[third_number_ordinal], Four_Numbers[2]);
                for(const auto & first_operator : Operators)
                {
                    the_Select_Operators[0] = first_operator;
                    for(const auto & second_operator : Operators)
                    {
                        the_Select_Operators[1] = second_operator;
                        for(const auto & third_operator : Operators)
                        {
                            the_Select_Operators[2] = third_operator;
                            for(int bracket_type_ordinal = 0; bracket_type_ordinal < 7; bracket_type_ordinal ++)
                            {
                                answer.clear();
                                complete_answer = "";
                                for(int answer_index = 0; answer_index < 4; answer_index ++)
                                {
                                    // 0. (a b) c d
                                    // 1. a (b c) d
                                    // 2. a b (c d)
                                    // 3. (a b c) d
                                    // 4. a (b c d)
                                    // 5. (a b)(c d)
                                    // 6. a b c d
                                    switch (answer_index){
                                        case 0:
                                            switch (bracket_type_ordinal) {
                                                case 0: case 3: case 5:
                                                    answer.emplace_back("(");
                                                    complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        case 1:
                                            switch (bracket_type_ordinal) {
                                                case 1: case 4:
                                                    answer.emplace_back("(");
                                                    complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        case 2:
                                            switch (bracket_type_ordinal) {
                                                case 2: case 5:
                                                    answer.emplace_back("(");
                                                    complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        default: ;
                                    }
                                    answer.emplace_back(to_string(Four_Numbers[answer_index].numerator) + "/" + to_string(Four_Numbers[answer_index].denominator));
                                    complete_answer += to_string(Four_Numbers[answer_index].numerator);
                                    switch (answer_index) {
                                        case 1:
                                            switch (bracket_type_ordinal) {
                                                case 0: case 5:
                                                    answer.emplace_back(")");
                                                    complete_answer += ")";
                                                default: ;
                                            }
                                            break;
                                        case 2:
                                            switch (bracket_type_ordinal) {
                                                case 1: case 3:
                                                    answer.emplace_back(")");
                                                    complete_answer += ")";
                                                default: ;
                                            }
                                            break;
                                        case 3:
                                            switch (bracket_type_ordinal) {
                                                case 2: case 4: case 5:
                                                    answer.emplace_back(")");
                                                    complete_answer += ")";
                                                default: ;
                                            }
                                            break;
                                        default: ;
                                    }
                                    if(answer_index < 3) {
                                        answer.emplace_back(the_Select_Operators[answer_index]);
                                        complete_answer += the_Select_Operators[answer_index];
                                    }

                                }
                                calculate_answer(answer);

                            }
                        }
                    }
                }
                swap(Four_Numbers[third_number_ordinal], Four_Numbers[2]);
            }
            swap(Four_Numbers[second_number_ordinal], Four_Numbers[1]);
        }
        swap(Four_Numbers[first_number_ordinal], Four_Numbers[0]);
    }
}

int main() {
    // 使用当前系统时间作为种子值
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();

    // 使用种子值初始化随机数生成器
    default_random_engine generator(seed);

    // 生成随机数
    uniform_int_distribution<int> distribution(1,13);
    while(true)
    {
        for(auto & Number : Four_Numbers) {
            Number.numerator = distribution(generator);
            // printf("%d", Number.numerator);
        }
        string whether_play;
        printf("Do you want to play the game?(YES/NO)");
        cin >> whether_play;
        if(whether_play == "YES")   calculate_whole_answers();
        else break;
    }
    return 0;
}

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
vector<string> Whole_answers;
vector<string> answer;
string complete_answer;


auto str_to_fraction(string fraction_in_str)
{
    size_t position = fraction_in_str.find('/');
    Fraction ans;
    if(position == variant_npos)    ans.numerator = -1, ans.denominator = -1;
    else    ans.numerator = stoi(fraction_in_str.substr(0, position)) , ans.denominator = stoi(fraction_in_str.substr(position + 1));
    return ans;
}


auto fraction_to_str(Fraction fraction)
{
    return to_string(fraction.numerator) + '/' + to_string(fraction.denominator);
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
        Fraction temporary_variable = str_to_fraction(answer[index_of_one]);
        if(temporary_variable.numerator != -1 and temporary_variable.numerator != temporary_variable.denominator)    return false;
    }
}


auto simplify_formula_first_part(vector<string> answer)
{
    int layer = 0;
    int step = 0;
    static vector<bool> whether_found_addition_or_subtraction;
    static vector<bool> whether_found_multiplication_or_division;
    whether_found_addition_or_subtraction.clear();
    whether_found_multiplication_or_division.clear();
    whether_found_multiplication_or_division.push_back(false);
    whether_found_addition_or_subtraction.push_back(false);
    static bool decision_front;
    static bool decision_back;
    static bool change_symbol_from_subtraction;
    static bool change_symbol_from_division;
    static vector<int> brackets;
    brackets.clear();
    static string symbol;
    bool whether_change = false;
    static Fraction temporary_fraction;
    while(true)
    {
        if(step == answer.size())
        {
            if(! whether_change)
                break;
            else
            {
                step = 0;
                whether_change = false;
            }
        }
        symbol = complete_answer[step];
        if(symbol == "(")
        {
            layer += 1;
            if(whether_found_multiplication_or_division.size() == layer)
            {
                whether_found_multiplication_or_division.push_back(false);
                whether_found_addition_or_subtraction.push_back(false);
            }
            else
            {
                whether_found_multiplication_or_division[layer] = false;
                whether_found_addition_or_subtraction[layer] = false;
            }
            brackets.push_back(step);
        }
        if(symbol == ")")
        {
            decision_front = false;
            decision_back = false;
            change_symbol_from_subtraction = false;
            change_symbol_from_division = false;
            if(whether_found_multiplication_or_division[layer] and ! whether_found_addition_or_subtraction[layer])
            {
                decision_front = true;
                decision_back = true;
                if(brackets[layer - 1] != 0 and answer[brackets[layer - 1] - 1] == "/")
                    change_symbol_from_division = true;
            }
            else if(brackets[layer - 1] != 0 and answer[brackets[layer - 1] - 1] == "/")    ;
            else
            {
                if(brackets[layer - 1] != 0)
                {
                    temporary_fraction = str_to_fraction(answer[brackets[layer - 1] - 2]);
                    if((answer[brackets[layer - 1] - 1] != "*" and answer[brackets[layer - 1] - 1] != "/") or (temporary_fraction.numerator == temporary_fraction.denominator and
                            before_or_after_one(brackets[layer - 1] - 2, true, answer)))
                    {
                        decision_front = true;
                        if(answer[brackets[layer - 1] - 1] == "-")
                            change_symbol_from_subtraction = true;
                    }
                }
                else    decision_front = true;
                if(step != answer.size() - 1)
                {
                    temporary_fraction = str_to_fraction(answer[step + 2]);
                    if(answer[step + 1] != "*" and answer[step + 1] != "/")
                        decision_back = true;
                    else if(temporary_fraction.numerator == temporary_fraction.denominator and before_or_after_one(step + 2,
                                                                                                                   false, answer))
                    {
                        answer[step + 1] == "*";
                        decision_back = true;
                    }
                }
                else    decision_back = true;
            }
            // 11j23i12345678901234567890
        }
    }

}


auto calculate_answer(vector<string> answer)
{
    static vector<bool> whether_use_addition_and_subtraction;
    static vector<bool> whether_use_multiplication_and_division;
    static vector<bool> whether_found_multiplication_or_division;
    whether_use_addition_and_subtraction.clear();
    whether_use_multiplication_and_division.clear();
    whether_found_multiplication_or_division.clear();
    static string symbol;
    static Fraction temporary_fraction_front;
    static Fraction temporary_fraction_back;
    int step = 0;
    int layer = 0;
    whether_use_addition_and_subtraction.clear();
    whether_use_multiplication_and_division.clear();
    whether_found_multiplication_or_division.clear();
    whether_use_addition_and_subtraction.push_back(false);
    whether_use_multiplication_and_division.push_back(true);
    whether_found_multiplication_or_division.push_back(false);

    while(answer.size() != 1)
    {
        if(step == answer.size())
        {
            step = 0;
            for(size_t index = 0; index < whether_use_addition_and_subtraction.size(); index ++)
            {
                whether_use_addition_and_subtraction[index] = ! whether_found_multiplication_or_division[index];
                whether_use_multiplication_and_division[index] = true;
                whether_found_multiplication_or_division[index] = false;
            }
        }
        symbol = answer[step];
        if(symbol == "(")
        {
            if(whether_found_multiplication_or_division.size() - 1 == layer)
            {
                whether_found_multiplication_or_division.push_back(false);
                whether_use_multiplication_and_division.push_back(true);
                whether_use_addition_and_subtraction.push_back(false);
            }
            layer += 1;
            step += 1;
            continue;
        }
        if(symbol == ")")
        {
            layer -= 1;
            if(answer[step - 2] == "(")
            {
                answer.erase(answer.begin() + step - 2);
                answer.erase(answer.begin() + step - 1);
                step -= 1;
            }
            else    step += 1;
            continue;
        }
        if(whether_use_addition_and_subtraction[layer])
        {
            if(symbol == "+")
            {
                if(answer[step - 1] == "(" or answer[step - 1] == ")" or answer[step + 1] == "(" or answer[step + 1] == ")")    ;
                else
                {
                    temporary_fraction_front = str_to_fraction(answer[step - 1]);
                    temporary_fraction_back = str_to_fraction(answer[step + 1]);
                    if(answer[step - 2] != "-")
                    {
                        temporary_fraction_front.numerator *= temporary_fraction_back.denominator;
                        temporary_fraction_back.numerator *= temporary_fraction_front.denominator;
                        temporary_fraction_front.numerator += temporary_fraction_back.numerator;
                        temporary_fraction_front.denominator *= temporary_fraction_back.denominator;
                    }
                    else
                    {
                        temporary_fraction_front.numerator *= temporary_fraction_back.denominator;
                        temporary_fraction_back.numerator *= temporary_fraction_front.denominator;
                        temporary_fraction_front.numerator -= temporary_fraction_back.numerator;
                        temporary_fraction_front.denominator *= temporary_fraction_back.denominator;
                    }
                    answer[step - 1] = fraction_to_str(temporary_fraction_front);
                    answer[step + 1] = fraction_to_str(temporary_fraction_back);
                    answer.erase(answer.begin() + step, answer.begin() + step + 2);
                    continue;
                }
            }
            else if(symbol == "-")
            {
                if(answer[step - 1] == "(" or answer[step - 1] == ")" or answer[step + 1] == "(" or answer[step + 1] == ")")    ;
                else
                {
                    temporary_fraction_front = str_to_fraction(answer[step - 1]);
                    temporary_fraction_back = str_to_fraction(answer[step + 1]);
                    if(answer[step - 2] != "-")
                    {
                        temporary_fraction_front.numerator *= temporary_fraction_back.denominator;
                        temporary_fraction_back.numerator *= temporary_fraction_front.denominator;
                        temporary_fraction_front.numerator -= temporary_fraction_back.numerator;
                        temporary_fraction_front.denominator *= temporary_fraction_back.denominator;
                    }
                    else
                    {
                        temporary_fraction_front.numerator *= temporary_fraction_back.denominator;
                        temporary_fraction_back.numerator *= temporary_fraction_front.denominator;
                        temporary_fraction_front.numerator += temporary_fraction_back.numerator;
                        temporary_fraction_front.denominator *= temporary_fraction_back.denominator;
                    }
                    answer[step - 1] = fraction_to_str(temporary_fraction_front);
                    answer[step + 1] = fraction_to_str(temporary_fraction_back);
                    answer.erase(answer.begin() + step, answer.begin() + step + 2);
                    continue;
                }
            }
        }
        if(whether_use_multiplication_and_division[layer])
        {
            if(symbol == "*")
            {
                whether_found_multiplication_or_division[layer] = true;
                if(answer[step - 1] == "(" or answer[step - 1] == ")" or answer[step + 1] == "(" or answer[step + 1] == ")")
                    whether_use_multiplication_and_division[layer] = false;
                else
                {
                    temporary_fraction_front = str_to_fraction(answer[step - 1]);
                    temporary_fraction_back = str_to_fraction(answer[step + 1]);
                    temporary_fraction_front.numerator *= temporary_fraction_back.numerator;
                    temporary_fraction_front.denominator *= temporary_fraction_back.denominator;
                    answer[step - 1] = fraction_to_str(temporary_fraction_front);
                    answer[step + 1] = fraction_to_str(temporary_fraction_back);
                    answer.erase(answer.begin() + step, answer.begin() + step + 2);
                    continue;
                }
            }
            else if(symbol == "/")
            {
                whether_found_multiplication_or_division[layer] = true;
                if(answer[step - 1] == "(" or answer[step - 1] == ")" or answer[step + 1] == "(" or answer[step + 1] == ")")
                    whether_use_multiplication_and_division[layer] = false;
                else
                {
                    temporary_fraction_front = str_to_fraction(answer[step - 1]);
                    temporary_fraction_back = str_to_fraction(answer[step + 1]);
                    if(temporary_fraction_back.denominator == 0)
                    {
                        answer.clear();
                        answer.emplace_back(fraction_to_str(temporary_fraction_back));
                        break;
                    }
                    temporary_fraction_front.numerator *= temporary_fraction_back.denominator;
                    temporary_fraction_front.denominator *= temporary_fraction_back.numerator;
                    answer[step - 1] = fraction_to_str(temporary_fraction_front);
                    answer[step + 1] = fraction_to_str(temporary_fraction_back);
                    answer.erase(answer.begin() + step, answer.begin() + step + 2);
                    continue;
                }
            }
        }
        step += 1;
    }
    Fraction ans = str_to_fraction(answer[0]);
    if(ans.denominator == 0)
        return "0";
    else if(ans.numerator % ans.denominator == 0 and ans.numerator / ans.denominator == 24)
        return "24";
    else
        return "0";
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
                                string ans = calculate_answer(answer);
                                if(ans == "24")
                                {
                                    Whole_answers.emplace_back(complete_answer);
                                }
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
            printf("%d , ", Number.numerator);
        }
        printf("\n");
        string whether_play;
        printf("Do you want to play the game?(YES/NO)");
        cin >> whether_play;
        if(whether_play == "YES")
        {
            calculate_whole_answers();
            for(const auto & answer : Whole_answers)
                cout << answer << endl;
        }
        else
        {
            break;
        }
    }
    return 0;
}

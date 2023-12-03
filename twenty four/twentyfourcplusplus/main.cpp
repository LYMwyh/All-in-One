#include <iostream>
#include <random>
//#include <chrono>
#include <vector>
#include <algorithm>
#include <map>
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
int one_as_a_group = 0;


auto char_to_string(char c)
{
    static string temporary_string;
    temporary_string.clear();
    temporary_string.append(1, c);
    return temporary_string;
}


auto str_to_fraction(const string & fraction_in_str)
{
    bool change;
    Fraction ans;
    if(! fraction_in_str.length())
    {
        ans.numerator = 0;
        ans.denominator = 0;
        change = false;
        return pair<Fraction, bool> (ans, change);
    }
    size_t position = fraction_in_str.find('/');
    if(position == string::npos)
    {
        change = true;
        ans.numerator = 0;
        for(const auto & symbol : fraction_in_str)
        {
            try {
                ans.numerator = ans.numerator * 10 + stoi(char_to_string(symbol));
            }
            catch (const exception & e)
            {
                ans.numerator = 0;
                ans.denominator = 0;
                change = false;
                break;
            }
        }
    }
    else
    {
        try {
            ans.numerator = stoi(fraction_in_str.substr(0, position)), ans.denominator = stoi(
                    fraction_in_str.substr(position + 1)), change = true;
        }
        catch (const exception & e)
        {
            ans.numerator = 0, ans.denominator = 0, change = false;
        }
    }
    return pair<Fraction, bool> (ans, change);
}


auto fraction_to_str(Fraction fraction)
{
    return to_string(fraction.numerator) + '/' + to_string(fraction.denominator);
}


auto gcd(int a, int b)
{
    int temp;
    while(b != 0)
    {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}


auto split_to_str_vector(const vector<string>& original_answer)
{
    static vector<string> new_answer;
    static int num;
    new_answer.clear();
    num = 0;
    for(const auto & equation : original_answer)
    {
        // 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
        for(auto symbol : equation)
        {
            try {
                num = num * 10 + stoi(char_to_string(symbol));
            }
            catch (const exception & e)
            {
                if(num != 0)
                {
                    new_answer.emplace_back(to_string(num));
                    num = 0;
                }
                new_answer.emplace_back(char_to_string(symbol));
            }
        }
    }
    if(num != 0)    new_answer.emplace_back(to_string(num));
    return new_answer;
}


auto split_to_str_vector(const string& original_answer)
{
    static vector<string> new_answer;
    static int num;
    new_answer.clear();
    num = 0;
    for(auto symbol : original_answer)
    {
        try {
            num = num * 10 + stoi(char_to_string(symbol));
        }
        catch (const exception & e)
        {
            if(num != 0)
            {
                new_answer.emplace_back(to_string(num));
                num = 0;
            }
            new_answer.emplace_back(char_to_string(symbol));
        }
    }
    if(num != 0)    new_answer.emplace_back(to_string(num));
    return new_answer;
}


auto str_vector_to_str(vector<string> & str_vector, bool format)
{
    // format means make the numerator and denominator relatively prime.
    if(str_vector.size() == 1)  return str_vector[0];
    static string ans;
    static pair<Fraction, bool> temporary_pair;
    static Fraction temporary;
    ans = "";
    int gcd_ans;
    for(const auto & element : str_vector)
    {
        if(format)
        {
            temporary_pair = str_to_fraction(element);
            temporary = temporary_pair.first;
            if(! temporary_pair.second)
            {
                ans += element;
                continue;
            }
            gcd_ans = gcd(temporary.numerator, temporary.denominator);
            if(temporary.denominator == gcd_ans)    ans += to_string(temporary.numerator / gcd_ans);
            else    ans += to_string(temporary.numerator / gcd_ans) + '/' + to_string(temporary.denominator / gcd_ans);
        }
        else    ans += element;
    }
    return ans;
}


pair<string, int> before_or_after_one(int index_of_one, int before, vector<string> answer) {
    if(before)
    {
        if(answer[index_of_one + 1] == "/") return {"", -1};
        else if(answer[index_of_one + 1] == "+")    return {"", answer.size()};
        else if(answer[index_of_one + 1] == "-")    return {"-", answer.size()};
        before = -1;
    }
    else
    {
        if(answer[index_of_one - 1] == "+" or answer[index_of_one - 1] == "-")  return {"", answer.size()};
        before = 1;
    }
    pair<Fraction, bool> temporary_pair;
    Fraction temporary_variable;
    while(true)
    {
        index_of_one += before;
        if(index_of_one < 0 or index_of_one >= answer.size())   return {"", answer.size()};
        if(answer[index_of_one] == "(" or answer[index_of_one] == ")")  return {answer[index_of_one], answer.size()};
        if(answer[index_of_one] == "+") return {"+", answer.size()};
        if(before == -1)
        {
            if(answer[index_of_one] == "/") return {"/", index_of_one};
            if(answer[index_of_one] == "-") return {"-", index_of_one};
        }
        else if(before and answer[index_of_one] == "-")    return {"-", answer.size()};
        temporary_pair = str_to_fraction(answer[index_of_one]);
        temporary_variable = temporary_pair.first;
        if(temporary_pair.second and temporary_variable.numerator != temporary_variable.denominator)    return {answer[index_of_one], index_of_one};
    }
}


auto format_one(vector<string> temporary_group)
{
    static int temporary_step;
    static string temporary_symbol;
    static pair<Fraction, bool> temporary_pair;
    temporary_step = 0;
    while(temporary_step < temporary_group.size())
    {
        temporary_symbol = temporary_group[temporary_step];
        temporary_pair = str_to_fraction(temporary_symbol);
        if(temporary_pair.second and temporary_pair.first.numerator == temporary_pair.first.denominator)
        {
            if(temporary_group.size() == 2) break;
            else if(temporary_step == 1 and temporary_group[temporary_step + 1] == "/")
            {
                temporary_step += 1;
                continue;
            }
            else if(temporary_step == 1 and temporary_group[temporary_step + 1] == "*")
            {
                temporary_group.erase(temporary_group.begin() + temporary_step);
                temporary_group.erase(temporary_group.begin() + temporary_step);
            }
            else
            {
                temporary_group.erase(temporary_group.begin() + temporary_step - 1);
                temporary_group.erase(temporary_group.begin() + temporary_step - 1);
            }
            temporary_step -= 2;
            one_as_a_group += 1;
        }
        temporary_step += 1;
    }
    return temporary_group;
}


auto simplify_formula_forth_part(vector<string> group)
{
    static vector<pair<map<string, string>, map<string, int>>> compare_nums;
    static string part_of_group;
    compare_nums.clear();
    for(int step = 0; step < group.size(); step ++)
    {
        part_of_group = group[step];
        compare_nums.emplace_back(pair<map<string, string>, map<string, int>> ({{"representative", part_of_group},{"operator", char_to_string(part_of_group[0])}},
                                                                               {{"index", step}}));
    }
    sort(compare_nums.begin(), compare_nums.end(), [](auto a, auto b) -> auto{return a.first["representative"] < b.first["representative"];});
    for(int step = 0; step < compare_nums.size(); step ++)
        if(compare_nums[step].first["operator"] == "+")
        {
            swap(compare_nums[0], compare_nums[step]);
            break;
        }
    static vector<string> new_group;
    new_group.clear();
    for(auto & element : compare_nums)
        new_group.emplace_back(group[element.second["index"]]);
    new_group[0] = new_group[0].substr(1);
    return new_group;
}


auto simplify_formula_third_part(vector<string> part_of_group)
{
    if(part_of_group.size() < 3)    return part_of_group;
    static vector<pair<map<string, string>, map<string, int>>> sort_list;
    static string symbol;
    static int min_number;
    sort_list.clear();
    for(int step = 0; step < part_of_group.size(); step ++)
    {
        symbol = part_of_group[step];
        if(symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/" and symbol !="(" and symbol != ")")
            sort_list.emplace_back(pair<map<string, string>, map<string, int>> ({{"representative", symbol},{"operator", part_of_group[step - 1]}},
                                   {{"index", step}}));
    }
    min_number = 0;
    static int temporary_step;
    temporary_step = 0;
    for(auto & element : sort_list)
    {
        if(element.first["operator"] == "*" and sort_list[min_number].first["representative"] > element.first["representative"])
            min_number = temporary_step;
        temporary_step ++;
    }
    if(min_number != 0)
    {
        swap(part_of_group[sort_list[0].second["index"]], part_of_group[sort_list[min_number].second["index"]]);
        sort_list[min_number].first["representative"] = sort_list[0].first["representative"];
    }
    static int first_number;
    first_number = sort_list[0].second["index"] + 1;
    sort_list.erase(sort_list.begin());
    sort(sort_list.begin(), sort_list.end(), [](auto a, auto b) -> auto{return a.first["representative"] < b.first["representative"];});
    static vector<string> new_list;
    new_list.clear();
    for(int i = 0; i < first_number; i ++)
        new_list.emplace_back(part_of_group[i]);
    static int index_of_sort_list;
    static int index;
    index_of_sort_list = 0;
    for(int step = first_number; step < part_of_group.size(); step += 2)
    {
        index = sort_list[index_of_sort_list].second["index"];
        new_list.emplace_back(part_of_group[index - 1]);
        new_list.emplace_back(part_of_group[index]);
        index_of_sort_list ++;
    }
    return new_list;
}


pair<vector<string>, int> simplify_formula_second_part(int step, vector<string> answer, int layer)
{
    vector<string> group;
    vector<string> temporary_group;
    temporary_group.emplace_back("+");
    static string symbol;
    pair<vector<string>, int> temporary_pair_second_part;
    while(step < answer.size())
    {
        symbol = answer[step];
        if(symbol == "+" or symbol == "-")
        {
            temporary_group = format_one(temporary_group);
            temporary_group = simplify_formula_third_part(temporary_group);
            group.emplace_back(str_vector_to_str(temporary_group, false));
            temporary_group.clear();
        }
        if(symbol == "(")
        {
            temporary_pair_second_part = simplify_formula_second_part(step + 1, answer, layer + 1);
            temporary_pair_second_part.first.insert(temporary_pair_second_part.first.begin(), "(");
            temporary_pair_second_part.first.emplace_back(")");
            temporary_group.emplace_back(str_vector_to_str(temporary_pair_second_part.first, false));
            step = temporary_pair_second_part.second + 1;
            continue;
        }
        if(symbol == ")") break;
        temporary_group.emplace_back(symbol);
        step ++;
    }
    temporary_group = format_one(temporary_group);
    temporary_group = simplify_formula_third_part(temporary_group);
    group.emplace_back(str_vector_to_str(temporary_group, false));
    temporary_group.clear();
    if(layer == 0)
    {
        while(one_as_a_group)
        {
            one_as_a_group --;
            group.emplace_back("*1");
        }
    }
    group = simplify_formula_forth_part(group);
    temporary_pair_second_part.first = group, temporary_pair_second_part.second = step;
    return temporary_pair_second_part;
}


auto simplify_formula_first_part(vector<string> answer)
{
    int layer = 0;
    int step = 0;
    static pair<Fraction, bool> temporary_pair;
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
    int temporary_layer;
    static pair<string, int> temporary_symbol_and_index;
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
        symbol = answer[step];
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
                    temporary_pair = str_to_fraction(answer[brackets[layer - 1] - 2]);
                    temporary_fraction = temporary_pair.first;
                    if(answer[brackets[layer - 1] - 1] != "*" and answer[brackets[layer - 1] - 1] != "/")
                    {
                        decision_front = true;
                        if(answer[brackets[layer - 1] - 1] == "-")
                            change_symbol_from_subtraction = true;
                    }
                    else if(temporary_pair.second and temporary_fraction.numerator == temporary_fraction.denominator)
                    {
                        temporary_symbol_and_index = before_or_after_one(brackets[layer - 1] - 2, true, answer);
                        if(temporary_symbol_and_index.first == "/") ;
                        else if(str_to_fraction(temporary_symbol_and_index.first).second)   ;
                        else    decision_front = true;
                        if(temporary_symbol_and_index.first == "-")    change_symbol_from_subtraction = true;
                    }
                }
                else    decision_front = true;
                if(step != answer.size() - 1)
                {
                    temporary_pair = str_to_fraction(answer[step + 2]);
                    temporary_fraction = temporary_pair.first;
                    if(answer[step + 1] != "*" and answer[step + 1] != "/")
                        decision_back = true;
                    else if(temporary_pair.second and temporary_fraction.numerator == temporary_fraction.denominator)
                    {
                        temporary_symbol_and_index = before_or_after_one(step + 2, false, answer);
                        if(str_to_fraction(temporary_symbol_and_index.first).second)    ;
                        else    decision_back = true;
                    }
                }
                else    decision_back = true;
            }
            if(decision_front and decision_back)
            {
                whether_change = true;
                if(change_symbol_from_subtraction or change_symbol_from_division)
                {
                    temporary_layer = 0;
                    for(int temporary_step = brackets[layer - 1] + 1; temporary_step < step; temporary_step ++)
                    {
                        if(change_symbol_from_subtraction and temporary_layer == 0 and answer[temporary_step] == "+")
                            answer[temporary_step] = "-";
                        else if(change_symbol_from_subtraction and temporary_layer == 0 and answer[temporary_step] == "-")
                            answer[temporary_step] = "+";
                        else if(change_symbol_from_division and temporary_layer == 0 and answer[temporary_step] == "*")
                            answer[temporary_step] = "/";
                        else if(change_symbol_from_division and temporary_layer == 0 and answer[temporary_step] == "/")
                            answer[temporary_step] = "*";
                        else if(answer[temporary_step] == "(")
                            temporary_layer += 1;
                        else if(answer[temporary_step] == ")")
                            temporary_layer -= 1;
                    }
                }
                if(whether_found_multiplication_or_division[layer])
                    whether_found_multiplication_or_division[layer - 1] = true;
                if(whether_found_addition_or_subtraction[layer])
                    whether_found_addition_or_subtraction[layer - 1] = true;
                answer.erase(answer.begin() + brackets[layer - 1]);
                answer.erase(answer.begin() + step - 1);
                step -= 2;
            }
            brackets.pop_back();
            layer -= 1;
        }
        if(symbol == "+" or symbol == "-")
            whether_found_addition_or_subtraction[layer] = true;
        else if(symbol == "*" or symbol == "/")
            whether_found_multiplication_or_division[layer] = true;
        step += 1;
    }
//    for(const auto & element : answer)
//        cout << element << ' ';
//    cout << endl;
    return answer;
}


auto calculate_answer(vector<string> answer)
{
    static pair<Fraction, bool> temporary_pair;
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
                    temporary_pair = str_to_fraction(answer[step - 1]);
                    temporary_fraction_front = temporary_pair.first;
                    temporary_pair = str_to_fraction(answer[step + 1]);
                    temporary_fraction_back = temporary_pair.first;
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
                    temporary_pair = str_to_fraction(answer[step - 1]);
                    temporary_fraction_front = temporary_pair.first;
                    temporary_pair = str_to_fraction(answer[step + 1]);
                    temporary_fraction_back = temporary_pair.first;
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
                    temporary_pair = str_to_fraction(answer[step - 1]);
                    temporary_fraction_front = temporary_pair.first;
                    temporary_pair = str_to_fraction(answer[step + 1]);
                    temporary_fraction_back = temporary_pair.first;
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
                    temporary_pair = str_to_fraction(answer[step - 1]);
                    temporary_fraction_front = temporary_pair.first;
                    temporary_pair = str_to_fraction(answer[step + 1]);
                    temporary_fraction_back = temporary_pair.first;
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
    temporary_pair = str_to_fraction(answer[0]);
    Fraction ans = temporary_pair.first;
    if(ans.denominator != 0 and ans.numerator % ans.denominator == 0 and ans.numerator / ans.denominator == 24)
        return "24";
    else
        return "0";
}


auto calculate_whole_answers()
{
    Whole_answers.clear();
    static string old_version;
    static pair<vector<string>, int> temporary_pair_second_part;
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
                                                    // complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        case 1:
                                            switch (bracket_type_ordinal) {
                                                case 1: case 4:
                                                    answer.emplace_back("(");
                                                    // complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        case 2:
                                            switch (bracket_type_ordinal) {
                                                case 2: case 5:
                                                    answer.emplace_back("(");
                                                    // complete_answer += "(";
                                                default: ;
                                            }
                                            break;
                                        default: ;
                                    }
                                    answer.emplace_back(to_string(Four_Numbers[answer_index].numerator) + "/" + to_string(Four_Numbers[answer_index].denominator));
                                    // complete_answer += to_string(Four_Numbers[answer_index].numerator);
                                    switch (answer_index) {
                                        case 1:
                                            switch (bracket_type_ordinal) {
                                                case 0: case 5:
                                                    answer.emplace_back(")");
                                                default: ;
                                            }
                                            break;
                                        case 2:
                                            switch (bracket_type_ordinal) {
                                                case 1: case 3:
                                                    answer.emplace_back(")");
                                                default: ;
                                            }
                                            break;
                                        case 3:
                                            switch (bracket_type_ordinal) {
                                                case 2: case 4: case 5:
                                                    answer.emplace_back(")");
                                                default: ;
                                            }
                                            break;
                                        default: ;
                                    }
                                    if(answer_index >= 0 and answer_index < 3) {
                                        answer.emplace_back(the_Select_Operators[answer_index]);
                                    }
                                }
                                string ans = calculate_answer(answer);
                                if(ans == "24")
                                {
                                    complete_answer = str_vector_to_str(answer, true);
                                    answer = split_to_str_vector(complete_answer);
                                    old_version = "";
                                    while(true)
                                    {
                                        one_as_a_group = 0;
                                        answer = simplify_formula_first_part(answer);
                                        complete_answer = str_vector_to_str(answer, false);
                                        temporary_pair_second_part = simplify_formula_second_part(0, answer, 0);
                                        answer = temporary_pair_second_part.first;
                                        answer = split_to_str_vector(answer);
                                        complete_answer = str_vector_to_str(answer, false);
                                        if(old_version == complete_answer) break;
                                        old_version = complete_answer;
                                    }
                                    if(find(Whole_answers.begin(), Whole_answers.end(), complete_answer) == Whole_answers.end())
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
//        Four_Numbers[0].numerator = 1;
//        Four_Numbers[1].numerator = 1;
//        Four_Numbers[2].numerator = 1;
//        Four_Numbers[3].numerator = 24;
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
            if(Whole_answers.size())
                for(const auto & temporary_answer : Whole_answers)
                cout << temporary_answer << endl;
            else
                cout << "There is no any answers!" << endl;
        }
        else
        {
            break;
        }
    }
    return 0;
}

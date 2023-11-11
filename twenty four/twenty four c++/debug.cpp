#include <iostream>
#include <string>

int main() {
    std::string str = "abc";
    try {
        int num = std::stoi(str);  // 这将抛出一个异常，因为 "abc" 不能转换为整数
    } catch (std::invalid_argument const &e) {
        std::cout << "Invalid argument: " << e.what() << std::endl;
    } catch (std::out_of_range const &e) {
        std::cout << "Out of range: " << e.what() << std::endl;
    } catch (...) {
        std::cout << "Unknown exception caught" << std::endl;
    }
    return 0;
}
